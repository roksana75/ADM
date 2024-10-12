# Validating and Parsing Email Addresses
import re
patrn = r'^<([a-zA-Z][\w\.-]+)@([a-zA-Z]+)\.([a-zA-Z]{1,3})>$'
for _ in range(int(input())):
    name, email = input().split(' ')
    if re.match(patrn, email):
        print(f"{name} {email}")
