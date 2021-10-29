'''Cho dãy số A[] gồm có N phần tử.
Một cặp nghịch thế là một cặp số (u, v) sao cho u < v và A[u] > A[v]. 
Nhiệm vụ của bạn là hãy đếm số lượng cặp nghịch thế trong dãy số A[] ban đầu.'''
n=int(input())
a=[int(x) for x in input().split()]
count=int(0)
for i in range(0, n-1):
    for j in range(i+1, n):
        if(a[i]>a[j]):
            count=count+1
print(count)
