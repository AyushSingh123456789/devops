import re

# search: find first match anywhere in string
re.search(r'ERROR', 'INFO: ok\nERROR: disk full')

# match: only checks from the start of the string
re.match(r'INFO', 'INFO: ok')

# findall: all matches as a list # ['1', '80', '2', '45']

re.findall(r'\d+', 'server1: 80% cpu, server2: 45% cpu')

# finditer: like findall but gives you match objects (with position info)
for m in re.finditer(r'\d+', 'cpu: 80 mem: 45'):
    print(m.group(), m.start())
 
# sub: replace 
re.sub(r'password=\s+', 'password=****', 'password=secret123 user=admin')

# split: split on a pattern
re.split(r'\s,\s*', 'us-east-1, us-west-2,eu-central-1')