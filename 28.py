poster=int(input())
guys=list(map(int,input().split()[:poster]))
for p in range(poster):
  print(guys[p],p)
