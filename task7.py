def seven (filename):

    app_run_time = {'BackendApp': {'max_run_time': 0, 'min_run_time' : 0, 'max_timestamp': 0, 'min_timestamp': 0},
                      'FrontendApp': {'max_run_time': 0, 'min_run_time' : 0, 'max_timestamp': 0, 'min_timestamp': 0},
                      'API': {'max_run_time': 0, 'min_run_time' : 0, 'max_timestamp': 0, 'min_timestamp': 0}
    }
    with open(filename, 'r') as file:
        for line in file:
            ok = 0
            if "[INFO]" in line and "ran successfully" in line and "SYSTEM" not in line:
                parts = line.split(" - ")
                timestamp, app, status, run_time = parts[0], parts[2].split()[0], "has ran successfully", int (parts[2].split()[5][:-2])
                if run_time > app_run_time[app]['max_run_time']:
                    app_run_time[app]['max_run_time'] = run_time
                    app_run_time[app]['max_timestamp'] = timestamp
                if run_time < app_run_time[app]['min_run_time'] or ok !=1:
                    app_run_time[app]['min_run_time'] = run_time
                    app_run_time[app]['min_timestamp'] = timestamp
                    ok = 1
    return app_run_time