# Import necessary libraries and modules
import joblib  
import numpy as np
import pandas as pd  
from pathlib import Path

# Define a class named PredictionPipeline
class PredictionPipeline:
    def __init__(self):
        # Load the pre-trained model from the specified file path using joblib
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    # Method to make predictions using the loaded model
    def predict(self, data):
        # Use the loaded model to make predictions on the input data
        prediction = self.model.predict(data)
        
        return prediction
