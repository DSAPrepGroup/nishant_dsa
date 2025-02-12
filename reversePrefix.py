class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        for index, letter in enumerate(word):
            if letter == ch:
                return word[index::-1] + word[index+1::]
        return word