# Validating UID
import re
for _ in range(int(input())):
    s = ''.join(sorted(input()))  # Changed variable name to 's'
    try:
        assert re.search(r'[A-Z]{2}', s)
        assert re.search(r'\d{3}', s)
        assert not re.search(r'[^a-zA-Z0-9]', s)
        assert not re.search(r'(.)\1', s)
        assert len(s) == 10
    except:
        print('Invalid')
    else:
        print('Valid')