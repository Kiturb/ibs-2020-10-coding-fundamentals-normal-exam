with open('results.txt') as f:
    lines = f.read().splitlines()

lines.pop(0)

fr = []
sw = []
ge = []
year = []

for x in lines:
    details = x.split()
    fr.append(int(details[0]))
    sw.append(int(details[1]))
    ge.append(int(details[2]))
    year.append(int(details[3]))

minFrance = fr.index(min(fr))
maxFrance = fr.index(max(fr))

minSweden = sw.index(min(sw))
maxSweden = sw.index(max(sw))

minGermany = ge.index(min(ge))
maxGermany = ge.index(max(ge))

print(print("{} {} {}".format('France =>', year[minFrance], year[maxFrance])))
print(print("{} {} {}".format('Sweden =>', year[minSweden], year[maxSweden])))
print(print("{} {} {}".format('Germany =>', year[minGermany], year[maxGermany])))
