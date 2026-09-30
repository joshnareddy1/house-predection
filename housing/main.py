from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import joblib

app = FastAPI()

model = joblib.load("model_trained.pk2")

template = Jinja2Templates(directory="template")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home(request: Request):
    return template.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/predict")
def predict(
    request: Request,
    avg_area_income: float = Form(...),
    avg_area_house_age: float = Form(...),
    avg_area_number_of_rooms: float = Form(...),
    avg_area_number_of_bedrooms: float = Form(...),
    area_population: float = Form(...)
):

    input_data = [[
        avg_area_income,
        avg_area_house_age,
        avg_area_number_of_rooms,
        avg_area_number_of_bedrooms,
        area_population
    ]]

    prediction = model.predict(input_data)

    return template.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": float(prediction[0])
        }
    )