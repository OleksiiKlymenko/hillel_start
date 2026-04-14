from flask import Flask, render_template
from flask import request

from flask_home_work.F1Teams import generate_teams

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", result = "This is the main page")

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

app.run(debug=True)    # запускаємо локальний сервер