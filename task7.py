def seven(log_dict):
    for list_at_hand in log_dict.values():
        parts = list_at_hand.split(' - ')
        app_type = parts[2].split()[0]
        print [app_type]