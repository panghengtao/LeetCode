class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        src = []
        candidates.sort()
        self.dsf(target, 0, candidates, len(candidates), [], src)
        print(src)

    def dsf(self, target, index, candidates, length,  path, src):
        if target < 0 or index > length:
            return
        elif target == 0:
            src.append(path)
        else:
            for i in range(index, len(candidates)):
                self.dsf(target - candidates[i], i + 1, candidates, length, path+[candidates[i]], src)

s = Solution()
s.combinationSum2([10,1,2,7,6,1,5], 8)

a = set([1, 1])
print(a)
# a.add(set([1, 1]))
print(a)