# Filtering CI/Build Output

lines = open('build.log').read().splitlines()
errors = [l for l in lines if re.search(r'\b(ERROR|FAILED|Exception)\b', l)]