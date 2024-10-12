# Re.start() & Re.end()
import re
text = input()
pattern = input()
positions = [(m.start(), m.start() + len(pattern) - 1) for m in re.finditer(f'(?={re.escape(pattern)})', text)]
if positions:
    for pos in positions:
        print(pos)
else:
    print((-1, -1))
