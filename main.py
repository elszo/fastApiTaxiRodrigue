from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import uvicorn
import pandas as pd

app = FastAPI()

class Item(BaseModel):
    pickup_longitude: float
    pickup_latitude: float
    dropoff_longitude: float
    dropoff_latitude: float
    hour: int
    weekday: int
    month: int


class Predictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, features):
        return self.model.predict(features)[0]

# Charger le modèle pré-entraîné
model_path = "./models/taxi.model"
predictor = Predictor(model_path)

@app.get("/")
def root():
    return {"message": "Hello!"}

@app.post("/predict")
async def predict(item: Item):

    features = pd.DataFrame.from_dict({
        'pickup_longitude': [item.pickup_longitude],
        'pickup_latitude': [item.pickup_latitude],
        'dropoff_longitude': [item.dropoff_longitude],
        'dropoff_latitude': [item.dropoff_latitude],
        'hour': [item.hour],
        'weekday': [item.weekday],
        'month': [item.month]
    })

    prediction = predictor.predict(features)
    prediction = round(prediction)

    heures, reste = divmod(prediction, 3600)
    minutes, secondes = divmod(reste, 60)

    resultat = f"Durée du voyage: {prediction}s"
    if heures > 0:
        resultat = f"Durée du voyage: {heures}h {minutes}mn {secondes}s"
    elif minutes > 0:
        resultat = f"Durée du voyage: {minutes}mn {secondes}s"

    return {resultat}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1",
                port=8000, reload=True)