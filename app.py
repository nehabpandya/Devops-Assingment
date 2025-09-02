from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for workouts
workouts = []


@app.route("/")
def home():
    return jsonify({"message": "Welcome to ACEestFitness and Gym API"})


@app.route("/workouts", methods=["POST"])
def add_workout():
    data = request.get_json()
    workout = data.get("workout")
    duration = data.get("duration")

    if not workout or duration is None:
        return jsonify({"error": "Please provide both workout and duration"}), 400

    try:
        duration = int(duration)
    except ValueError:
        return jsonify({"error": "Duration must be a number"}), 400

    entry = {"workout": workout, "duration": duration}
    workouts.append(entry)

    return jsonify({"message": f"'{workout}' added successfully!", "workout": entry}), 201


@app.route("/workouts", methods=["GET"])
def view_workouts():
    if not workouts:
        return jsonify({"message": "No workouts logged yet."}), 200
    return jsonify({"workouts": workouts})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)
