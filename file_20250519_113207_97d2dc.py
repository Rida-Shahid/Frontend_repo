```python
def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]

def main():
    user_input = input("enter a string to check if it's a palindrome: ")
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is not a palindrome.")

if __name__ == "__main__":
    main()
