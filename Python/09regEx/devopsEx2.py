# Extracting IPs
# (Note: this matches IP-shaped strings, not strictly valid 0–255 ranges — fine for log scraping, not for validation.)

ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
re.findall(ip_pattern, log)  # ['192.168.1.45']



# The function re.findall(ip_pattern, log) executes the following procedure:

# Scanning: Python's re module scans through the string provided in the log variable from left to right.

# Matching: It looks for text sequences that strictly satisfy the structural rules defined by ip_pattern (three sets of 1–3 digits followed by dots, ending with a final set of 1–3 digits).

# Extraction: Every time it finds a matching sequence that meets the word-boundary criteria, it extracts it.

# Returning: It collects all non-overlapping matches into a Python list of strings and returns them. In your example, it successfully finds and returns ['192.168.1.45'].