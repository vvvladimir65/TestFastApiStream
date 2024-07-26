from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('model.pkl')

# Initialize FastAPI app
FastApiReg = FastAPI()

# Add CORS middleware
FastApiReg.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific allowed origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Define request model for input data
class InputData(BaseModel):
    BedroomCount:float
    LivingArea:float
    BathroomCount:float
    StateOfBuilding_Encoded:float
    # MonthlyCharges:float
    SwimmingPool:float
    # NumberOfFacades:float
    RoomCount: float

# API endpoint for predictions
@FastApiReg.post('/predict/')
def predict(input_data: InputData):
    # Print input for debugging purposes
    # print(input_data)

    # Organize input data into a DataFrame directly
    data = pd.DataFrame({
        "BedroomCount": [input_data.BedroomCount],
        "LivingArea": [input_data.LivingArea],
        "BathroomCount": [input_data.BathroomCount],
        "StateOfBuilding_Encoded": [input_data.StateOfBuilding_Encoded],
        # "MonthlyCharges": [input_data.MonthlyCharges],
        "SwimmingPool": [input_data.SwimmingPool],
        # "NumberOfFacades": [input_data.NumberOfFacades],
        "RoomCount": [input_data.RoomCount]
    })
    # Make prediction
    prediction = model.predict(data)
    
    # Return predicted value
    return {"prediction": prediction[0]}

@FastApiReg.get("/")
def read_root():
    return {"message": "Welcome to the ML Model API!"}