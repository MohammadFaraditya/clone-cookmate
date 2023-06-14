FROM python:3.11

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8050

# CMD ["python", "-u", "main.py"]

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8050", "main:app"]