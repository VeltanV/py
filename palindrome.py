def isPalindrome(aString):
    oldString = aString.lower()
    newString = ""

    for x in oldString:
        newString = x + newString
    if newString == oldString:
        return True
    else:
        return False


print(isPalindrome("StaTs"))
