from collections import defaultdict
import re
from datetime import time
from enum import Enum
from itertools import chain
from datetime import datetime


class LogStatus(Enum):
    INFO = "INFO"
    DEBUG = "DEBUG"
    ERROR = "ERROR"


class Log:
    REGEX = r'^(?P<ts>([0-9]{2}:){2}[0-9]{2}) - \[(?P<status>[A-Z]+)\] - (?P<app>[^ ]+) .*'

    def __init__(self, app: str, status: LogStatus, timestamp: time):
        self.app = app
        self.status = status
        self.timestamp = timestamp

    @classmethod
    def from_string(cls, log_line: str):
        match = re.fullmatch(Log.REGEX, log_line)
        if not match:
            return None
        return cls(match["app"], match["status"], time.fromisoformat(match["ts"]))

    def __str__(self):

        return f'TS: {self.timestamp}; APP: {self.app}; STATUS: {self.status}'


def one(filename):
    log_count = defaultdict(int)
    with open(filename, 'r') as file:
        info_logs_count = defaultdict(int)

        for line in file:
            log_time, log_type, message = line.strip().split(' - ')
            app = message.split()[0]

            if log_type == '[INFO]':
                if info_logs_count[app] % 2 == 0:
                    log_count[(log_type, app)] += 1
                info_logs_count[app] += 1
            else:
                log_count[(log_type, app)] += 1

        print("1. INFO/DEBUG/ERROR logs per type of app:")
        for (log_type, app), count in log_count.items():
            print(f"{app} - {log_type}: {count} logs")

        return log_count

def calculate_average_run_time(total_run_time, successful_run_count):
    average_run_time_per_app = {}
    for app, count in successful_run_count.items():
        if count > 0:
            average_run_time_per_app[app] = total_run_time[app] / count
        else:
            average_run_time_per_app[app] = 0

    return average_run_time_per_app


def two(filename):
    total_run_time = {'BackendApp': 0, 'FrontendApp': 0, 'API': 0}
    successful_run_count = {'BackendApp': 0, 'FrontendApp': 0, 'API': 0}
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


def three(logs):
    return {k: len(list(filter(lambda l: l.status == LogStatus.ERROR.value, v))) for k, v in logs.items()}

def four(logs):
    return next(iter(sorted(three(logs).items(), key=lambda t: t[1], reverse=True)))

def app_status_pairs(logs):
    return {k: len(list(filter(lambda l: l.status == LogStatus.INFO.value, v))) for k, v in logs.items()}

def get_day_third_key(log):
    if log.timestamp < time.fromisoformat('08:00:00'):
        return 1
    if log.timestamp < time.fromisoformat('16:00:00'):
        return 2
    return 3

def five(log_dict):
    item_list = {app_status_pairs(log_dict)[key] for key in app_status_pairs(log_dict)}
    x = max(item_list)
    for item in app_status_pairs(log_dict):
        if (app_status_pairs(log_dict))[item] == x:
            max_app = item
    return

def six(log_dict):
    error_logs_for_each_app = [
        list(filter(lambda lg: lg.status == LogStatus.ERROR.value, v))
        for v in log_dict.values()
    ]
    all_error_logs = chain.from_iterable(error_logs_for_each_app)
    day_thirds_dict = {k: [] for k in range(1, 4)}
    for log in all_error_logs:
        day_thirds_dict[get_day_third_key(log)].append(log)
    return {k: len(v) for k, v in day_thirds_dict.items()}

def seven (filename):

    app_run_time = {'BackendApp': {'max_run_time': 0, 'min_run_time' : 0, 'max_timestamp': 0, 'min_timestamp': 0},
                      'FrontendApp': {'max_run_time': 0, 'min_run_time' : 0, 'max_timestamp': 0, 'min_timestamp': 0},
                      'API': {'max_run_time': 0, 'min_run_time' : 0, 'max_timestamp': 0, 'min_timestamp': 0}
    }
    with open(filename, 'r') as file:
        for line in file:
            ok = 0
            if "[INFO]" in line and "ran successfully" in line and "SYSTEM" not in line:
                parts = line.split(" - ")
                timestamp, app, status, run_time = parts[0], parts[2].split()[0], "has ran successfully", int (parts[2].split()[5][:-2])
                if run_time > app_run_time[app]['max_run_time']:
                    app_run_time[app]['max_run_time'] = run_time
                    app_run_time[app]['max_timestamp'] = timestamp
                if run_time < app_run_time[app]['min_run_time'] or ok !=1:
                    app_run_time[app]['min_run_time'] = run_time
                    app_run_time[app]['min_timestamp'] = timestamp
                    ok = 1
    return app_run_time

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


def failureRatePercentage(log_count, err_log_count, filename='output.txt'):
    with open(filename, 'r') as file:
        for line in file:
            log_time, log_type, message = line.strip().split(' - ')
            # print(log_type)
            app = message.split()[0]
            if log_type == "[ERROR]":
                err_log_count[app] += 1
            else:
                log_count[app] += 1


def nine():
    log_counts = defaultdict(int)
    err_log_count = defaultdict(int)
    failureRatePercentage(log_counts, err_log_count)

    # print("9. Failure rate percentage for each type of App: ")
    '''
    for app in set(chain(log_counts.keys(), err_log_count.keys())):
        final_dict = defaultdict(int)
        total_count = log_counts[app] + err_log_count[app]
        fail_percentage = (err_log_count[app] / total_count) * 100 if total_count > 0 else 0
        print(f"{app} - Fail percentage: {fail_percentage}%")
    '''
    result_dict = {}
    for app in set(chain(log_counts.keys(), err_log_count.keys())):
        total_count = log_counts[app] + err_log_count[app]
        fail_percentage = (err_log_count[app] / total_count) * 100 if total_count > 0 else 0
        result_dict[app] = fail_percentage
    return result_dict

