# Validating things (env vars, versions, resource names)
# Use re.fullmatch (not search) for validation — it forces the entire string to match, not just part of it.

# semantic version
re.fullmatch(r'\d+\.\d+\.\d+', '1.4.2')  # matches

# valid k8s-style resource name (lowercase alphanumeric + hyphens)
re.fullmatch(r'[a-z0-9]([-a-z0-9]*[a-z0-9])?', 'my-service-01')