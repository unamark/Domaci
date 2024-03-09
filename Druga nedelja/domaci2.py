import math

# 1.
def carobni_stapic():
    broj = int(input("Upisite broj kako bi otvorili portal:"))
    if(broj % 2 == 0):
        print('Portal se otvara!')
    else:
        print('Portal ostaje zatvoren!')

#carobni_stapic()
# 2.
def jabuke(p, m):
    if(p > m):
        print('Pobednik u berbi jabuka je Petar!')
    else:
        print('Pobednik u berbi jabuka je Miloš!')
#jabuke(15, 4)
# 3.
def pristup_ispitu(prisustvo, seminarski):
    if(prisustvo > 75 and seminarski == 1):
        print('Studentu dozvoljeno prisustvo ispitu!')
    else:
        print('Studentu nije dozvoljeno prisustvo ispitu!')
#pristup_ispitu(76, 1)
# 4.
def kucni_red(vreme):
    if((vreme >= 17 and vreme <= 22) or (vreme >= 6 and vreme <= 13)):
        print('Radovi su dozvoljeni!')
    else:
        print('Radovi nisu dozvoljeni!') 
# kucni_red(23)
# 5.
def basta(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True      
#if basta(7, 5, 10):
    print('Moguce je napraviti bastu u obliku trougla.')
#else:
    print('Nije moguce napraviti bastu u obliku trougla.')

# 6.
def pcela(x,y):
    if y == 2 * x + 5:
        print('Pcela se krece po zici.')
    else:
        print('Pcela se ne krece po zici.')
#pcela(3, 5)
# 7.
def takmicenje(m1, p1, m2, p2):
    prvi = m1 + p1
    drugi = m2 + p2
    if drugi > prvi :
        print('Pobedio je drugi.')
    elif drugi == prvi:
        if p1 > p2:
            print('Pobedio je prvi.')
        else:
            print('Pobedio je drugi.')
    else:
        print('Pobedio je prvi.')
#takmicenje(45, 13, 50, 8)
# 8.
def uspeh_ucenika(prosek):
    if prosek >= 4.5:
        print('Odlican!')
    elif prosek >= 3.5:
        print('Vrlo dobar.')
    elif prosek >= 2.5:
        print('Dobar.')
    elif prosek >= 2:
        print('Dovoljan.')
    elif prosek == 1:
        print('Nedovoljan.')
#uspeh_ucenika(4.47)
# 9.
def zavesa(x1, y1, x2, y2, x3, y3, x4, y4):   
    povrsina_zavese = abs((x2 - x1) * (y2 - y1))
    povrsina_prozora = abs((x4 - x3) * (y4 - y4))  
    
    if povrsina_zavese >= povrsina_prozora:
        print('Zavesa moze da prekrije prozor.')
    else:
        print('Zavesa ne prekriva prozor.')
# zavesa(1,3,7,8,3,1,5,2)
# 10.
def pikado(poluprecnik , c_x, c_y, s_x, s_y):
    rastojanje_strelica_centar = math.sqrt((c_x - s_x)**2 + (c_y - s_y)**2)
    if rastojanje_strelica_centar <= poluprecnik:
        print('Strelica je pogodila tablu.')
    else:
        print('Strelica nije pogodila tablu.')
# pikado(2, 10, 10, 12, 10)
# 11.
def kretanje_mrava(m_x, m_y, s_x, s_y, s_xd, s_yd):
    #(m_x, m_y) koordinate mrava
    # (s_x, s_y) leva koordinata stola, (s_xd, s_yd) desna koordinata stola
    if(m_x >= s_x and m_y <= s_y) and (m_x <= s_xd and m_y >= s_yd):
        print('Mrav se krece po ivici stola.')
    else:
        print('Mrav se ne krece po ivici stola.')
#kretanje_mrava(1,3, 4, 5, 1, 3)
# 12.
def dvocifreni(broj):
    c1 = broj // 10
    c2 = broj % 10
    if c1 > c2:
        print(c1 - c2)
    elif c1 < c2:
        print(c1 + c2)
    else:
        print(c1 * c2)
#dvocifreni(56)
# 13.
def veci_sto(r1, r2):
    povrsina1 = r1**2 * math.pi
    povrsina2 = r2**2 * math.pi
    if povrsina1 > povrsina2:
        print('Obim veceg stola je ', 2 * r1 * math.pi)  
    elif povrsina2 > povrsina1:
        print('Obim veceg stola je ', 2 * r2 * math.pi)
    else:
        print('Stolovi su iste velicine.')
# veci_sto(15, 16)
# 14.
def proizvodi(a, b, c):
    namjanja = a + b
    par = (a,b)
    if namjanja > a + c:
        namjanja = a + c
        par = (a,c)
    elif namjanja > b + c:
        namjanja = b + c
        par = (b,c)
    print(f'Prizvodi sa cenama {par} daju najmanju vrednost: {namjanja}.')
# proizvodi(5,2,7)
# 15.
def prestupna_godina(godina):
    if (godina % 4 == 0 and godina % 100 != 0) or godina % 400 == 0:
        print(f'Godina {godina}. je prestupna.')
    else:
        print(f'Godina {godina}. nije prestupna.')
# prestupna_godina(2024)
# 16.
def unutar_pravougaonika(tacka_x, tacka_y, x1, y1, x2, y2):
    if x1 <= tacka_x <= x2 and y1 <= tacka_y <= y2:
       return True
    else:
        return False
# print('Jeste' if unutar_pravougaonika(1, 3, 4, 5, 3 ,6) else 'Nije')   
# 17.
def dva_kvadrata(a, b):
    broj_kvadrata = b // a
    if broj_kvadrata >= 2:
        #print(broj_kvadrata)
        return True
    else:
        #print(broj_kvadrata)
        return False
# print('Mogu' if dva_kvadrata(3, 7) else 'Ne mogu')
# 18.
def agregatno_stanje_vode():
    temperatura = int(input('Unesite temperaturu vode: '))
    if temperatura > 0 and temperatura < 100:
        print('tecno')
    elif temperatura <= 0:
        print('cvrsto')
    else:
        print('gasovito')
# agregatno_stanje_vode()
# 19.
def popust_skola(puna_skolarina, prosek_ucenika, nagrada):
    skolarina = puna_skolarina

    if prosek_ucenika >= 4.5:
        skolarina -= puna_skolarina * 40 / 100
    elif prosek_ucenika >= 3.5:
        if nagrada == 1:
            skolarina -= puna_skolarina * 30 / 100
        else:
            skolarina -= puna_skolarina * 20 / 100
    elif prosek_ucenika >= 2.5:
        if nagrada == 1:
            skolarina -= puna_skolarina * 30 / 100
        else:
            skolarina -= puna_skolarina * 10 / 100
    print(skolarina)
# popust_skola(1100.75, 2.7, 1)
# 20.
def operacije_cifre():
    n = int(input('Unesite cetvorocifren broj: '))
    
    if(n % 2 == 0):
        zbir = 0
        while n != 0:
            cifra = n % 10
            n = n // 10
            if cifra % 2 == 0:
                zbir += cifra
        return zbir
    else:
        proizvod = 1
        while n != 0:
            cifra = n % 10
            n = n // 10
            if cifra % 2 != 0:
                proizvod *= cifra
        return proizvod
# print(operacije_cifre())
# 21.
def racuna_y(x):
    y = 0
    if x <= -7:
        y = -2*x + 7/2
    elif x < 1:
        y = (x**2 - 3*x + 5) / (x**2 + 2)
    elif x <= 8:
        y = math.sqrt(x**2 + 2*x + 2) + math.sqrt(abs(3/2*x - 4/7))
    else:
        y = abs(3/x**2 - 11*x)
    
    return y
# print(racuna_y(3))
# 22.
def kvadranti(x, y):
    if x >= 0 and y >= 0:
        print(f'Tacka {x,y} pripada 1 kvadrantu.')
    elif x < 0 and y >= 0:
        print(f'Tacka {x,y} pripada 2 kvadrantu.')
    elif x >= 0 and y < 0:
        print(f'Tacka {x,y} pripada 4 kvadrantu.')
    else:
        print(f'Tacka {x,y} pripada 3 kvadrantu.')
# kvadranti(-1, 0)
# 24.
def skratiti_tekst(tekst):
    skraceni = tekst
    if(len(tekst) > 30):
        skraceni = tekst[:30] + '...'
    return skraceni
# print(skratiti_tekst('0123456789012345678901234567890125'))
# 25.
def uklanja(tekst):
    novi = tekst[1:len(tekst)-1]
    return novi
# print(uklanja('jaoooj'))
# 26.
def brojni_sistem():
    broj = input('Unesite broj: ')
    prefiks = broj[:2]

    if prefiks == '0b':
        print(f'Broj {broj} je binarni.')
    elif prefiks == '0o':
        print(f'Broj {broj} je oktalni.')
    elif prefiks == '0x':
        print(f'Broj {broj} je heksadecimalni.')
    else:
        print(f'Broj {broj} je dekadni.')
# brojni_sistem()
# 27.
def samoglasnik(string):
    string.lower()
    for i in range(0, len(string)):
        s = string[i]
        if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
            print('String sadrzi bar jedan samoglasnik.')
            break
# samoglasnik('AKJOhduis')
# 28.
def zavrsava(string, target):
    if string[len(string)-len(target):] == target:
        print('zavrsava se')
    else:
        print('ne')
# zavrsava('Abcd', 'cd')
# 29.
def binarni(string):
    for i in range(len(string)):
        if string[i] != '0' and string[i] != '1':
            return False
    
    return True
#print('Jeste binarni.' if binarni('013101010') else 'Nije binarni broj.')
# 30.
def zbir():
    n = int(input('unesite broj n:'))
    zbir, proizvod = 0, 1
    parni, neparni = 0, 0
    for i in range(1,n):
        if i % 2 == 0:
            zbir += i
            parni += 1
        else:
            proizvod *= i
            neparni += 1
    
    print(f'Zbir: {zbir}, proizvod: {proizvod}.\nBroj parnih: {parni}, broj neparnih: {neparni}.')
# zbir()  
# 31.
def sumira_segment():
    start = int(input('Unesite pocetak '))
    end = int(input('Unesite kraj '))
    suma = 0
    for i in range(start, end+1):
        if i % 2 == 0 and i % 4 != 0:
            suma += i**2
    return suma
# print(sumira_segment())
# 32.
def deljivi(a, b, delilac):
    suma, broj = 0, 0
    for i in range(a+1, b):
        if i % delilac == 0:
            suma += i
            broj += 1
    print(f'Suma {suma}, broj deljivih elemenata {broj}.')
# deljivi(1, 5, 3)
# 33.
def sabira_cifre(broj):
    suma = 0
    while (broj != 0):
        suma += broj % 10
        broj = broj // 10  
    return suma
# print(sabira_cifre(125))
# 34.
def proizvod_cifara(tekst):
    suma = 0
    for i in tekst:
        if i.isdigit():
            suma += int(i)
    print('Suma je ', suma)
# proizvod_cifara('1cjbcj3hfckj11d1')
# 35.
def cifre_u_stringu(string):
    broj_cifara = 0
    br = ''
    for i in string:
        if i.isdigit():
            broj_cifara += 1
            br += i
    print(f'Broj cifara je {broj_cifara} => {int(br)}.')
#cifre_u_stringu('Hi Mr.Rober53. How are you today? Today is 08.10.2019')
# 36.
def enkriptuje(s):
    enkriptovano = ''
    for i in s:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            enkriptovano += '1'
        else:
            enkriptovano += '0'
    return enkriptovano
# print(enkriptuje('abaae'))
# 37.
def igrac_u_plusu(listica):
    suma = 0
    for c in listica:
        if c == '1':
            suma += 1
        elif c == '*':
            suma -= 1
    
    if suma >= 0:
        print('Igrac je u plusu.')
    else:
        print('Igrac je u minusu.')
# igrac_u_plusu('100000**1*1*00*100')
# 38.
def enkriptstr(s):
    enkriptovano = ''
    for i in s:
        if i.isdigit():
            if int(i) % 2 == 0:
                enkriptovano += '0'
            else:
                enkriptovano += '1'
        else:
            enkriptovano += i
    return enkriptovano
# print(enkriptstr('15023'))
# 39.
def narcissistic(broj):
    br_cif, suma = 0, 0
    tmp = broj
    cifre = []
    while tmp != 0:
        cif = tmp % 10
        cifre.append(cif)
        br_cif += 1
        tmp //= 10

    for cifra in cifre:
        suma += cifra**br_cif
    
    if suma == broj:
        print('Da')
    else:
        print('Ne')
# narcissistic(1634)
# 40.
def apsolutna_suma(niz):
    suma = 0
    for i in niz:
        if i < 0 and i % 2 == 0:
            suma += abs(i)
    return(suma)
# print(apsolutna_suma([-2, 7, -5, 3, 1, -4]))   
# 41.
def manji(L, max):
    ukupno = 0
    for i in L:
        if i < max:
            ukupno += 1
    return ukupno
# print(manji([1,2,3], 3))
# print(manji([-1, 0, 5], -2))
# 42.
def market(cene, popust):
    manja = 0
    originalne = 0
    for i in cene:
        originalne += i
        manja += i*popust/100
    print(f'Market ce zaraditi {manja}€ manje u odnosu na {originalne}€.')
# market([2, 4, 11.22, 3, 4.5, 20.15], 10)
# 43.
def likovno(ocene):
    tri, cetiri, pet = 0, 0, 0
    for i in ocene:
        if i == 3:
            tri += 1
        elif i == 4:
            cetiri += 1
        elif i == 5:
            pet += 1
    print(f'{pet} ucenika ima ocenu 5, {cetiri} ucenika ocenu 4 i {tri} ucenika ocenu 3.')
# likovno([3, 5, 4, 5, 5, 3, 4, 4, 5, 5, 4, 5])
def lik2(ocene):
    uk = [0,0,0,0,0,0]
    for i in ocene:
        uk[i] += 1
    print(f'{uk[5]} ucenika ima ocenu 5, {uk[4]} ucenika ocenu 4 i {uk[3]} ucenika ocenu 3.')
# lik2([3, 5, 4, 5, 5, 3, 4, 4, 5, 5, 4, 5])
# 44.
def utakmice(posete):
    return max(posete)
# print(utakmice([3, 15, 75, 12, 246, 2, 98, 45, 22, 73]))
# 45.
def prosecna_plata(plate):
    broj = 0
    prosek = sum(plate) / len(plate)
    for z in plate:
        if z > prosek:
            broj += 1
    print(f'{broj} zaposlenih ima vecu platu od prosecne ({prosek})')
# prosecna_plata([500, 600, 700])   
# 46.
def drugo_max_primanje(plate):
    print(sorted(plate, reverse=True)[1])
# drugo_max_primanje([500, 600, 700, 650, 300])
# 47.
def minmax():
    a = int(input('Unesite broj: '))
    b = int(input('Unesite broj: '))   
    c = int(input('Unesite broj: '))
    print(f'max = {max(a, b, c)}, min = {min(a, b, c)}')
# minmax()
# 48.
def stepenovanje(x, n):
    ukupno, i = 1, 1
    while i <= n:
        ukupno *= x
        i +=1
    return ukupno
# print(stepenovanje(13, 2))
# 49.
def skrati(s, duzina):
    if len(s) <= duzina:
        s1 = s +'...'
    else:
        s1 = s[:duzina] + '...'
    print(s1)
# skrati('abcde', 10)
# 50.
def samoglasnici(string):
    novi = ''
    for i in string:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            novi += i
    return novi
# print(samoglasnici('Samo samoglasnici.'))
# 51.

def lozinka(rec):
    up, low, dig = 0, 0, 0
    for i in rec:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
        elif i.isdigit():
            dig +=1
    if len(rec) >= 8 and up >= 1 and low >= 1 and dig >= 1:
        return True
    else:
        return False
# print('YES' if lozinka('Ahgj3s2ojj') else 'NO')
# 52. 
def prosireni(a, pre, suf, num):
    novi = pre*num + a + suf*num
    return novi
# print(prosireni('test', 'pr', 'su', 2))
# 54.
def slobodni(string, pozicija):
    if pozicija == 0 and string[1] == 0:
        return True
    elif (pozicija == len(string)-1  or pozicija == -1) and string[pozicija-1] == 0:
        return True
    elif string[pozicija-1] == 0 and string[pozicija+1] == 0:
        return True
    else:
        return False
# print('1' if slobodni('01010', 2) else '0')
# 55.
def voda(h, o):
    broj_molekula = 0
    while h > 1 and o > 0:
        h -= 2
        o -= 1
        broj_molekula += 1
    return broj_molekula
# print(voda(7, 2))
# 56.
def jednocifreni_neg(string):
    ukupno = 0
    n = string.split('-')
    for i in n:
        if i[0] == '+':
            continue
        elif len(i) == 1:
            ukupno += 1
        else:
            deo = i[0:i.find('+')+1]
            if len(deo) == 1:
                print(deo)
                ukupno += 1
            else:
                continue
    print(ukupno)
    #print(n)
# jednocifreni_neg('+23-2-32+4-22-4')
# 57. 
# narcissistic(163)
# 58.
def bez_cifara(string):
    novi = ''
    for i in string:
        if i.isdigit():
            continue
        else:
            novi += i
    
    return novi
# print(bez_cifara('Hi Mr. Rober53. How are you today? Today is 08.10.2019'))
# 59.
# print(enkriptstr('15023'))
# 60.
def kvadrira_el_segmenta():
    start = int(input('Unesite pocetak '))
    end = int(input('Unesite kraj '))
    suma = 0
    for i in range(start, end+1):
        if i % 3 == 0 and i % 6 != 0:
            suma += i**2
    return suma
# print(kvadrira_el_segmenta())
# 61.
def velika_slova(tekst):
    novi = ''
    for k in tekst:
        if k.isupper():
            novi += k
    return novi
# print(velika_slova('Prva recenica. Ovo je druga recenica. Na kraju treca.'))
# 62.
def heksadecimalni(string):
    broj = 0
    br = string.split(' ')
    for i in br:
        if i.find('0x') == 0:
            broj += 1
    return broj
# print(heksadecimalni('12 0x1A 0001 121 0x2'))
# print(heksadecimalni('12 001 31'))
# 63.
def najduza_rec(string):
    reci = string.split(' ')
    print(max(reci, key=len))
# najduza_rec('nar kivi grejpfrut kokos ananas')
# 64.
def zbir_najmanje_najvece_cifre(broj):
    najmanja, najveca = 9, 0
    while broj > 0:
        cifra = broj % 10
        najmanja = min(najmanja, cifra)
        najveca = max(najveca, cifra)
        broj //= 10
    
    print(f'Najveca: {najveca}, najmanja: {najmanja}, zbir = {najmanja+najveca}')
# zbir_najmanje_najvece_cifre(245739)
# 65.
def stubici():
    d = float(input('Unesite duzinu terase: '))
    n = int(input('Unesite broj stubica: '))
    s = float(input('Unesite sirinu stubica u cm: '))

    r = (d * 100 - n * s) / (n + 1)
    print(f'Rastojanje izmedju stubica je {round(r, 2)} cm')
# stubici()
# 66.
def lista_brojeva(lista):
    dvocifreni, trocifreni = 0, 0
    for broj in lista:
        if broj > 99 and broj < 1000:
            trocifreni += 1
        elif broj > 9 :
            dvocifreni += 1
        else:
            continue
    if dvocifreni > trocifreni:
        print('Vise ima dvocifrenih.')
    else:
        print('Vise ima trocifrenih.')
# lista_brojeva([123, 24, 2, 785, 1457, 31, 45, 9, 147, 111])
# 67.
def ponavljanja_broja(lista):
    broj = int(input('Unesite broj: '))
    return lista.count(broj)
# print(ponavljanja_broja([0, 11, 2, 4, 6, 7, 2, 1, 4, 13]))
# 68.
def uveca_zarade(zarade, x):
    prosek = sum(zarade) / len(zarade)
   
    for i in range(len(zarade)):
        if zarade[i] > prosek:
            zarade[i] += x
    return zarade
# print(uveca_zarade([200, 700, 350, 600, 212, 473], 2))
# 69.
def iznad_proseka(zarade):
    prosek = sum(zarade) / len(zarade)
    iznad = 0
    for i in range(len(zarade)):
        if zarade[i] > prosek:
            zarade[i] -= zarade[i] * 10 / 100
            if zarade[i] > prosek:
                iznad += 1
        elif zarade[i] < prosek:
            zarade[i] += zarade[i] * 10 / 100
            if zarade[i] > prosek:
                iznad += 1
    return iznad
# print(iznad_proseka([300, 750, 600]))
# 70.
def deljivi_sa_tri(lista):
    zbir = 0
    for i in lista:
        if i % 3 == 0:
            zbir += i**2
    return zbir
# print(deljivi_sa_tri([1, 4, 9, 7, 16, 15]))
# 71.
def analiza_liste(lista):
    ukupan = 0
    for broj in lista:
        k = math.sqrt(broj)
        if k == int(k):     #   math.sqrt(broj) % 1 == 0
            ukupan += 1
    return ukupan
# print(analiza_liste([4, 7, 9, 6, 13]))
# 72.
def ekonomija_i_razvoj(ocene):
    suma, veca, br = 0, 0, 0
    for i in ocene:
        if i > 5:
            suma += i
            br += 1
    prosek = suma / br  
    
    for i in ocene:
        if i > prosek:
            veca += 1
    return veca
# print(ekonomija_i_razvoj([5, 7, 9, 10, 6, 8, 7]))
# 73.
def inventar_igraca(inventar, pozicija):
    for i, item in enumerate(inventar, 1):
        print(i, item)
    if pozicija < 1 or pozicija > len(inventar):
        return None
    else:
        return inventar[pozicija-1]
# print(inventar_igraca(['mac', 'sesir', 'rukavice', 'kompas', 'mapa'], 3))
# 74.
def plata_u_dolarima(plate):
    prosek = sum(plate)/len(plate)

    print(prosek * 1.1)
# plata_u_dolarima([12000, 1500, 3500, 4800, 11260, 15600])  
# 75.
def stednja(stednje, kamata):
    ukupno = 0
    for i in stednje:
        ukupno += i*kamata/100
    return sum(stednje)-ukupno
# print(stednja([1500, 11000, 11110, 500, 5000], 5))
# 76.
def menja_elemente(lista, element, zamena):
    lista = [zamena if el == element else el for el in lista]
    print(lista)
# menja_elemente([2, 7, 13, 4, 2, 78], 2, -2)
# 77.
def sortirana(lista):
    return lista == sorted(lista)   
# print(sortirana([0, 1, 3, 4, 5]))
# 78.
def drugi(artikli):
    return sorted(artikli, reverse=True)[1]
# print(drugi([15.76, 28.33, 3.5, 66, 12, 10.99]))
# 79.
def suprotna_vrednost(elementi):
    ukupno = 0
    for i in elementi:
        if i > 0 and elementi.count(-i) > 0:
            ukupno += 1
    return ukupno
# print(suprotna_vrednost([1, 5, 4, 7, -3, 12, -1, 3]))
# 80.
def skok_razlika(duzine):
    najduzi = max(duzine)
    najkraci = min(duzine)
    return najduzi - najkraci
# print('Razlika izmedju najduzeg i najkraceg skoka je', skok_razlika([15, 17, 2, 9, 19]))
# 81.
def akcije(cene):
    najveci_pad = cene[1] - cene[0]
    najveci_porast = cene[1] - cene[0]
    for i in range(len(cene)-1):
        pad = cene[i+1] - cene[i]
        if pad < najveci_pad:
            najveci_pad = pad
        if pad > najveci_porast:
            najveci_porast = pad
    print(f"Najveci pad je {abs(najveci_pad)}, najveci porast cena akcija je {najveci_porast}.")
# akcije([33.45, 156.21, 134, 163.3, 80.5, 13.78])
# 82.
def pozoriste(slobodna_mesta, n):
    najbolji, ostalo = 0, 0
    
    for i in range(len(slobodna_mesta)):
        o = slobodna_mesta[i] - n
        if o > ostalo:
            ostalo = o
            najbolji = i
    return najbolji
# print(pozoriste([10, 8, 15, 12, 7], 6))
# 83.
def putovanje(destinacije,budzet):
    dest = sorted(destinacije, reverse=True)
    ostaje = budzet
    for i in dest:
        o = budzet - i       
        if o >= 0 and o < ostaje:
           ostaje = o
    return ostaje
# print(putovanje([1453, 1200, 350, 678, 2330], 2350))
# 84.
def restoran(kapacitet, gosti):
    fali = gosti - sum(kapacitet) 
    stolova = fali / 4
    return math.ceil(stolova)
# print(restoran([4, 6, 2, 8, 5], 34))
# 85.
def rezervacija_bioskop(slobodno, n):
    potrebno = 0
    for i in sorted(slobodno, reverse=True):
        if n - i <= 0:
            potrebno += 1
            break
        elif n - i > 0:
            potrebno += 1
            n = n-i
    return potrebno
# print(rez_bioskop([4, 6, 2, 8, 5], 15))
# 86.
def absolute_of_even_sum(niz_brojeva):
    suma = 0
    for i in niz_brojeva:
        if i < 0 and i % 2 == 0:
            suma += abs(i)
    return(suma)
# print(absolute_of_even_sum([-2, 7, -5, 3, 1, -4]))
# 87.
def presek_liste(a, b):
    a_skup = set(a)
    b_skup = set(b)
    return list(a_skup & b_skup)
# print(presek_liste([1, 2, 'a'], ['a', 2]))
# print(presek_liste([2, 3, 4], [1, 1, 7]))
# 88.
def br_elemenata(a, max):
    manji = 0
    for i in a:
        if i < max:
            manji += 1
    return manji
# print(br_elemenata([-1,0,5],-2))
# 89.
def br_elemenata(a):
    return suprotna_vrednost(a)
# print(br_elemenata([1, 2, -1, 3, -3]))
# print(br_elemenata([20, 10, -10, 100]))
# 90.
def update_list(a, x):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a[i] += x
    return a
# print(update_list([1, 2, -1, 3, -4], 3))
# print(update_list([21, 10, -10, 100], 5))
# 91.
def second_max(a):
    return sorted(a, reverse=True)[1]
# print(second_max([1, 22, 33, 44]))
# 92.
def unos_proizvoda(n):
    i = 1
    lista_proizvoda = []
    while n > 0:
        naziv = input(f'Unesite naziv {i}. proizvoda: ')
        opis = input(f'Unesite opis {i}. proizvoda: ')
        cena = float(input(f'Unesite cenu {i}. proizvoda: '))
        broj_artikala = int(input(f'Unesite broj artikala {i}. proizvoda: '))
        proizvod = {
            'naziv': naziv,
            'opis': opis,
            'cena': cena,
            'broj_artikala': broj_artikala
        }
        lista_proizvoda.append(proizvod)
        n -= 1
        i += 1
    return lista_proizvoda

def pro_naziv(proizvodi, search_term):
    for proiz in proizvodi:
        if proiz['naziv'].find(search_term) == 0:
            return proiz
# proizvodi = (unos_proizvoda(2))
# print(pro_naziv(proizvodi, 'ko'))  
# 93.
def igrice(lista_igrica):
    x = int(input('Unesite min ocenu: '))
    y = input('Unesite zeljenog izdavaca: ')
    return [igrica for igrica in lista_igrica if igrica['ocena'] > x and igrica['izdavac'] == y]

# igricee = [
#     {'ime': 'kola', 'izdavac':'pop', 'godina_izlaska':2020,'ocena':6.7},
#     {'ime': 'gta', 'izdavac':'pop', 'godina_izlaska':2019,'ocena':8.9},
#     {'ime': 'lets play', 'izdavac':'nin', 'godina_izlaska':2023,'ocena':7.5},
#     {'ime': 'tenis', 'izdavac':'pop', 'godina_izlaska':2012,'ocena':3.5}
# ]
# print(igrice(igricee))

# 94.
def get_ewfbyr(string, slovo):
    
    s = string.split(' ')
    # reci = []
    # for i in s:
    #     if len(i) % 2 == 0 and slovo not in i:
    #         reci.append(i)
    # return reci
    reci = [i for i in s if len(i) % 2 == 0 and slovo not in i]
    return reci
# print(get_ewfbyr('words with even number of letters without character d', 'd'))
# 95.
def longest_increasing(input_list):
    najduzi = [input_list[0]]
    trenutni = [input_list[0]]

    for i in range(1, len(input_list)):
        if input_list[i-1] > 0 and input_list[i] >= input_list[i - 1]:
            trenutni.append(input_list[i])
            if len(trenutni) > len(najduzi):
                najduzi = trenutni[:]
        else:
            trenutni = [input_list[i]]

    return najduzi
# print(longest_increasing([1, 2, 3, -1, 0, 5, 6, 7, 10, 10, 1]))
# 96.
def razbiti_string(string, number):
    lista = []
    for i in range(0, len(string), number):
        lista.append(string[i:i+number])
    if len(lista[-1]) < number:
        lista[-1] = lista[-1] + '*' * (number - len(lista[-1]))
    return lista
# print(razbiti_string('danas polažemo test', 5))
# print(razbiti_string('kurs web program.', 6))
# print(razbiti_string('da', 7))
# 97.
# proizvodi = unos_proizvoda(1)
def trguje(proizvodi, naziv, raspolozivi_novac):
    for proizvod in proizvodi:
        if proizvod['naziv'] == naziv:
            cena = proizvod['cena']
            broj = proizvod['broj_artikala']
            ukupno = raspolozivi_novac // cena
            if ukupno > broj:
                return int(broj)
            else:
                return int(ukupno)
# print(trguje(proizvodi, 'lampa', 10))
# 98.
def jednostavna_akcije(zahtev):
    deo = zahtev.split(' ')
    kolicina = int(deo[1])
    cena = float(deo[2])
    status = deo[3]

    if status == 'B':
        return kolicina * cena, 0
    elif status == 'S':
        return 0, kolicina * cena
def slozena(zahtev):
    ukupno_kupljenih = 0
    ukupno_prodatih = 0
    akcije = zahtev.split(',')
    for akcija in akcije:
        kupljena, prodata = jednostavna_akcije(akcija)
        ukupno_kupljenih += kupljena
        ukupno_prodatih += prodata
    
    print(f'Buy:{round(ukupno_kupljenih, 2)} Sell:{round(ukupno_prodatih, 2)}')
# slozena('ZNG 1300 2.66 B,NY 50 56.32 B,OWW 1000 11.623 B,OGG 20 580.1 B')
# 99.
def split_string(string, number):  
    lista = []
    for i in range(0, len(string), number):
        lista.append(string[i:i+number])
    return lista
# print(split_string('kurs web program.', 6))
# 100.
def ima_veliko_slovo(string):
    for slovo in string:
        if slovo.isupper():
            return True
    return False
def ima_malo_slovo(string):
    for slovo in string:
        if slovo.islower():
            return True
    return False
def ima_broj(string):
    for slovo in string:
        if slovo.isdigit():
            return True
    return False
def check_password (input_string, min_string_len, flagUpper, flagLower, flagDigit):
    upper = ima_veliko_slovo(input_string)
    lower = ima_malo_slovo(input_string)
    digit = ima_broj(input_string)
    if len(input_string) > min_string_len and flagUpper == upper and flagLower == lower and flagDigit == digit:
        return True
    else:
        return False
# print(check_password('Passw123', 7, True, False, True))
# 101.
def vreme_do_autobusa(vreme):
    sat, min = map(int, vreme.split(':'))
    minuti = sat * 60 + min
    autobus = 6 * 60
    vreme_do = autobus - minuti - 5
    return max(vreme_do, 0)
# print(vreme_do_autobusa('05:00'))
# 102.
def vrata(n):
    vrata = [False] * n
    
    for i in range(1, n):
        for j in range(1, n):
            if j % i == 0:
                vrata[j] = not(vrata[j])
    otvorena = 0
    for i in range(1, n):
        if vrata[i] == 1:
            otvorena += 1

    return otvorena
# print(vrata(5))




'''ChatGPT izrada zadataka 80., 76. '''
def razlika_skokova(skokovi):
    if not skokovi:
        return 0
    
    najkraci_skok = min(skokovi)
    najduzi_skok = max(skokovi)
    
    razlika = najduzi_skok - najkraci_skok
    
    return razlika
def zamijeni_element(list, stari_element, novi_element):
    for i in range(len(list)):
        if list[i] == stari_element:
            list[i] = novi_element

# Primjer korištenja
# skokovi = [3, 7, 2, 8, 4, 10]
# razlika = razlika_skokova(skokovi)
# print("Razlika između najdužeg i najkraćeg skoka je:", razlika)


