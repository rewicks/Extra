
MAX = 122
MIN = 97

n = int(input("What is your n? "))

l = []
for x in range(0, n):
    l.append(MAX)


def p(num_list):
    temp = ""
    for n in num_list:
        temp += chr(n)
    return temp

n-=1
i = n
while (i > 0):
  for j in range(MAX, MIN-1, -1):
    l[i] = j
    print(p(l))
    #print(l)
  count = 0
  for j in range(i-1, -1, -1):
    if l[j] != MIN:
      l[j]-=1
      for k in range(j+1, n+1):
        l[k] = MAX
      break
    else:
      count += 1
  i = n-count
