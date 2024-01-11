from collections import defaultdict

total_run_time = {'BackendApp': 0, 'FrontendApp': 0, 'API': 0}
successful_run_count = {'BackendApp': 0, 'FrontendApp': 0, 'API': 0}


def calculate_average_run_time(total_run_time, successful_run_count):
    average_run_time_per_app = {}

    for app, count in successful_run_count.items():
        if count > 0:
            average_run_time_per_app[app] = total_run_time[app] / count
        else:
            average_run_time_per_app[app] = 0

    return average_run_time_per_app


def two(filename, total_run_time, successful_run_count):
    with open(filename, 'r') as file:
        for line in file:
            if "[INFO]" in line and "ran successfully" in line and "SYSTEM" not in line:
                parts = line.split(" - ")
                timestamp, app, status, run_time = parts[0], parts[2].split()[0], "has ran successfully", int(
                    parts[2].split()[5][:-2])

                total_run_time[app] += run_time
                successful_run_count[app] += 1

    average_run_time_per_app = calculate_average_run_time(total_run_time, successful_run_count)

    for app, average_run_time in average_run_time_per_app.items():
        print(f'Average successful runtime for {app}: {average_run_time}ms')

    return  average_run_time_per_app

#two("logTest", total_run_time, successful_run_count)
