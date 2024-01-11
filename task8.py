from datetime import datetime

def eight(filename):
    with open(filename, "r") as file:
        logs = file.readlines()

    app_types = ["FrontendApp", "BackendApp", "API"]
    activities = ["INFO", "DEBUG", "ERROR"]

    result_dict = {}

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

        app_results = {}
        for activity in activities:
            hour, count = find_max_hour(counts[activity])
            app_results[activity] = {'hour': hour, 'count': count}

        result_dict[app_type] = app_results

    return result_dict

def find_max_hour(counts):
    if not counts:
        return None, 0

    max_hour, max_count = max(counts.items(), key=lambda x: x[1])
    return max_hour, max_count

#result = eight("output.txt")
#print(result)
