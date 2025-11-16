import pickle
import numpy as np

# Try to load real model
try:
    with open("app/ml/risk_model.pkl", "rb") as f:
        model = pickle.load(f)
    MODEL_AVAILABLE = True
except:
    MODEL_AVAILABLE = False
    print("⚠ No ML model found. Using dummy risk classifier.")

def predict_risk(features):

    if MODEL_AVAILABLE:
        X = np.array([[
            features["missing_sections"],
            features["budget"],
            features["timeline_months"],
            features["inconsistency_score"],
        ]])
        proba = model.predict_proba(X)[0]
        score = float(proba[1])
        label = "High" if score > 0.6 else "Medium" if score > 0.3 else "Low"

        return {"score": score, "label": label}

    # fallback dummy model (safe)
    score = (features["missing_sections"] + features["inconsistency_score"]) / 10
    label = "High" if score > 0.5 else "Low"

    return {"score": score, "label": label}
