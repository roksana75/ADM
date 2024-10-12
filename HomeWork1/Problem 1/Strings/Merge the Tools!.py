# Merge the Tools!
from collections import OrderedDict
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        unique_chars = "".join(OrderedDict.fromkeys(substring))
        print(unique_chars)