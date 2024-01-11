from datetime import time
from itertools import chain
from log import LogStatus


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