# Group(), Groups() & Groupdict()

import re
seq = r'([a-zA-Z0-9])\1+'
match = re.search(seq, input().strip())
print(match.groups()[0] if match else -1)