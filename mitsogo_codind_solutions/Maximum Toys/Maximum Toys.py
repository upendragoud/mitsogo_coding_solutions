from textwrap import wrap, fill

prices=[1,4,5,3,2,1,1,6]
PRICES = []
all = []
req = []
for i in range(len(prices)):
    PRICES.append(prices[i:])
# print(PRICES)
for i in PRICES:
    P = ""
    for j in i:
        P+=str(j)
    for k in range(1, len(P)+1):
        for a in (wrap(P, k)):
            all.append(int(a))
s = set(all)
for i in s:
    sum = 0
    if len(str(i)) > 1:
        for j in str(i):
            sum += int(j)
    if sum == 6:
        req.append(i)

sor = sorted(req, key=lambda x:len(str(x)), reverse=True)
print(sor[0])