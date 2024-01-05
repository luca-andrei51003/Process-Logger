import random
import datetime

def random_log_time():
    start_date = datetime.datetime(2020, 1, 1)
    end_date = datetime.datetime.now()
    random_date = start_date + datetime.timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )
    return random_date.strftime("%Y-%m-%d %H:%M:%S")


def random_log_type():
    return random.choice(['INFO', 'DEBUG', 'ERROR'])

def random_app():
    return random.choice(['BackendApp', 'FrontendApp', 'API', 'SYSTEM'])

def random_ms():
    return round(random.uniform(10, 30))

def random_success_log_message_running(app):
    return '{} has started running... \n'.format(app)

def random_success_log_message_ms(app, ms):
    return '{} has ran successfully in {}ms'.format(app, ms)

def random_fail_log_message():
    return '{} has failed after {}ms. Retrying... '.format(random_app(), random_ms())

def random_debug_log_message():
    return '{} is still running, please wait... '.format(random_app())
maxRuntime = 0
minRuntime = 31
maxrTimestamp = None
minrTimestamp = None
f = open(r'output.txt', 'a')
for x in range(10000):
    log_type = random_log_type()
    if (log_type == 'ERROR'):
        to_write = "{} - [{}] - {}\n".format(random_log_time(), log_type, random_fail_log_message())
        f.write(to_write)
    elif (log_type == 'DEBUG'):
        to_write = "{} - [{}] - {}\n".format(random_log_time(), log_type, random_debug_log_message())
        f.write(to_write)
    else:
        log_time = random_log_time()
        app = random_app()
        to_write_running = "{} - [{}] - {}".format(log_time, log_type, random_success_log_message_running(app))
        runtime = random_ms()
        
        to_write_finish = "{} - [{}] - {}\n".format(log_time, log_type, random_success_log_message_ms(app, runtime))
        f.write(to_write_running)
        f.write(to_write_finish)
        if (runtime > maxRuntime):
            maxRuntime = runtime
            maxrTimestamp = log_time
        elif (runtime < minRuntime):
            minRuntime = runtime
            minrTimestamp = log_time
        else:
            pass
print (minRuntime, maxRuntime, maxrTimestamp, minrTimestamp)