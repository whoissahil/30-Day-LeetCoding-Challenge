'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    All inputs will be in lowercase.
    The order of your output does not matter.

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myList = []
        firstList = []
        for i in range(0,len(strs)):
            tmp = list(strs[i])
            tmp.sort()
            if tmp not in myList:
                myList.append(tmp)
                firstList.append([strs[i]])
            elif tmp in myList:
                firstList[myList.index(tmp)].append(strs[i])
        return(firstList)