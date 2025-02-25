"""
The isalnum() method in Python is a built-in string function that checks if all characters in a string are alphanumeric (letters or numbers). 
It returns True if the string contains only alphanumeric characters and is not empty; otherwise, it returns False. 
Python

create a new string add all the characters to it and reverse it to check if palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for i in s :
            if i.isalnum():
                newString += i.lower()
        return newString == newString[::-1]