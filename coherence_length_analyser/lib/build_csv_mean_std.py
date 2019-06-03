import csv
import numpy as np
import decimal
decimal.getcontext().rounding = decimal.ROUND_UP

def floating(string):
    try:
        return float(string)
    except ValueError:
        return string


path = r"C:\Users\Haarmeyer\OUT\coherence_length_analyser\lines.csv"

with open(path, "r") as file:
    reader = csv.reader(file)
    lst = list(reader)

lst = [[floating(x) for x in y] for y in lst]

for item in lst:
    if type(item[0]) is float:
        tmp = item[4:]
        mean = np.mean(tmp)
        std = np.std(tmp, ddof=1)
        mean = decimal.Decimal(str(mean)).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP)
        std = decimal.Decimal(str(std)).quantize(decimal.Decimal('.00001'), rounding=decimal.ROUND_HALF_UP)
        item.extend([mean,std])
#        print(item)
lst[0].extend(["Mittelwert","Standardabweichung"])
lst[1].extend(["[\\textmu m]","[\\textmu m]"])

path2 = r"C:\Users\Haarmeyer\OUT\coherence_length_analyser\lines2.csv"
with open(path2, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(lst)

#print(lst)