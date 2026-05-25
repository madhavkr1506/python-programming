class StringException(Exception):
    def __init__(self, message:str):
        super().__init__(message)

class LengthZeroException(StringException):
    pass

# def canReach(s:str, minJump:int, maxJump:int)->bool:
#     try:
#         n1 = len(s)
#         if n1 == 0: raise LengthZeroException(f"string of length zero")
#         dp = [-1]*n1
#         can_reached = False
#         curr = 0
#         if s[curr] == '0':
#             can_reached = helper(s=s, curr=curr, minJump=minJump, maxJump=maxJump, dp=dp)
#         if can_reached: return True
#         return False
#     except Exception as err:
#         if isinstance(err, LengthZeroException):
#             raise err
#         raise err
    
# def helper(s:str, curr:int, minJump:int, maxJump:int, dp:list[int]):
#     if curr >= len(s): 
#         return False
#     if s[curr] == '1':
#         return False
#     if curr == len(s) - 1:
#         return True
#     if dp[curr] != -1:
#         return dp[curr]
#     if curr == len(s) - 1 and s[curr] == '0':
#         dp[curr] = True
#         return True
#     range0 = curr + minJump
#     range1 = min(curr + maxJump, len(s)-1)
#     for next in range(range0, range1+1):
#         if next >= 0 and next < len(s):
#             if s[next] == '0':
#                 if helper(s=s, curr=next, minJump=minJump, maxJump=maxJump, dp=dp):
#                     dp[curr] = True
#                     return True
#     dp[curr] = False
#     return False

def canReach(s:str, minJump:int, maxJump:int)->bool:
    try:
        n1 = len(s)
        if n1 == 0: raise LengthZeroException(f"string of length zero")   
        dp = [False] * n1
        dp[0] = True

        reachable = 0

        for i in range(1, n1):
            if i - minJump >= 0 and dp[i - minJump]:
                reachable += 1
            if i - maxJump - 1 >=0 and dp[i - maxJump - 1]:
                reachable -= 1
            if s[i] == '0' and reachable > 0:
                dp[i] = True
        return dp[-1]   
    except Exception as err:
        if isinstance(err, LengthZeroException):
            raise err
        raise err

"""
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

 

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
 

Constraints:

2 <= s.length <= 105
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length
 
"""

def main():
    try:
        s:str="011010"
        minJump=2
        maxJump=3    
        can_reached = canReach(s=s, minJump=minJump, maxJump=maxJump)
        print(f"can reached: {can_reached}")
    except Exception as err:
        if isinstance(err, LengthZeroException):
            print(f"string length zero exception: {err}")
            return
        print(f"generic exception: {err}")

if __name__ == "__main__":
    main()