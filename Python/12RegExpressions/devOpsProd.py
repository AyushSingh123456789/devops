# A realistic combined example: scan a log file for errors and pull out structured data.

pattern = re.compile(
    r'^(?P<date>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '
    r'(?P<level>ERROR|WARN) \[(?P<service>[\w-]+)\] (?P<msg>.+)$',
    re.MULTILINE
)

with open('app.log') as f:
    content = f.read()

for m in pattern.finditer(content):
    print(f"{m['date']} | {m['service']} | {m['msg']}")
    
    
    
# Want me to give you a small set of practice exercises (e.g. parsing nginx access logs, extracting resource limits from a YAML/Docker config, masking secrets in output)? That's usually the fastest way to get this to stick