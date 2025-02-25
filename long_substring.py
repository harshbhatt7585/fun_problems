"""
2. **Longest Substring Without Repeating Characters**

Given a string, find the length of the longest substring that does not contain any repeating characters.

**Example:**

Input: "abcabcbb"

Output: 3 (Longest substring: "abc")
"""

## solves in O(N) where N is the length of the string
def get_longest_substring(string: str):
    count = {}
    sub_str = ""
    for s in string:
        if count.get(s, False):
            break
        count[s] = 1
        sub_str += s
    
    return sub_str


if __name__ == "__main__":
    sub_str = get_longest_substring("abcabcbb")
    print(sub_str)

            