def seven (filename):

    max_run_time = {'BackendApp': {'run_time': 0, 'timestamp': 0},
                      'FrontendApp': {'run_time': 0, 'timestamp': 0},
                      'API': {'run_time': 0, 'timestamp': 0}
    }
    min_run_time = {'BackendApp': {'run_time': 0, 'timestamp': 0},
                      'FrontendApp': {'run_time': 0, 'timestamp': 0},
                      'API': {'run_time': 0, 'timestamp': 0}
    }
    with open(filename, 'r') as file:
        for line in file:
            if "[INFO]" in line and "ran successfully" in line and "SYSTEM" not in line:
                parts = line.split(" - ")
                timestamp, app, status, run_time = parts[0], parts[2].split()[0], "has ran successfully", int (parts[2].split()[5][:-2])
                
                #total_run_time[app] += run_time
                if run_time > max_run_time[app]['run_time']:
                    max_run_time[app]['run_time'] = run_time
                    max_run_time[app]['timestamp'] = timestamp
                if run_time < min_run_time[app]['run_time']:
                    min_run_time[app]['run_time'] = run_time
                    min_run_time[app]['timestamp'] = timestamp
    return max_run_time, min_run_time
    