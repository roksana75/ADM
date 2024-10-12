# Find a string
def count_substring(string, sub_string):
    count = 0
    substring_length = len(sub_string)
    for i in range(len(string) - substring_length + 1):
        if string[i:i + substring_length] == sub_string:
            count += 1
            
    return count