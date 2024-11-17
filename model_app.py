from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

class Input(BaseModel):
    department: str
    region: str
    education: str
    gender: str
    recruitment_channel: str
    no_of_trainings: int
    age: int
    previous_year_rating: float
    length_of_service:int
    KPIs_met : int
    awards_won : int
    avg_training_score: int


class Output(BaseModel):
    is_promoted: int

@app.post("/predict", response_model=Output)
def predict(data_input: Input) -> Output:
    x_input = pd.DataFrame([{
        'department': data_input.department,
        'region': data_input.region,
        'education': data_input.education,
        'gender': data_input.gender,
        'recruitment_channel': data_input.recruitment_channel,
        'no_of_trainings': data_input.no_of_trainings,
        'age': data_input.age,
        'previous_year_rating': data_input.previous_year_rating,
        'length_of_service': data_input.length_of_service,
        'KPIs_met >80%': data_input.KPIs_met,
        'awards_won?': data_input.awards_won,
        'avg_training_score': data_input.avg_training_score
}])
    
    model = joblib.load('promotion_model.pkl')
    prediction = model.predict(x_input)[0]  # Get the single prediction value
    return Output(is_promoted=int(prediction))
