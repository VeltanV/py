def isPalindrome(aString):
    oldString = aString.lower()
    newString = ""

    for x in oldString:
        newString = x + newString
    return newString == oldString


print(isPalindrome("StaTs"))
