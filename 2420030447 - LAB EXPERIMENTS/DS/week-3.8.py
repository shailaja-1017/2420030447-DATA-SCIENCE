def lcs_length(X,Y):
    m,n=len(X),len(Y)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if X[i]==Y[j]:
                dp[i+1][j+1]=dp[i][j]+1
            else:
                dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
    return dp[m][n]
sequence1 = "ACDEF"
sequence2 = "AEBDF"  
length=lcs_length(sequence1, sequence2)
print(f"The length of the longest common subsequence between '{sequence1}' and '{sequence2}' is: {length}")