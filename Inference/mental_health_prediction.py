import joblib
import sys
import pandas as pd

# Load trained model & vectorizer
model = joblib.load("mental_health_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")  # Ensure this is saved in Step 1
encoder = joblib.load("label_encoder.pkl")  # Ensure this is saved in Step 1

def predict_mental_health(statement):
    # Convert input text to TF-IDF features
    statement_vectorized = vectorizer.transform([statement]).toarray()
    
    # Predict condition
    prediction = model.predict(statement_vectorized)[0]
    condition = encoder.inverse_transform([prediction])[0]
    
    return condition

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict_mental_health.py 'I feel very anxious and nervous'")
    else:
        statement = sys.argv[1]
        prediction = predict_mental_health(statement)
        print("Predicted Mental Health Condition:", prediction)