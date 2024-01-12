from log import Log, LogStatus
from service import three, four, six
from collections import defaultdict
from task9 import failureRatePercentage, run
from task1 import one
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
sdict = seven('logTest')
print(sdict)
#print(run())
'''
for app_name in sdict:
        print(f"Max / min time for {app_name}: {sdict[app_name]['max_run_time']} and {sdict[app_name]['min_run_time']} occurring at {sdict[app_name]['max_timestamp']} and {sdict[app_name]['min_timestamp']}.")
'''