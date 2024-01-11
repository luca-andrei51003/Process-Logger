from datetime import datetime

with open("output.txt", "r") as file:
    logs = file.readlines()

frontend_counts = {"INFO": {}, "DEBUG": {}, "ERROR": {}}
backend_counts = {"INFO": {}, "DEBUG": {}, "ERROR": {}}
api_counts = {"INFO": {}, "DEBUG": {}, "ERROR": {}}

for log in logs:
    parts = log.split(" - ")
    timestamp_str, app_type, activity = parts[0], parts[2].split()[0], parts[1][1:-1]
    timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")

    if app_type == "FrontendApp":
        if timestamp.hour not in frontend_counts[activity]:
            frontend_counts[activity][timestamp.hour] = 1
        else:
            frontend_counts[activity][timestamp.hour] += 1
    elif app_type == "BackendApp":
        if timestamp.hour not in backend_counts[activity]:
            backend_counts[activity][timestamp.hour] = 1
        else:
            backend_counts[activity][timestamp.hour] += 1
    elif app_type == "API":
        if timestamp.hour not in api_counts[activity]:
            api_counts[activity][timestamp.hour] = 1
        else:
            api_counts[activity][timestamp.hour] += 1


def find_max_hour(counts):
    if not counts:
        return None, 0

    max_hour, max_count = max(counts.items(), key=lambda x: x[1])
    return max_hour, max_count

print("FrontendApp:")
hour, count = find_max_hour(frontend_counts["INFO"])
print(f"  Most INFO activities occurred {count} times at hour {hour}")
hour, count = find_max_hour(frontend_counts["DEBUG"])
print(f"  Most DEBUG activities occurred {count} times at hour {hour}")
hour, count = find_max_hour(frontend_counts["ERROR"])
print(f"  Most ERROR activities occurred {count} times at hour {hour}")

print("\nBackendApp:")
hour, count = find_max_hour(backend_counts["INFO"])
print(f"  Most INFO activities occurred {count} times at hour {hour}")
hour, count = find_max_hour(backend_counts["DEBUG"])
print(f"  Most DEBUG activities occurred {count} times at hour {hour}")
hour, count = find_max_hour(backend_counts["ERROR"])
print(f"  Most ERROR activities occurred {count} times at hour {hour}")

print("\nAPI:")
hour, count = find_max_hour(api_counts["INFO"])
print(f"  Most INFO activities occurred {count} times at hour {hour}")
hour, count = find_max_hour(api_counts["DEBUG"])
print(f"  Most DEBUG activities occurred {count} times at hour {hour}")
hour, count = find_max_hour(api_counts["ERROR"])
print(f"  Most ERROR activities occurred {count} times at hour {hour}")
