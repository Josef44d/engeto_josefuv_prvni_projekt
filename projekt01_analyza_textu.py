TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
oddelovac = '=' * 40

# pro uživatele
uzivatel = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123',
}
print(oddelovac)

# zadání uživetele s podmínkami
jmeno = input('username : ')
heslo = input('password : ')
print(oddelovac)
if uzivatel.get(jmeno) == heslo:
    print('Welcome to the app ' + str(jmeno) + '.')
else:
    print('Neplatné přihlašovací údaje.Ukončuji program.')
    quit()

# uživatel má možnost výběru ze 3 textů
print('We have', len(TEXTS), 'texts to be analyzed.')
print(oddelovac)

# zadání čísla textu s podmínkami
number = input(f'Enter a number btw.1 and {len(TEXTS)} to select: ')
if not number.isnumeric:
    print('The input is not number')
    quit()
elif int(number) > len(TEXTS) or int(number) < 1:
    print('Invalid number')
    quit()
print(oddelovac)

# index, rozdělení a očištění textu
number_index = int(number) - 1

cista_slova = []
for slovo in TEXTS[int(number_index)].split():
    cista_slova.append(slovo.strip(",.''()'\n"))

# počet slov v textu
word_count = len(cista_slova)
print(f'There are {word_count} words in the selected text.')

# počet slov začínající velkým písmenem
prvni_velke = []
for slovo in cista_slova:
    if slovo.istitle() == True:
        prvni_velke.append(slovo)
print(f'There are {len(prvni_velke)} titlecase words.')

# počet slov s velkými písmeny
velka_pismena = []
for slovo in cista_slova:
    if slovo.isupper() and slovo.isalpha() == True:
        velka_pismena.append(slovo)
print(f'There are {len(velka_pismena)} uppercase words.')

# počet slov s malými písmeny
mala_pismena = []
for slovo in cista_slova:
    if slovo.islower() and slovo.isalpha() == True:
        mala_pismena.append(slovo)
print(f'There are {len(mala_pismena)} lowercase words.')

# počet čísel v textu
cisla = []
for slovo in cista_slova:
    if int(slovo.isnumeric()) == True:
        cisla.append(int(slovo))
print(f'There are {len(cisla)} numeric strings.')

# součet čísel
print(f'The sum of all the numbers {sum(cisla)}.')
print(oddelovac)

# výstup se sloupcovým grafem
print('LEN' + '|' + '    OCCURENCES     ' + '|' + 'NR.')
print(oddelovac)
delka_slov = []
for s in cista_slova:
    delka_slov.append(int(len(s)));
    delka_slov.sort()

pocet_slov = {}
for s in delka_slov:
    pocet_slov[s] = pocet_slov.get(s, 0) + 1

for s in pocet_slov:
    nasobek = pocet_slov[s] * '*'
    print(f"{str(s).ljust(2)} | {str(nasobek).ljust(17)} | {pocet_slov[s]}")
