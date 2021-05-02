# DP背包问题

$X=\{xi\}$ xi= 0 or 1
$V=\{vi\}$ value
$W=\{wi\}$ weight
$\Sigma wx <= MAX$
$max\Sigma vx$
```python
def DP(w,p,m,x):
    v = 0
    Load = [[0 for col in range(m+1)]for raw in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            Load[i][j] = Load[i-1][j]
            if (j>=w[i])and(Load[i-1][j-w[i]]+p[i]>Load[i-1][j]):
                Load[i][j]=Load[i-1][j-w[i]]+p[i]
    j = m
    for i in range(n,0,-1):
        if Load[i][j]>Load[i-1][j]:
            x[i] = 'load'
            j =j-w[i]
    v = Load[n][m]
```
