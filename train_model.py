import random
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

data = []

for i in range(10000):

    battery = random.uniform(5, 100)
    signal = random.uniform(20, 100)
    packet_loss = random.uniform(0, 50)
    delay = random.uniform(10, 200)

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

X = df[
    [
        "battery",
        "signal",
        "packet_loss",
        "delay"
    ]
]

y = df["status"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)


new_sensor = pd.DataFrame(
    [[18, 42, 32, 145]],
    columns=[
        "battery",
        "signal",
        "packet_loss",
        "delay"
    ]
)

prediction = model.predict(new_sensor)

print("\nNew Sensor:")
print("Prediction:", prediction[0])

probability = model.predict_proba(new_sensor)

print("Probabilities:", probability)

print("Classes:", model.classes_)
