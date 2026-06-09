class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(oc, cc, s):
            if oc == n and cc == n:
                result.append(s)
                return

            if oc < n:
                helper(oc + 1, cc, s + "(")

            if cc < oc:
                helper(oc, cc + 1, s + ")")

        helper(0, 0, "")
        return result
        