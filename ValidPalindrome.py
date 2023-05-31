s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

def isPalindrome(s):
    t = ""

    for character in s:
        if character.isalnum():
            t += character.lower()

    left = 0
    right = len(t) - 1
    while left<right:
        if t[left] == t[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

x = isPalindrome(s3)

print(x)