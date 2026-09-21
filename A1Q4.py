def forloop(s):
    s=s.lower()
    len_s = len(s)
    for i in range(len_s):
        if s[i] != s[len_s - 1 - i]:
            print("for-loop Check : Not a palindrome")
            return
    print("for-loop Check : Is a palindrome")

def two_pointer(s):
    s=s.lower()
    for i in range(len(s)):
        for j in range(len(s)):
            if s[j] != s[len(s) - 1 - i]:
                print("two-pointer Check : Not a palindrome")
                return
            else:
                print("two-pointer Check : Is a palindrome")
                return

string="madam"
forloop(string)
two_pointer(string)
