inStr = input('Enter string:')
arr = list(inStr)
out = []

for x in arr:
    if arr.count(x) == 1:
        out.append(x)

print(out)
