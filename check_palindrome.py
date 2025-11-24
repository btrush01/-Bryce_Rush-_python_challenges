def reverse_string(string):
    return string[::-1]

test_1 = "Hello World"
print(reverse_string(test_1))


def is_palindrome(string):
    cleaned_string = string.strip().lower()
    if cleaned_string == reverse_string(cleaned_string):
        return True
    
test_2 = "1Rac e car1"
print(is_palindrome(test_2))