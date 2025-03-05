"""
Generate All Subsequences of a String

Write a recursive function to generate all subsequences (power set) of a given string.

Example:

Input: "abc"

Output: ["", "a", "b", "c", "ab", "ac", "bc", "abc"]
"""

def generate_subsequence(string):
    if not string:
        return [""]
    
    smaller_subsequence = generate_subsequence(string[1:])
    result = []

    result.extend(smaller_subsequence)
    result.extend([string[0] + sub for sub in smaller_subsequence])
    print(result)
    return result

generate_subsequence('abc')