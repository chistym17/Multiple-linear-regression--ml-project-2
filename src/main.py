import joblib
import pandas as pd
model = joblib.load('notebook/multiple_linear_regression_model.pkl')

def predict_performance(hours_studied, previous_scores, extracurricular_activities, sleep_hours, question_papers_practiced):
    extracurricular_activities = 1 if extracurricular_activities.lower() == 'yes' else 0
    
    input_data = pd.DataFrame({
        'Hours Studied': [hours_studied],
        'Previous Scores': [previous_scores],
        'Extracurricular Activities': [extracurricular_activities],
        'Sleep Hours': [sleep_hours],
        'Sample Question Papers Practiced': [question_papers_practiced]
    })
    
    prediction = model.predict(input_data)
    
    return prediction[0]

if __name__ == "__main__":
    hours_studied = 6
    previous_scores = 85
    extracurricular_activities = 'Yes'
    sleep_hours = 7
    question_papers_practiced = 3
    
    predicted_performance = predict_performance(
        hours_studied,
        previous_scores,
        extracurricular_activities,
        sleep_hours,
        question_papers_practiced
    )
    
    print(f"Predicted Performance Index: {predicted_performance:.2f}")
