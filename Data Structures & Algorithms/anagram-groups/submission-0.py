class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique = {}
        output = []

        for i in range(len(strs)):
            sort = "".join(sorted(strs[i]))
            if sort in unique:
                unique[sort].append(strs[i])
            else:
                unique[sort] = [strs[i]]

        for key in unique:
            output.append(unique[key])

        return output
                