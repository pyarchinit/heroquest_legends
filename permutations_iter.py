#script from https://stackoverflow.com/questions/34970848/find-all-combination-that-sum-to-n-with-multiple-lists/34971783#34971783

# n = 5
# import itertools, operator
# for cuts in itertools.combinations_with_replacement(range(n+1),1):
#     combi = list(map(operator.sub, cuts + (n,), (0,) + cuts))
#     if max(combi) <= n:
#         print(combi)

#a script by AxelTheRabbit @kembridg from Telegram @pythonita
class Permutation_class:
    N = 0
    res = []
    def __init__(self,n):
        self.N = n
    def rec(self,l):
        s=sum(l)
        if s==self.N:
            self.res.append(l)
            return
        elif s>self.N:
            return
        for x in range(1,self.N+1):
            self.rec(l+[x])

#ac = Permutation_class(10)
#ac.rec([])
#print(Permutation_class.res)