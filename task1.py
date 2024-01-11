from collections import defaultdict
from log import LogStatus
from itertools import chain

# cu log.py
def task1(logs):
    info_logs_count = defaultdict(int)
    log_count = defaultdict(int)

    for key, log_list in logs.items():
        for log in log_list:
            if log.status == LogStatus.INFO.value:
                if info_logs_count[key] % 2 != 0:
                    log_count[(log.status, key)] += 1
                info_logs_count[key] += 1
            else:
                log_count[(log.status, key)] += 1

    print("1. INFO/DEBUG/ERROR logs per type of app:")
    for (log_type, app), count in log_count.items():
        print(f"{app} - {log_type}: {count} logs")


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