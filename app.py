import pickle
import flask

# Use pickle to load in the pre-trained model.
with open(
    f"model/<..............>", "rb"
) as f:  # File Model Ada di Drive intip.in/ModelKel4ITS02
    model = pickle.load(f)
app = flask.Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def main():
    if flask.request.method == "GET":
        return flask.render_template("main.html")
    if flask.request.method == "POST":
        MinTemp = flask.request.form["MinTemp"]
        MaxTemp = flask.request.form["MaxTemp"]
        Evaporation = flask.request.form["Evaporation"]
        Sunshine = flask.request.form["Sunshine"]
        WindGustDir = flask.request.form["WindGustDir"]
        WindGustSpeed = flask.request.form["WindGustSpeed"]
        WindDir9am = flask.request.form["WindDir9am"]
        WindDir3pm = flask.request.form["WindDir3pm"]
        WindSpeed9am = flask.request.form["WindSpeed9am"]
        Humidity9am = flask.request.form["Humidity9am"]
        Pressure9am = flask.request.form["Pressure9am"]
        Cloud9am = flask.request.form["Cloud9am"]
        Temp9am = flask.request.form["Temp9am"]
        RainToday = flask.request.form["RainToday"]
        input_variables = pd.DataFrame(
            [
                [
                    MinTemp,
                    MaxTemp,
                    Evaporation,
                    Evaporation,
                    Sunshine,
                    WindGustDir,
                    WindGustSpeed,
                    WindDir9am,
                    WindDir3pm,
                    WindSpeed9am,
                    Humidity9am,
                    Pressure9am,
                    Cloud9am,
                    Temp9am,
                    RainToday,
                ]
            ],
            columns=[
                "MinTemp",
                "MaxTemp",
                "Evaporation",
                "Sunshine",
                "WindGustDir",
                "WindGustSpeed",
                "WindDir9am",
                "WindDir3pm",
                "WindSpeed9am",
                "Humidity9am",
                "Pressure9am",
                "Cloud9am",
                "Temp9am",
                "RainToday",
            ],
            dtype=float,
        )
        prediction = model.predict(input_variables)[0]
        return flask.render_template(
            "main.html",
            original_input={
                "MinTemp": MinTemp,
                "MaxTemp": MaxTemp,
                "Evaporation": Evaporation,
                "Sunshine": Sunshine,
                "WindGustDir": WindGustDir,
                "WindGustSpeed": WindGustSpeed,
                "WindDir9am": WindDir9am,
                "WindDir3pm": WindDir3pm,
                "WindSpeed9am": WindSpeed9am,
                "Humidity9am": Humidity9am,
                "Pressure9am": Pressure9am,
                "Cloud9am": Cloud9am,
                "Temp9am": Temp9am,
                "RainToday": RainToday,
            },
            result=prediction,
        )


if __name__ == "__main__":
    app.run()