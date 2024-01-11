from collections import defaultdict
from log import LogStatus
from itertools import chain

def failureRatePercentage(log_count, err_log_count, filename='output.txt'):
    with open(filename, 'r') as file:
        for line in file:
            log_time, log_type, message = line.strip().split(' - ')
            #print(log_type)
            app = message.split()[0]
            if log_type == "[ERROR]":
                err_log_count[app] += 1
            else:
                log_count[app] += 1

def run():
    log_counts = defaultdict(int)
    err_log_count = defaultdict(int)
    failureRatePercentage(log_counts, err_log_count)
    
    #print("9. Failure rate percentage for each type of App: ")
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