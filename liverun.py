import random
import time
import pandas as pd

from sklearn.ensemble import RandomForestClassifier


# --------------------------------------------------
# STEP 1: CREATE TRAINING DATA
# --------------------------------------------------

# --------------------------------------------------
# CREATE TRAINING DATA
# --------------------------------------------------

data = []

for i in range(10000):

    battery = random.uniform(5, 100)
    signal = random.uniform(20, 100)
    packet_loss = random.uniform(0, 50)
    delay = random.uniform(10, 200)

    # Calculate a health score
    score = 0

    # Battery
    if battery < 20:
        score += 3
    elif battery < 40:
        score += 1

    # Signal
    if signal < 40:
        score += 3
    elif signal < 60:
        score += 1

    # Packet loss
    if packet_loss > 30:
        score += 3
    elif packet_loss > 15:
        score += 1

    # Delay
    if delay > 150:
        score += 3
    elif delay > 80:
        score += 1

    # Decide status based on total problem score
    if score >= 6:
        status = "Failing"

    elif score >= 2:
        status = "Warning"

    else:
        status = "Healthy"

    data.append([
        battery,
        signal,
        packet_loss,
        delay,
        status
    ])


# --------------------------------------------------
# CREATE DATAFRAME
# --------------------------------------------------

df = pd.DataFrame(
    data,
    columns=[
        "battery",
        "signal",
        "packet_loss",
        "delay",
        "status"
    ]
)


# --------------------------------------------------
# SEPARATE INPUTS AND OUTPUT
# --------------------------------------------------

X = df[
    [
        "battery",
        "signal",
        "packet_loss",
        "delay"
    ]
]

y = df["status"]


# --------------------------------------------------
# CREATE AND TRAIN RANDOM FOREST
# --------------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)


# --------------------------------------------------
# STEP 5: CREATE OUR VIRTUAL SENSORS
# --------------------------------------------------

sensors = {

    "S1": {
        "battery": 95,
        "signal": 90,
        "packet_loss": 2,
        "delay": 25
    },

    "S2": {
        "battery": 85,
        "signal": 88,
        "packet_loss": 3,
        "delay": 30
    },

    "S3": {
        "battery": 90,
        "signal": 85,
        "packet_loss": 2,
        "delay": 25
    },

    "S4": {
        "battery": 80,
        "signal": 92,
        "packet_loss": 2,
        "delay": 20
    },

    "S5": {
        "battery": 90,
        "signal": 87,
        "packet_loss": 3,
        "delay": 28
    }
}


# --------------------------------------------------
# STEP 6: SIMULATE S3 FAILURE
# --------------------------------------------------

def simulate_failure():

    sensors["S3"]["battery"] -= random.uniform(0.5, 1.5)

    sensors["S3"]["signal"] -= random.uniform(1, 3)

    sensors["S3"]["packet_loss"] += random.uniform(2, 5)

    sensors["S3"]["delay"] += random.uniform(5, 15)


# --------------------------------------------------
# STEP 7: AI ANALYZES EVERY SENSOR
# --------------------------------------------------

def analyze_sensors():

    for name, sensor in sensors.items():

        # Convert the current sensor data into a DataFrame
        sensor_data = pd.DataFrame(
            [[
                sensor["battery"],
                sensor["signal"],
                sensor["packet_loss"],
                sensor["delay"]
            ]],
            columns=[
                "battery",
                "signal",
                "packet_loss",
                "delay"
            ]
        )

        # Ask the AI to predict the sensor's condition
        prediction = model.predict(sensor_data)[0]

        # Get probability for each class
        probabilities = model.predict_proba(sensor_data)[0]

        # Get class names
        classes = model.classes_

        # Match each class with its probability
        probability_dict = dict(
            zip(classes, probabilities)
        )

        # Get failing probability
        failing_probability = probability_dict["Failing"] * 100

        print(
            name,
            "| Battery:",
            round(sensor["battery"], 1),
            "%",
            "| Signal:",
            round(sensor["signal"], 1),
            "| Loss:",
            round(sensor["packet_loss"], 1),
            "%",
            "| Delay:",
            round(sensor["delay"], 1),
            "ms",
            "| AI:",
            prediction,
            "| Failing:",
            round(failing_probability, 1),
            "%"
        )


# --------------------------------------------------
# STEP 8: RUN THE NETWORK EVERY SECOND
# --------------------------------------------------

while True:

    # Make S3 gradually fail
    simulate_failure()

    print("\n==============================================")
    print("             AI SENSOR MONITOR")
    print("==============================================")

    # Let AI analyze all five sensors
    analyze_sensors()

    time.sleep(1)
