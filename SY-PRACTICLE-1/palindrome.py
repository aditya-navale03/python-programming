def is_palindrome(s):
    return s == s[::-1]

input_string = "malayalam"
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")
