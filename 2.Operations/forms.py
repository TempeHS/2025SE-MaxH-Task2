from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class StudentScoreForm(FlaskForm):
    Hours_Studied = FloatField(
        "Hours Studied",
        validators=[DataRequired(), NumberRange(min=0, message="Must be a positive number")],
        render_kw={"type": "number", "step": "any"},
    )
    Attendance = IntegerField(
        "Attendance (%)",
        validators=[DataRequired(), NumberRange(min=0, max=100, message="Must be between 0 and 100")],
    )
    Parental_Involvement = SelectField(
        "Parental Involvement",
        choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")],
        validators=[DataRequired()],
    )
    Access_to_Resources = SelectField(
        "Access to Resources",
        choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")],
        validators=[DataRequired()],
    )
    Extracurricular_Activities = BooleanField("Participates in Extracurricular Activities?")
    Sleep_Hours = FloatField(
        "Sleep Hours",
        validators=[DataRequired(), NumberRange(min=0, message="Must be a positive number")],
        render_kw={"type": "number", "step": "any"},
    )
    Previous_Scores = IntegerField(
        "Previous Scores",
        validators=[DataRequired(), NumberRange(min=0, max=100, message="Must be between 0 and 100")],
    )
    Motivation_Level = SelectField(
        "Motivation Level",
        choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")],
        validators=[DataRequired()],
    )
    Internet_Access = BooleanField("Has Internet Access?")
    Tutoring_Sessions = IntegerField(
        "Number of Tutoring Sessions",
        validators=[DataRequired(), NumberRange(min=0, message="Must be a positive number")],
    )
    Family_Income = SelectField(
        "Family Income",
        choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")],
        validators=[DataRequired()],
    )
    Teacher_Quality = SelectField(
        "Teacher Quality",
        choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")],
        validators=[DataRequired()],
    )
    School_Type = SelectField(
        "School Type",
        choices=[("Public", "Public"), ("Private", "Private")],
        validators=[DataRequired()],
    )
    Peer_Influence = SelectField(
        "Peer Influence",
        choices=[("Negative", "Negative"), ("Neutral", "Neutral"), ("Positive", "Positive")],
        validators=[DataRequired()],
    )
    Physical_Activity = IntegerField(
        "Physical Activity (hours per week)",
        validators=[DataRequired(), NumberRange(min=0, message="Must be a positive number")],
    )
    Learning_Disabilities = BooleanField("Has Learning Disabilities?")
    Parental_Education_Level = SelectField(
        "Parental Education Level",
        choices=[
            ("High School", "High School"),
            ("College", "College"),
            ("Postgraduate", "Postgraduate"),
        ],
        validators=[DataRequired()],
    )
    Distance_from_Home = SelectField(
        "Distance from Home",
        choices=[("Near", "Near"), ("Moderate", "Moderate"), ("Far", "Far")],
        validators=[DataRequired()],
    )
    Gender = SelectField(
        "Gender",
        choices=[("Male", "Male"), ("Female", "Female")],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")