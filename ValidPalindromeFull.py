s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

def isPalindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not alphaNum(s[left]):
            left += 1
        while right > left and not alphaNum(s[right]):
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1
    return True
def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


print(isPalindrome(s3))