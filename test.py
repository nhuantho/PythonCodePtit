def minTimeForWritingChars(N, insert, remov, cpy):
    if N == 0:
        return 0
    if N == 1:
        return insert
    dp = [0] * (N + 1)
    dp[1] = insert
    for i in range(2, N + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i - 1] + insert, dp[i // 2] + cpy)
        else:
            dp[i] = min(dp[i - 1] + insert, dp[(i + 1) // 2] + cpy + remov)
    return dp[N]
 
# Driver Code
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        N=int(input())
        insert, remov, cpy=map(int, input().split())
        print(minTimeForWritingChars(N, insert, remov, cpy))