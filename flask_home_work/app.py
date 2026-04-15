from flask import Flask, render_template
from flask import request

from flask_home_work.F1Teams import generate_teams

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", result = "Це основна сторінка")

@app.route("/f1_teams")
def list_f1_teams():
    data = generate_teams()
    return render_template("teams.html", teams = data)

@app.route("/drivers/<name>")
def drivers(name):
    all_teams = generate_teams()
    found_driver = None

    for team in all_teams:
        if team.driver == name:
            found_driver = team
            break

    if found_driver:
        return render_template("driver_info.html", driver=found_driver)


@app.route("/your_vote")
def your_vote():
    all_teams = generate_teams()
    return render_template("your_vote.html", teams=all_teams)


@app.route("/check_winner", methods=["POST"])
def check_winner():
    user_team = request.form.get("selected_team")
    user_driver = request.form.get("selected_driver")

    ferrari_drivers = ["Lewis Hamilton", "Charles Leclerc"]

    is_ferrari = ("Ferrari" in user_team) and (user_driver in ferrari_drivers)

    return render_template("result.html",
                           team=user_team,
                           driver=user_driver,
                           is_ferrari=is_ferrari)

app.run(debug=True)