import numpy as np
import tensorflow as tf
from PIL import Image
from io import BytesIO

model = None

def load_model():
  model = tf.keras.models.load_model('./model_capstone.h5')
  return model

def predict_image(image: Image.Image):
  global model
  if model is None:
    model = load_model()
    
  image = np.asarray(image.resize((300, 300)))[..., :3]
  image = np.expand_dims(image, 0)
  image = image / 127.5 - 1.0
  
  class_probabilities = model.predict(image) 

  class_names = ['ayam', 'brokoli', 'jagung', 'kacang_tanah', 'kangkung', 'kentang', 'labu', 'labu_siam', 'lobak_merah', 'mentimun', 'nanas', 'nangka', 'nasi_putih', 'paprika', 'pare', 'pepaya', 'pisang', 'singkong', 'tahu', 'telur', 'tempe', 'terong', 'tomat', 'ubi', 'wortel']
  predicted_classes_index = np.argmax(class_probabilities)
  predicted = class_names[predicted_classes_index]
        
  return predicted
    
def read_imagefile(file) -> Image.Image:
  image = Image.open(BytesIO(file))
  return image