class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique = dict()
        output = []

        for val in strs:
            sort = "".join(sorted(val))
            if sort in unique:
                unique[sort].append(val)
            else:
                unique[sort] = [val]
        
        for key in unique:
            output.append(unique[key])
        
        return output