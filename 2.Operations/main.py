from flask import Flask, render_template, request, flash, redirect
from forms import StudentScoreForm
import requests

app = Flask(__name__)
app.secret_key = "your_secret_key"

API_URL = "http://127.0.0.1:3000/api/prediction"
HEADERS = {"Authorisation": "uPTPeF9BDNiqAkNj"}

@app.route("/", methods=["GET", "POST"])
def predict():
    form = StudentScoreForm()
    if form.validate_on_submit():
        input_data = {
            "Hours_Studied": form.Hours_Studied.data,
            "Attendance": form.Attendance.data,
            "Parental_Involvement": form.Parental_Involvement.data,
            "Access_to_Resources": form.Access_to_Resources.data,
            "Extracurricular_Activities": int(form.Extracurricular_Activities.data),
            "Sleep_Hours": form.Sleep_Hours.data,
            "Previous_Scores": form.Previous_Scores.data,
            "Motivation_Level": form.Motivation_Level.data,
            "Internet_Access": int(form.Internet_Access.data),
            "Tutoring_Sessions": form.Tutoring_Sessions.data,
            "Family_Income": form.Family_Income.data,
            "Teacher_Quality": form.Teacher_Quality.data,
            "School_Type": form.School_Type.data,
            "Peer_Influence": form.Peer_Influence.data,
            "Physical_Activity": form.Physical_Activity.data,
            "Learning_Disabilities": int(form.Learning_Disabilities.data),
            "Parental_Education_Level": form.Parental_Education_Level.data,
            "Distance_from_Home": form.Distance_from_Home.data,
            "Gender": form.Gender.data,
        }

        try:
            response = requests.post(API_URL, json=input_data, headers=HEADERS)
            print(f"API Response: {response.status_code}, {response.text}")  # Debugging line
            response_data = response.json()

            if response.status_code == 200:
                flash(f"Predicted Exam Score: {response_data['prediction']}", "success")
            else:
                flash(f"Error: {response_data.get('message', 'Unknown error')}", "danger")
        except Exception as e:
            print(f"Error connecting to API: {e}")  # Debugging line
            flash(f"Error connecting to API: {str(e)}", "danger")
        return redirect("/")
    return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)