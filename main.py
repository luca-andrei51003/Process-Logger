from log import Log, LogStatus
from service import three, four, six
from collections import defaultdict
from task9 import failureRatePercentage, run
from task1 import one
from task2 import two
from task5 import five
from task7 import seven

def read_logs(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        logs = [Log.from_string(line) for line in lines]
    logs = [log for log in logs if log]
    app_names = set(log.app for log in logs)
    log_dict = {app_name: [] for app_name in app_names}
    for log in logs:
        log_dict[log.app].append(log)
    return log_dict

log_dict = read_logs('input.txt')
#Run task 1:
#one('input.txt')
#Run task 2:
#print(two('input.txt'))
#Run task 3:
#print(three(log_dict))

#To run task 7, run following loop:
'''
for app_name in sdict:
        print(f"Max / min time for {app_name}: {sdict[app_name]['max_run_time']} and {sdict[app_name]['min_run_time']} occurring at {sdict[app_name]['max_timestamp']} and {sdict[app_name]['min_timestamp']}.")
'''