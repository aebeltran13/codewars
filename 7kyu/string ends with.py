# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(text, ending):
    # your code here...
    text_len = len(text)
    ending_len = len(ending)

    text_end = text[text_len - ending_len : ]

    return True if text_end == ending else False