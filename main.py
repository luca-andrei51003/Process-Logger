from log import Log, LogStatus
from service import three, four, six
from collections import defaultdict
from task9 import failureRatePercentage, run
from task1 import count_logs_from_file, one

def read_logs():
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        logs = [Log.from_string(line) for line in lines]
    logs = [log for log in logs if log]
    app_names = set(log.app for log in logs)
    log_dict = {app_name: [] for app_name in app_names}
    for log in logs:
        log_dict[log.app].append(log)
    return log_dict


def main():
    '''
    log_dict = read_logs()
    #print(failure_rate.items())
    print(three(log_dict))
    print(four(log_dict))
    print(six(log_dict))
    print(failureRatePercentage(log_dict))
    '''
    run()
    one()

main()