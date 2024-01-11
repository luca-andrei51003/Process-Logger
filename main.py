from log import Log, LogStatus
from service import three, four, six, nine
from collections import defaultdict


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
    log_dict = read_logs()
    
    for key in log_dict:
        if (log_dict[key]=="ERROR"):
            
    
    '''mlist = [LogStatus.INFO, LogStatus.ERROR, LogStatus.DEBUG]
    sep_log_dict = {'app_name':None}
    failure_rate = {'app_type': None, 'value': None}
    for x in mlist:
        for key in log_dict.items():
            if x not in sep_log_dict:
                sep_log_dict[x] = {}
            sep_log_dict[x][tuple(key)] = x
            failure_rate['app_type'] = x
            total = len(sep_log_dict[x])
            aux = nine(sep_log_dict[x])
            failure_rate['value'] = (aux/total) * 10'''
    print(failure_rate.items())
    print(three(log_dict))
    print(four(log_dict))
    print(six(log_dict))


main()