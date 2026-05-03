import os

HOSTS = ['8.8.8.8', '1.1.1.1', '8.8.4.4']
LOG_FILE = 'results.txt'

for host in HOSTS:
    code = os.system('ping -n 1 ' + host + ' > nul 2>&1')
    status = 'UP' if code == 0 else 'DOWN'
    entry = host + ': ' + status
    print(entry)
    with open(LOG_FILE, 'a') as f:
        f.write(entry + '\n')