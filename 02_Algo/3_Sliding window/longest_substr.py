# medium 

def longest_substr_without_replacement(words):
    substr = ''
    left = 0
    max_len = 0
    
    for right in range(len(words)):
        while words[right] in substr:
            substr = substr[1:]
            left +=1

        substr += words[right]

        max_len = max(max_len, len(substr))

    return max_len