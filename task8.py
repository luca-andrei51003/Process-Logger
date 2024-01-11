from datetime import datetime


def eight():
    with open("output.txt", "r") as file:
        logs = file.readlines()

    app_types = ["FrontendApp", "BackendApp", "API"]
    activities = ["INFO", "DEBUG", "ERROR"]

    for app_type in app_types:
        counts = {activity: {} for activity in activities}

        for log in logs:
            parts = log.split(" - ")
            timestamp_str, log_app_type, activity = parts[0], parts[2].split()[0], parts[1][1:-1]

            if log_app_type == app_type:
                timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")
                if timestamp.hour not in counts[activity]:
                    counts[activity][timestamp.hour] = 1
                else:
                    counts[activity][timestamp.hour] += 1

        print(f"\n{app_type}:")
        for activity in activities:
            hour, count = find_max_hour(counts[activity])
            print(f"  Most {activity} activities occurred {count} times at hour {hour}")


def find_max_hour(counts):
    if not counts:
        return None, 0

    max_hour, max_count = max(counts.items(), key=lambda x: x[1])
    return max_hour, max_count


eight()
