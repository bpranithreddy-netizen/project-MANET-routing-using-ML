network = {
    "S1": ["S2", "S3"],
    "S2": ["S1", "S3", "S4"],
    "S3": ["S1", "S2", "S4"],
    "S4": ["S2", "S3", "S5"],
    "S5": ["S4", "Gateway"],
    "Gateway": ["S5"]
}

from collections import deque


def find_route(network, start, destination):

    queue = deque()

    queue.append([start])

    visited = set()

    visited.add(start)

    while queue:

        route = queue.popleft()

        current = route[-1]

        if current == destination:
            return route

        for neighbor in network[current]:

            if neighbor not in visited:

                visited.add(neighbor)

                new_route = route + [neighbor]

                queue.append(new_route)

    return None

route = find_route(
    network,
    "S1",
    "Gateway"
)

print("Route:", route)

failed_sensor = "S3"

def remove_failed_sensor(network, failed_sensor):

    new_network = {}

    for node in network:

        if node == failed_sensor:
            continue

        new_network[node] = []

        for neighbor in network[node]:

            if neighbor != failed_sensor:

                new_network[node].append(neighbor)

    return new_network

failed_sensor = "S3"

new_network = remove_failed_sensor(
    network,
    failed_sensor
)

route = find_route(
    new_network,
    "S1",
    "Gateway"
)

print("New route:", route)

