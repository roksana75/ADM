# Re.findall() & Re.finditer()

import re

consonants =  '[^aeiou]'
a = re.findall("(?<=" + consonants + ")([aeiou]{2,})" + consonants, input(), re.I)
print('\n'.join(a or ['-1']))