# Parsing a Log File

log = '2026-07-23 14:32:10 ERROR [auth-service] Failed login for user admin from 192.168.1.45'

pattern = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+) \[(?P<service>[\w-]+)\] (?P<message>.+)'

m = re.match(pattern, log)
if m:
    print(m.group('level'))    # ERROR
    print(m.group('service'))  # auth-service
    print(m.group('message'))  # Failed login for user admin from 192.168.1.45