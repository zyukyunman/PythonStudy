# -*- coding: utf-8 -*-


def Triangles():
    L = [1]
    while True:
        yield(L)
        L.append(0)
        L = [L[n] + L[n - 1] for n in range(len(L))]

m = 10
n = 0
for l in Triangles():
    print(l)
    n = n + 1
    if n == m:
        break
