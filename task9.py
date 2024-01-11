'''
from collections import defaultdict
from log import LogStatus
from itertools import chain
def failureRatePercentage(log_count, err_log_count, filename = 'output.txt'):
    with open (filename, 'r') as file:
        err_log_count = defaultdict(int)
        for line in file:
            log_time, log_type, message = line.strip().split(' - ')
            app = message.split()[0]
            if log_type == "ERROR":
                err_log_count[app] += 1
            else:
                log_count[(log_type, app)] += 1

def run():
    log_counts = defaultdict(int)
    err_log_count = defaultdict(int)
    failureRatePercentage(log_counts, err_log_count)
    print("1. Failure rate percentage for each type of App: ")
    for app, count in log_counts.items():
        print(f"{app} - Fail percentage: {err_log_count[app]/count * 100}%")
'''
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
    
    print("9. Failure rate percentage for each type of App: ")
    
    for app in set(chain(log_counts.keys(), err_log_count.keys())):
        total_count = log_counts[app] + err_log_count[app]
        fail_percentage = (err_log_count[app] / total_count) * 100 if total_count > 0 else 0
        print(f"{app} - Fail percentage: {fail_percentage}%")
