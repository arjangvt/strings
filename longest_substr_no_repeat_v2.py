"""
This function returns the longest substr with no repeat.
It does the task using a data dictionary for tracking the indexes

written by: Arjang Fahim
Last update: 2/11/2021

"""

def longest_substr_no_repeat(s):

    if len(s) == 1:
        return 1

    idx_holder = {}
    idx = 0
    max_str = ""
    max_len = 0

    while idx < len(s):
        if s[idx] in max_str:
            if max_len < len(max_str):
                max_len = len(max_str)
            idx = idx_holder[s[idx]] + 1
            max_str = ""

        else:
            max_str = max_str + s[idx]
            if max_len < len(max_str):
                max_len = len(max_str)
            idx_holder[s[idx]] = idx
            idx = idx + 1


    return max_len


s = "aabbccddeeffgghhiijjkk"
#s = "p"
print(longest_substr_no_repeat(s))