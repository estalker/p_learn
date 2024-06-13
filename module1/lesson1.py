flowerbed = [0,0]
n = 3

str_ = ''.join(str(x) for x in flowerbed)

if n == 0:
    print(True)

if len(str_) < 3 and str_.count("1") < 1 and n < 2:
    print(True)


if str_.startswith("00"):
    str_ = str_.replace("00","10",1)
    n = n - 1
    if str_.endswith("00"):
        str_ = "01".join(str_.rsplit("00", 1))
        n = n - 1



if n <= 0:
    print(True)

for i,x in enumerate(reversed(range(1, n+1))):
    if x <= str_.count('000'):
        print(True)
    else:
        str_ = str_.replace("000","010",1)
print(False)







