import pickle

lead = {
    "lead_source": "paid_ads",
    "industry": "technology",
    "employment_status": "employed",
    "location": "north_america",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0,
    "interaction_count": 4,
    "lead_score": 0.41,
}

# Load the trained model
with open("pipeline.bin", "rb") as f:
    model = pickle.load(f)

# Inspect the class labels
print("Classes:", model.classes_)

# Predict the probabilities
probabilities = model.predict_proba([lead])
print("All probabilities:", probabilities)

# Get the probability for converted = 1
positive_index = list(model.classes_).index(1)
probability = probabilities[0][positive_index]

print(f"Conversion probability: {probability:.3f}")
