class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p1=len(s)   #3
        p2=len(t)   #6
        i,j=0,0
        count=0
        while i<p1 and j<p2:  
            if s[i] == t[j]: #
                count+=1
                j+=1
                i+=1
            else:
                j+=1

        if count == p1:
            return True
        else:
            return False
        return count