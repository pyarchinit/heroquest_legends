#script from https://stackoverflow.com/questions/34970848/find-all-combination-that-sum-to-n-with-multiple-lists/34971783#34971783

n = 10
import itertools, operator
for cuts in itertools.combinations_with_replacement(range(n+1),1):
    combi = list(map(operator.sub, cuts + (n,), (0,) + cuts))
    if max(combi) <= n:
        print(combi)

#a script by AxelTheRabbit @kembridg from Telegram @pythonita
res = []
def rec(l):
     s=sum(l)
     if s==N:
          res.append(l)
          return
     elif s>N:
           return
     for x in range(1,N):
           rec(l+[x])

rec([])
print(res)