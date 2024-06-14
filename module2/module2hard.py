import sys

string_n = input()

try:
    n = int(string_n)
except ValueError as verr:
    print("Ошибка ввода")
    sys.exit(1)
except Exception as ex:
    print("Введено не целое число")
    sys.exit(1)

if n < 3 or n > 20:
    print("Число должно быть между 3 и 20 ")
    sys.exit(1)


def syfer(n_: int) -> str:
    pairs = []

    for i in range(1, n_):
        for j in range(i + 1, n_):
            if n_ % (i + j) == 0:
                pairs.append(i)
                pairs.append(j)
    return "".join([str(element) for element in pairs])


assert (syfer(3) == "12")
assert (syfer(4) == "13")
assert (syfer(5) == "1423")
assert (syfer(6) == "121524")
assert (syfer(7) == "162534")
assert (syfer(8) == "13172635")
assert (syfer(9) == "1218273645")
assert (syfer(10) == "141923283746")
assert (syfer(11) == "11029384756")
assert (syfer(12) == "12131511124210394857")
assert (syfer(13) == "112211310495867")
assert (syfer(14) == "1611325212343114105968")
assert (syfer(15) == "1214114232133124115106978")
assert (syfer(16) == "1317115262143531341251161079")
assert (syfer(17) == "11621531441351261171089")
assert (syfer(18) == "12151811724272163631545414513612711810")
assert (syfer(19) == "118217316415514613712811910")
assert (syfer(20) == "13141911923282183731746416515614713812911")

print(syfer(n))
