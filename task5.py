from collections import defaultdict
from log import LogStatus
from service import app_status_pairs

def five(log_dict):
    item_list = {app_status_pairs(log_dict)[key] for key in app_status_pairs(log_dict)}
    x = max(item_list)
    for item in app_status_pairs(log_dict):
        if (app_status_pairs(log_dict))[item] == x:
            max_app = item
    print(max(item_list), max_app)