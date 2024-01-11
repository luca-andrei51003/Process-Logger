from collections import defaultdict


def count_logs_from_file(log_count, filename='output.txt'):
    with open(filename, 'r') as file:
        info_logs_count = defaultdict(int)

        for line in file:
            log_time, log_type, message = line.strip().split(' - ')
            app = message.split()[0]

            if log_type == 'INFO':
                if info_logs_count[app] % 2 == 0:
                    log_count[(log_type, app)] += 1
                info_logs_count[app] += 1
            else:
                log_count[(log_type, app)] += 1


if __name__ == "__main__":
    log_counts = defaultdict(int)
    count_logs_from_file(log_counts)
    print("1. INFO/DEBUG/ERROR logs per type of app:")
    for (log_type, app), count in log_counts.items():
        print(f"{app} - {log_type}: {count} logs")
