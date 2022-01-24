'''
3. Feladat
Készíts egy programot, amely a felhasználó által megadott egész számról eldönti, hogy
- csak 3-mal osztható,
- csak 4-gyel osztható,
- 3-mal és 4-gyel is osztható,
- sem 3-mal, sem 4-gyel nem osztható!
'''

beker = int(input('Adj meg egy számot: \t'))
if beker %3 == 0:
    print(f'A szám {beker}: 3-al osztható.')
if beker %4 == 0:
    print(f'A szám {beker}: 4-el osztható.')
if beker %3 == 0 and beker %4 == 0:
    print(f'A szám {beker}: 3-al, és 4-el is osztható.')
if beker %3 != 0 and beker %4 != 0:
    print(f'A szám {beker}: sem 3-al, sem 4-el nem osztható.')