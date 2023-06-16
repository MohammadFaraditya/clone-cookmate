from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

from classifier_helpers import predict_image, read_imagefile
from recipe_helpers import get_recommendation, get_all_recipes, get_detail_recipe, get_all_ingredients, get_specific_ingredients, get_specific_recipes

app = FastAPI(title='CookMate!')
app.mount("/static", StaticFiles(directory="documentation/static"), name="static")

@app.get("/")
async def read_root():
    return {"CookMate-API"}

@app.get("/recipes", status_code=200)
async def recipes(name: str | None = None):
    if name:
        recipes = get_specific_recipes(name)
    else:
        recipes = get_all_recipes()
    
    return {"data": recipes}

@app.get("/recipes/{id}", status_code=200)
async def detail_recipe(id: str):
    
    recipe = get_detail_recipe(id)
    
    return {"data": recipe}

@app.get("/ingredients", status_code=200)
async def ingredients(name: str | None = None):
    if name:
        ingredients = get_specific_ingredients(name)
    else:
        ingredients = get_all_ingredients()
    
    return {"data": ingredients}

@app.post("/predict", status_code=200)
async def predict_img(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg","jpeg","png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = predict_image(image)
    recommendation_result = get_recommendation([prediction])
    
    return {"data": recommendation_result}

@app.post("/recommend", status_code=200)
async def predict_text(request: Request):
    request_body = await request.json()
    
    ingredients_list = request_body['ingredients'].split(",")
    
    recommendation_result = get_recommendation(ingredients_list)
    
    return {"data": recommendation_result}


@app.get("/api-doc", status_code=200)
async def show_api_doc(request: Request):
    file_path= os.path.join(os.getcwd(), "documentation", "index.html")
    with open(file_path, "r") as file:
        content = file.read()
    return HTMLResponse(content)

if __name__ == "__main__":
    uvicorn.run(app, debug=True)