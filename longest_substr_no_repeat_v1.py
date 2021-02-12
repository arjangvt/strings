"""
This function recursively returns the longest substr with no repeat recursively.
Note: This version of the program does not work with very large string due to maxumum
recursive depth limitation!

written by: Arjang Fahim
Last update: 1/29/2021

"""

def longest_substr_no_repeat(s, s_idx, n_idx, max_len, temp_str, index_holder):

    if len(s) == 1:
        return 1

    if n_idx >= len(s):
        return max_len

    if s[n_idx] in temp_str:
        # find the index
        new_idx = index_holder[s[n_idx]]
        if max_len <= len(temp_str):
            max_len = len(temp_str)
        max_len = longest_substr_no_repeat(s, s_idx+1, new_idx + 1, max_len, "", index_holder)
    else:
        temp_str = temp_str + s[n_idx]

        index_holder[s[n_idx]] = n_idx

        if len(temp_str) > max_len:
            max_len = len(temp_str)
        max_len = longest_substr_no_repeat(s, s_idx, n_idx + 1, max_len, temp_str, index_holder)

    return max_len


s = "bcdefaast"
#s = "p"
print(longest_substr_no_repeat(s, 0, 0, 0, "", {}))
