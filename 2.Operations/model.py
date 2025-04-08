import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

class MLModel:
    def __init__(self, model=None, poly_transformer=None, scaling_params=None):
        self.model = model
        self.poly_transformer = poly_transformer
        self.scaling_params = scaling_params  # Dictionary to store min-max values for scaling

    def load_model(self, model_path, poly_path, scaling_params_path=None):
        try:
            with open(model_path, "rb") as model_file:
                self.model = pickle.load(model_file)
            with open(poly_path, "rb") as poly_file:
                self.poly_transformer = pickle.load(poly_file)
            if scaling_params_path:
                with open(scaling_params_path, "rb") as scaling_file:
                    self.scaling_params = pickle.load(scaling_file)
            print(f"Model, polynomial transformer, and scaling parameters loaded successfully.")
            print("Loaded Scaling Parameters:", self.scaling_params)
        except FileNotFoundError:
            print(f"Error: Model, transformer, or scaling parameters file not found.")
        except Exception as e:
            print(f"Error loading model, transformer, or scaling parameters: {e}")

    def preprocess_input(self, input_data):
        input_df = pd.DataFrame([input_data])
        print("Raw Input Data (before scaling):")
        print(input_df)

        # Encode categorical variables
        encoding_map = {
            "Parental_Involvement": {"Low": 1, "Medium": 2, "High": 3},
            "Access_to_Resources": {"Low": 1, "Medium": 2, "High": 3},
            "Motivation_Level": {"Low": 1, "Medium": 2, "High": 3},
            "Family_Income": {"Low": 1, "Medium": 2, "High": 3},
            "Teacher_Quality": {"Low": 1, "Medium": 2, "High": 3},
            "School_Type": {"Public": -1, "Private": 1},
            "Peer_Influence": {"Negative": -1, "Neutral": 0, "Positive": 1},
            "Parental_Education_Level": {"High School": 1, "College": 2, "Postgraduate": 3},
            "Distance_from_Home": {"Near": 1, "Moderate": 2, "Far": 3},
            "Gender": {"Male": -1, "Female": 1},
            "Internet_Access": {False: -1, True: 1},
            "Extracurricular_Activities": {False: -1, True: 1},
            "Learning_Disabilities": {False: -1, True: 1},
        }

        for column, mapping in encoding_map.items():
            if column in input_df:
                input_df[column] = input_df[column].map(mapping)

        # Create engineered features
        input_df["Knowledge"] = input_df["Hours_Studied"] * input_df["Previous_Scores"]
        input_df["Engagement"] = input_df["Attendance"] * input_df["Hours_Studied"]

        # Select only the required features for the model
        model_features = ["Engagement", "Knowledge", "Attendance"]
        input_df = input_df[model_features]

        # Fill missing values for optional features with defaults
        input_df.fillna(0, inplace=True)

        # Scale numerical features using saved min-max values
        if self.scaling_params:
            for feature in model_features:
                if feature in self.scaling_params:
                    min_val, max_val = self.scaling_params[feature]
                    input_df[feature] = (input_df[feature] - min_val) / (max_val - min_val)

        # Log the scaled inputs for debugging
        print("Scaled Input Data:")
        print(input_df)

        # Transform input data using the polynomial transformer
        poly_features = self.poly_transformer.transform(input_df)
        return poly_features

    def predict(self, input_data):
        if not self.model or not self.poly_transformer:
            raise ValueError("Model or polynomial transformer is not loaded properly.")
        try:
            # Preprocess the input data
            preprocessed_data = self.preprocess_input(input_data)
            
            # Get the scaled prediction
            scaled_prediction = self.model.predict(preprocessed_data)[0]
            
            # Reverse scale the prediction
            if "Exam_Score" in self.scaling_params:
                min_val, max_val = self.scaling_params["Exam_Score"]
                original_prediction = (scaled_prediction * (max_val - min_val)) + min_val
            else:
                original_prediction = scaled_prediction  # If no scaling params, return as is
            
            return round(original_prediction, 2)
        except Exception as e:
            print(f"Prediction failed: {e}")
            raise