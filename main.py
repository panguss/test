n=int(input())
if n > 999999 or n < 1:
    print('Число не входит в заданный диапазон')
if ((n // 100000) % 10) == 1:
    print('сто ', end='')
if ((n // 100000) % 10) == 2:
    print('двести ', end='')
if ((n // 100000) % 10) == 3:
    print('триста ', end='')
if ((n // 100000) % 10) == 4:
    print('четыреста ', end='')
if ((n // 100000) % 10) == 5:
    print('пятьсот ', end='')
if ((n // 100000) % 10) == 6:
    print('шестьсот ', end='')
if ((n // 100000) % 10) == 7:
    print('семьсот ', end='')
if ((n // 100000) % 10) == 8:
    print('восемьсот ', end='')
if ((n // 100000) % 10) == 9:
    print('девятьсот ', end='')
if ((n // 10000) % 10 == 1):
    if (n // 1000 % 10) == 0:
        print('десять тысяч ', end='')
    if (n // 1000 % 10) == 1:
        print('одинадцать тысяч ', end='')
    if (n // 1000 % 10) == 2:
        print('двенадцать тысяч ', end='')
    if (n // 1000 % 10) == 3:
        print('тринадцать тысяч ', end='')
    if (n // 1000 % 10) == 4:
        print('четырнадцать тысяч ', end='')
    if (n // 1000 % 10) == 5:
        print('пятьнадцать тысяч ', end='')
    if (n // 1000 % 10) == 6:
        print('шестнадцать тысяч ', end='')
    if (n // 1000 % 10) == 7:
        print('семьнадцать тысяч ', end='')
    if (n // 1000 % 10) == 8:
        print('восемьнадцать тысяч ', end='')
    if (n // 1000 % 10) == 9:
        print('девятьнадцать тысяч ', end='')
if ((n//10000) % 10) == 2:
    print('двадцать ', end='')
if ((n//10000) % 10) == 3:
    print('тридцать ', end='')
if ((n//10000) % 10) == 4:
    print('сорок ', end='')
if ((n//10000) % 10) == 5:
    print('пятьдесят ', end='')
if ((n//10000) % 10) == 6:
    print('шестьдесят ', end='')
if ((n//10000) % 10) == 7:
    print('семьдесят ', end='')
if ((n//10000) % 10) == 8:
    print('восемьдесят ', end='')
if ((n//10000) % 10) == 9:
    print('девяноста ', end='')
if ((n//10000) % 10 != 1) and len(str(n)) >= 4:
    if (n//1000) % 10 == 0:
        print('тысяч ', end='')
    if (n//1000) % 10 == 1:
        print('одна тысяча ', end='')
    if (n//1000) % 10 == 2:
        print('две тысячи ', end='')
    if (n//1000) % 10 == 3:
        print('три тысячи ', end='')
    if (n//1000) % 10 == 4:
        print('четыре тысячи ', end='')
    if (n//1000) % 10 == 5:
        print('пять тысяч ', end='')
    if (n//1000) % 10 == 6:
        print('шесть тысяч ', end='')
    if (n//1000) % 10 == 7:
        print('семь тысяч ', end='')
    if (n//1000) % 10 == 8:
        print('восемь тысяч ', end='')
    if (n//1000) % 10 == 9:
        print('девять тысяч ', end='')
if (n//100) % 10 == 1:
    print('сто ', end='')
if (n//100) % 10 == 2:
    print('двести ', end='')
if (n//100) % 10 == 3:
    print('триста ', end='')
if (n//100) % 10 == 4:
    print('четыреста ', end='')
if (n//100) % 10 == 5:
    print('пятьсот ', end='')
if (n//100) % 10 == 6:
    print('шестьсот ', end='')
if (n//100) % 10 == 7:
    print('семьсот ', end='')
if (n//100) % 10 == 8:
    print('восемьсот ', end='')
if (n//100) % 10 == 9:
    print('девятьсот ', end='')
if ((n//10) % 10 == 1):
    if n % 10 == 0:
        print('десять рублей ', end='')
    if n % 10 == 1:
        print('одинадцать рублей ', end='')
    if n % 10 == 2:
        print('двенадцать рублей ', end='')
    if n % 10 == 3:
        print('тринадцать рублей ', end='')
    if n % 10 == 4:
        print('четырнадцать рублей ', end='')
    if n % 10 == 5:
        print('пятьнадцать рублей ', end='')
    if n % 10 == 6:
        print('шестнадцать рублей ', end='')
    if n % 10 == 7:
        print('семьнадцать рублей ', end='')
    if n % 10 == 8:
        print('восемьнадцать рублей ', end='')
    if n % 10 == 9:
        print('девятьнадцать рублей ', end='')
if (n//10) % 10 == 2:
    print('двадцать ', end='')
if (n//10) % 10 == 3:
    print('тридцать ', end='')
if (n//10) % 10 == 4:
    print('сорок ', end='')
if (n//10) % 10 == 5:
    print('пятьдесят ', end='')
if (n//10) % 10 == 6:
    print('шестдесят ', end='')
if (n//10) % 10 == 7:
    print('семьдесят ', end='')
if (n//10) % 10 == 8:
    print('восемьдесят ', end='')
if (n//10) % 10 == 9:
    print('девяносто ', end='')
if ((n//10) % 10) != 1:
    if n % 10 == 0:
        print('рублей', end='')
    if n % 10 == 1:
        print('один рубль', end='')
    if n % 10 == 2:
        print('два рубля', end='')
    if n % 10 == 3:
        print('три рубля', end='')
    if n % 10 == 4:
        print('четыре рубля', end='')
    if n % 10 == 5:
        print('пять рублей', end='')
    if n % 10 == 6:
        print('шесть рублей', end='')
    if n % 10 == 7:
        print('семь рублей', end='')
    if n % 10 == 8:
        print('восемь рублей', end='')
    if n % 10 == 9:
        print('девять рублей', end='')
