# Hex Color Code
import re
patrn = r'(?<!^)(#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6}))(?=[\s;,)])'
for _ in range(int(input())):
    l = input()
    matches = re.finditer(patrn, l)
    for match in matches:
        print(match.group(1))