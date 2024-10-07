import math
h,w,n,m = map(int,input().split())

res = math.ceil(h/(n+1)) * math.ceil(w/(m+1))
print(res)