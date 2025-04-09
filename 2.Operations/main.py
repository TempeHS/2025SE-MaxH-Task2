from flask import Flask, render_template, request, flash, redirect, url_for
from forms import StudentScoreForm
import requests
import sqlite3  # For database operations

app = Flask(__name__)
app.secret_key = "your_secret_key"

API_URL = "http://127.0.0.1:3000/api/prediction"
HEADERS = {"Authorisation": "uPTPeF9BDNiqAkNj"}

# Database setup
DATABASE = "user_inputs.db"

def init_db():
    """Initialize the database and create the table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_inputs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Hours_Studied REAL,
            Attendance REAL,
            Parental_Involvement REAL,
            Access_to_Resources REAL,
            Extracurricular_Activities INTEGER,
            Sleep_Hours REAL,
            Previous_Scores REAL,
            Motivation_Level REAL,
            Internet_Access INTEGER,
            Tutoring_Sessions REAL,
            Family_Income REAL,
            Teacher_Quality REAL,
            School_Type REAL,
            Peer_Influence REAL,
            Physical_Activity REAL,
            Learning_Disabilities INTEGER,
            Parental_Education_Level REAL,
            Distance_from_Home REAL,
            Gender REAL
        )
    """)
    conn.commit()
    conn.close()

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
            # Send the input data to the prediction API
            response = requests.post(API_URL, json=input_data, headers=HEADERS)
            response_data = response.json()

            if response.status_code == 200:
                print("Input Data Sent to API:", input_data)
                flash(f"Predicted Exam Score: {response_data['prediction']}", "success")

                # Store the input data in the session for saving later
                request.session = input_data

                # Prompt the user to save their inputs
                flash("Do you want to save your inputs for future model training?", "info")
                return render_template("index.html", form=form, save_prompt=True)

            else:
                flash(f"Error: {response_data.get('message', 'Unknown error')}", "danger")
        except Exception as e:
            flash(f"Error connecting to API: {str(e)}", "danger")

    # Handle saving inputs if the user presses the "Save" button
    if request.method == "POST" and request.form.get("save_inputs") == "yes":
        try:
            input_data = request.session
            if not input_data:
                flash("No input data found to save.", "danger")
                return render_template("index.html", form=form, save_prompt=False)
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO user_inputs (
                    Hours_Studied, Attendance, Parental_Involvement, Access_to_Resources,
                    Extracurricular_Activities, Sleep_Hours, Previous_Scores, Motivation_Level,
                    Internet_Access, Tutoring_Sessions, Family_Income, Teacher_Quality,
                    School_Type, Peer_Influence, Physical_Activity, Learning_Disabilities,
                    Parental_Education_Level, Distance_from_Home, Gender
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, tuple(request.session.values()))
            conn.commit()
            conn.close()
            flash("Your inputs have been saved successfully!", "success")
        except Exception as e:
            flash(f"Error saving inputs: {str(e)}", "danger")    
    return render_template("index.html", form=form, save_prompt=False)

if __name__ == "__main__":
    init_db()  # Initialize the database
    app.run(debug=True, host="0.0.0.0", port=5000)