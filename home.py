def count(n):
   gg = [1,1]
   for i in range(n - 2):
    c = gg[-1] + gg[-2]
    gg.append(c)
   return gg[-1]
print(count(8))