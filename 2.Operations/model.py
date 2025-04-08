import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

class MLModel:
    def __init__(self, model=None, poly_transformer=None):
        self.model = model
        self.poly_transformer = poly_transformer

    def load_model(self, model_path, poly_path):
        try:
            with open(model_path, "rb") as model_file:
                self.model = pickle.load(model_file)
            with open(poly_path, "rb") as poly_file:
                self.poly_transformer = pickle.load(poly_file)
            print(f"Model and polynomial transformer loaded successfully from {model_path} and {poly_path}")
        except FileNotFoundError:
            print(f"Error: Model or transformer file not found at {model_path} or {poly_path}")
        except Exception as e:
            print(f"Error loading model or transformer: {e}")

    def preprocess_input(self, input_data):
        input_df = pd.DataFrame([input_data])
        required_features = ['Hours_Studied', 'Attendance', 'Previous_Scores']
        for feature in required_features:
            if feature not in input_df:
                raise ValueError(f"Missing required feature: {feature}")
        poly_features = self.poly_transformer.transform(input_df)
        return poly_features

    def predict(self, input_data):
        if not self.model or not self.poly_transformer:
            raise ValueError("Model or polynomial transformer is not loaded properly.")
        try:
            preprocessed_data = self.preprocess_input(input_data)
            prediction = self.model.predict(preprocessed_data)
            return round(prediction[0], 2)
        except Exception as e:
            print(f"Prediction failed: {e}")
            raise