import pandas as pd

data = {
    "battery": [95, 90, 85, 80, 70, 60, 50, 40, 30, 20, 15, 10],

    "signal": [95, 90, 88, 85, 80, 75, 65, 60, 55, 45, 40, 30],

    "packet_loss": [1, 2, 3, 4, 5, 7, 10, 14, 18, 25, 35, 50],

    "delay": [20, 22, 25, 30, 35, 45, 55, 70, 90, 120, 150, 200],

    "status": [
        "Healthy",
        "Healthy",
        "Healthy",
        "Healthy",
        "Healthy",
        "Healthy",
        "Healthy",
        "Warning",
        "Warning",
        "Warning",
        "Failing",
        "Failing"
    ]
}

df = pd.DataFrame(data)

print(df)

X = df[["battery", "signal", "packet_loss", "delay"]]

y = df["status"]

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

new_sensor = pd.DataFrame(
    [[18, 42, 32, 145]],
    columns=["battery", "signal", "packet_loss", "delay"]
)

prediction = model.predict(new_sensor)

print("Prediction:", prediction[0])

probability = model.predict_proba(new_sensor)

print("Probabilities:", probability)

print(model.classes_)

import random
import pandas as pd

data = []

for i in range(10000):

    battery = random.uniform(5, 100)
    signal = random.uniform(20, 100)
    packet_loss = random.uniform(0, 50)
    delay = random.uniform(10, 200)

    # Decide the status for this simulated example
    if battery < 20 and packet_loss > 25:
        status = "Failing"

    elif packet_loss > 30 and delay > 120:
        status = "Failing"

    elif battery < 35 or signal < 50 or packet_loss > 15 or delay > 80:
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

print(df.head(20))

print("\nTotal examples:", len(df))
