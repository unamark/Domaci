from functools import reduce
from time import time


# 17.
def vreme_izvrsavanja(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Trebalo je {t2-t1}s da se izvrsi.')
        return result
    return wrapper


# 1.
lista = ['flower', 'flow', 'flight', 'fabulous']
z1 = reduce(lambda a, b: a if len(a) > len(b) else b, lista)
# print(z1)

# 2.
imena = ['Ana', 'Jovan', 'Milica', 'Milos', 'Sara', 'Kris']
ocene = [7.64, 8, 8.5, 9, 8.3, 8.6]
z2 = list(filter(lambda x: x[1] > 8.5, zip(imena, ocene)))
# print(z2)

# 3.
studenti = [{'ime': 'Ana', 'godine': 22, 'prosek': 9.1},
            {'ime': 'Jovan', 'godine': 20, 'prosek': 8.5},
            {'ime': 'Kio', 'godine': 25, 'prosek': 7},
            {'ime': 'Uros', 'godine': 19, 'prosek': 7.6}]
z3 = list(filter(lambda x: x['godine'] > 21, studenti))
# print(sorted(z3, key=lambda st: st['prosek']))

# 4.
lista_recenica = ["Hello, World!", "Python is cool",
                  "Functional programming rocks"]
reci_po_str = map(lambda x: len(x.split()), lista_recenica)
# print('Ukupno reci:', reduce(lambda x, y: x+y, reci_po_str))

# 5.
torke = [('Ana', '4', 'Matematika'),
         ('Jovan', '5', 'Fizika'),
         ('k', '5', 'Matematika'),
         ('A', '3', 'Matematika')]
# prosecna ocena po predmmetu
prosek = {}
# za svaki predmet racuna njegovu prosecnu ocenu i stavlja u recnik
for i in torke:
    pr = i[2]
    # izdvaja sve el sa predmetom pr iz liste
    predmet = list(filter(lambda x: x[2] == pr, torke))
    # sabira sve ocene is pr koje smo izdvojili pomocu map
    ocene_suma = reduce(lambda x, y: x+y, map(lambda x: int(x[1]), predmet))
    broj_ocena = len(predmet)
    prosek[f'{pr}'] = ocene_suma / broj_ocena
# print(prosek)

# 6.
serija = [16, 3, 24, 13, 55]
z6 = map(lambda x: serija[x]-serija[x-1], range(1, len(serija)))
# print(list(z6))

# 7.
l = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# broji el i stavlja u recnik
sve = list(map(lambda x: {x: l.count(x)}, l))
# print(reduce(lambda x, y: {**x, **y}, sve))


# 8.
@vreme_izvrsavanja
def pravougaonici():
    with open('rectangles.txt') as dimenzije:
        kvadrati = []
        maks = 0
        for dim in dimenzije.readlines():
            dim = (dim.removesuffix('\n')).split(',')
            a = float(dim[0])
            b = float(dim[1])
            if a == b:
                kvadrati.append((a, b))
                if a*b > maks:
                    maks = a*b
    return f'Kvadrati su: {kvadrati}\npovrsina najveceg je: {maks}'


# print(pravougaonici())


# 9.
def naselje():

    naziv_grada = input('Unesite naziv grada: ')
    naselje_max = ''
    stanovnika_max = 0
    with open('cities.txt') as cities:
        for linija in cities.readlines():
            g = (linija.removesuffix('\n')).split(',')
            grad = g[0]
            ime_naselja = g[1]
            br_stanovnika = int(g[2])
            if grad.lower() == naziv_grada.lower() and br_stanovnika > stanovnika_max:
                stanovnika_max = br_stanovnika
                naselje_max = ime_naselja
    return f'Naselje u {naziv_grada} sa najvecim brojem stanovnika je: {naselje_max}.'


# print(naselje())


# 10.
@vreme_izvrsavanja
def najmanji_broj_stanovnika():
    unos = input('Unesite naziv drzave: ')
    najmanje_stanovnika = 999999999999
    naziv_grad = ''
    with open('population.txt') as fajl:
        for linija in fajl.readlines():
            tmp = (linija.removesuffix('\n')).split(',')
            drzava = tmp[0]
            grad = tmp[1]
            broj_stanovnika = int(tmp[2])
            if drzava.lower() == unos.lower() and broj_stanovnika < najmanje_stanovnika:
                najmanje_stanovnika = broj_stanovnika
                naziv_grad = grad
        return f'Grad sa najmanjim brojem stanovnika: {naziv_grad}.'


# print(najmanji_broj_stanovnika())


# 11.
def broj_stanovnika():
    unos = input('Unesite naziv drzave: ')
    ukupno_stanovnika = 0
    with open('population.txt') as fajl:
        for linija in fajl.readlines():
            tmp = (linija.removesuffix('\n')).split(',')
            drzava = tmp[0]
            br_stanovnika = int(tmp[2])
            if drzava.lower() == unos.lower():
                ukupno_stanovnika += br_stanovnika
    return ukupno_stanovnika


# print(broj_stanovnika())

# 12.

def heksadecimalni():
    hexa, ukupno = 0, 0

    with open('hexa.txt') as fajl:
        for broj in fajl.readlines():
            if broj.startswith('0x'):
                hexa = int((broj.removesuffix('\n')), 0)
                if hexa % 10 == 3:
                    ukupno += hexa

    return ukupno


# print(heksadecimalni())


# 13.
def append_to_file(list_of_products):
    with open('products.txt', mode='w') as fajl:
        fajl.write('Naziv, Opis, Godina, Kolicina, Cena\n')
        for proizvod in list_of_products:
            fajl.write(f'{proizvod['naziv']}, {proizvod['opis']}, {proizvod['godina']}, {
                       proizvod['kolicina']}, {proizvod['cena']}\n')


lista = [{'naziv': 'Televizor', 'opis': 'LG televizor 43inc', 'godina': 2019, 'kolicina': 10, 'cena':
          300}, {'naziv': 'Televizor', 'opis': 'Samsung televizor 39inc', 'godina': 2017, 'kolicina': 5,
                 'cena': 250},]

# append_to_file(lista)


def get_products_older_than(godina):
    with open('products.txt') as fajl:
        # fajl.readline()
        next(fajl)
        for proizvod in fajl.readlines():
            p = proizvod.split(', ')
            if int(p[2]) >= godina:
                print(proizvod)


# get_products_older_than(2018)

def iz_fajla_u_dict():
    proizvodi = []
    with open('products.txt') as fajl:
        next(fajl)
        for proizvod in fajl:
            info = proizvod.strip().split(', ')
            proizvodi.append(
                {'naziv': info[0], 'opis': info[1], 'godina': int(info[2]),
                    'kolicina': int(info[3]), 'cena': float(info[4])}
            )
    return proizvodi


proizvodi = iz_fajla_u_dict()


def max_possible_revenue(proizvodi):
    prihod = 0
    for p in proizvodi:
        prihod += p['kolicina'] * p['cena']
    return prihod


# print(max_possible_revenue(proizvodi))


# 14.
def append_to_file_student(list_of_students):
    with open('students.txt', mode='w') as fajl:
        fajl.write('Naziv, Opis, Godina, Kolicina, Cena\n')
        for student in list_of_students:
            fajl.write(f'{student['ime']},{student['prezime']},{student['godina']},{
                       student['prosek']}\n')


# append_to_file_student([{'ime': 'Marko', 'prezime': 'Markovic', 'godina': 2, 'prosek': 8.6}, {'ime': 'Boris',
            #   'prezime': 'Boricic', 'godina': 3, 'prosek': 7.9}, {'ime': 'Novak', 'prezime': 'Novovic',
            #   'godina': 3, 'prosek': 6.9}])

@vreme_izvrsavanja
def get_students_with_greater_grade(year, grade):
    ocene = {'A': (9.5, 10), 'B': (8.5, 9.5),
             'C': (7.5, 8.5), 'D': (6.5, 7.5),
             'E': (6, 6.5)}
    if grade not in ocene.keys():
        return 'Pravilno unesite ocenu!(A-F)'
    if 1 < year > 8:
        return 'Pravilno unesite godinu!(1-8)'

    studenti = []
    ocena = ocene[grade][0]
    with open('students.txt') as fajl:
        next(fajl)
        for student in fajl:
            s = student.split(',')
            if (int(s[2]) == year) and (float(s[3]) >= ocena):
                studenti.append({'ime': s[0], 'prezime': s[1],
                                'godina': int(s[2]), 'prosek': float(s[3])})
    return studenti


# year = int(input('Uneti godinu, ceo broj 1-8: '))
# grade = input('Uneti ocenu(slovo) A (9.5 - 10), B (8.5 - 9.5 ne uključujući), C (7.5 - 8.5 ne uključujući), D (6.5 - 7.5 ne uključujući) ili E (6 - 6.5 ne uključujući : ')
# year = 3
# grade = 'C'
# year = 4
# grade = 'C'
# print(get_students_with_greater_grade(year, grade))


# 15.
def kartica_validacija(broj_kartice):
    # broj_kartice = input('Unesite broj kartice: ')
    if len(broj_kartice) != 16 or not broj_kartice.isdigit():
        return False
    kartica = list(int(i) for i in broj_kartice)
    for i in range(len(broj_kartice)-2, -1, -2):
        br = int(kartica[i]) * 2
        if br > 9:
            u = br % 10 + br//10
            kartica[i] = u
        else:
            kartica[i] = br

    print(kartica)
    suma = sum(kartica)
    return suma % 10 == 0


# print(kartica_validacija('1020080000000030'))

# b)
@vreme_izvrsavanja
def validni_fajl():
    with open('kartice.txt', 'r') as fajl:
        with open('cardvalid.txt', 'w') as upis:
            for kartica in fajl:
                validno = ('Valid' if kartica_validacija(
                    kartica.strip()) else 'Invalid')
                upis.write(f'{kartica.strip()} -> {validno}\n')


# validni_fajl()
