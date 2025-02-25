class Solution:

"""
constraints - are words case sensitive
is array sorted
can the words have spaces

intiution : use a hash map where key will be sorted order of string element 
and values will be list of words with same letters that occur in  the input list.
return the values from the map in form of list.
"""

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map ={}
        for s in strs:
            array = list(s)
            array.sort()
            sorted_s = "".join(array)
            if sorted_s not in map:
                map[sorted_s] = []
            map[sorted_s].append(s)
        return list(map.values())