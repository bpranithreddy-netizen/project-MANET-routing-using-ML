import random
import time
import sklearn
import pandas

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
        "battery": 45,
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


def update_sensors():

    for sensor in sensors.values():

        sensor["battery"] -= random.uniform(0, 0.2)

        sensor["signal"] += random.uniform(-2, 2)

        sensor["packet_loss"] += random.uniform(-1, 1)

        sensor["delay"] += random.uniform(-3, 3)

        sensor["signal"] = max(0, min(100, sensor["signal"]))
        sensor["packet_loss"] = max(0, min(100, sensor["packet_loss"]))
        sensor["delay"] = max(1, sensor["delay"])


def display_sensors():

    print("\n-----------------------------")
    print("     SENSOR NETWORK")
    print("-----------------------------")

    for name, sensor in sensors.items():

        status = check_sensor_health(sensor)

        print(
            name,
            "| Battery:", round(sensor["battery"], 1), "%",
            "| Signal:", round(sensor["signal"], 1),
            "| Loss:", round(sensor["packet_loss"], 1), "%",
            "| Delay:", round(sensor["delay"], 1), "ms",
            "| Status:", status
        )
        
def simulate_failure():

    sensors["S3"]["battery"] -= random.uniform(0.5, 1.5)

    sensors["S3"]["signal"] -= random.uniform(1, 3)

    sensors["S3"]["packet_loss"] += random.uniform(2, 5)

    sensors["S3"]["delay"] += random.uniform(5, 15)

def check_sensor_health(sensor):
    if (
        sensor["battery"] < 20
        or sensor["signal"] < 40
        or sensor["packet_loss"] > 30
        or sensor["delay"] > 150
    ):
        return "FAILING"

    elif (
        sensor["battery"] < 40
        or sensor["signal"] < 60
        or sensor["packet_loss"] > 15
        or sensor["delay"] > 80
    ):
        return "WARNING"

    else:
        return "HEALTHY"


while True:

    update_sensors()

    simulate_failure()

    display_sensors()

    time.sleep(1)
