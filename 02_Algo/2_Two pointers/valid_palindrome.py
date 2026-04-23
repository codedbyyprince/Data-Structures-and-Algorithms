# easy 

# valid palindrome
def valid_palindrome(s):
    clean_text = "".join(char for char in s if char.isalnum()).lower()
    start = 0 
    end = len(clean_text) - 1   # fixed
    
    while start < end:
        if clean_text[start] == clean_text[end]:
            start += 1
            end -= 1           # fixed
        else:
            return False
    return True 

s1 = "Hello! World @2024 #Python_is_Cool."
print(valid_palindrome(s1))
s2 = 'A man, a plan, a canal: Panama'
print(valid_palindrome(s2))