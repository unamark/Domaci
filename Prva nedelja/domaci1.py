import math  
import random

#1. Napisati program koji racuna površinu i obim pravougaonika

def prvi():
    a = 2
    b = 3
    povrsina = a*b
    obim = 2*a+2*b

    print(f'Povrsina = {povrsina}\nObim = {obim}.')

#2. Napisati program koji koristi tri varijable a, b i c, a racuna vrijednosti x1 i x2 kvadratne
#jednacine ax^2 + bx + c = 0. Zanemariti slučaj negativnih vrijednosti ispod korijena
#(kompleksni brojevi).

def drugi(a,b,c):
    D = b**2 - 4*a*c
    x1 = (-b + math.sqrt(D)) / 2*a
    x2 = (-b - math.sqrt(D)) / 2*a
    
    print(f'x1 = {x1}, x2 = {x2}')

#3. Napisati program koji racuna razliku kvadrata.
def razlika_kvadrata(a,b):
    resenje = (a + b) * (a - b)
    return resenje 

#4. Sportista se na početku treninga zagrijeva tako što trči po ivicama pravougaonog terena
#dužine d i širine s. Napisati program kojim se određuje koliko metara pretrči sportista dok
#obiđe teren 4 puta
def sportista(d, s):
    pretrci = 4 * (2 * d + 2 * s)
    
    print(f'Sportista pretrci {pretrci} metara.')

#5. Napisati program koji na osnovu zadate širine i visine lista papira (pravougaonog oblika)
#u milimetrima određuje njegovu površinu u kvadratnim centimetrima
def povrsina_u_cm(sirina, visina):
    s = sirina / 10
    v = visina / 10
    povrsina = v * s
    return povrsina

# 6. Napisati program koji racuna kvadrat trinoma(a, b, c) koja za unijete parametre a, b i c
# računa kvadrat trinoma za unešene parametre. Formula: 𝑎^2 + 𝑏^2 + 𝑐^2 + 2𝑎𝑏 + 2𝑎𝑐 +
# 2𝑏c
def trinom(a, b, c):
    resenje = a**2 + b**2 + c**2 + 2*a*b + 2*a*c + 2*b*c
    return resenje

# 7. Marko voli biciklizam. Pošto Marko zna da je važno biti hidratizovan, pije vodu na svakih
# sat vremena vožnje bicikla i to pola litara vode. Kao ulaz poznato je vrijeme u satima, a
# treba štampati broj litara koje će Marko popiti, zaokruženo na najmanju vrijednost (donje
# cijelo).
# Primjer: time = 3 ----> litara = 1; time = 6.7---> litara = 3 ; time = 11.8--> litara = 5
def hidratizovan(vreme):
    #vreme // 2 ili vreme*0.5//1 
    litara = math.floor(vreme*0.5)
    print(f'popice {litara}l vode nakon {vreme}h.')

# 8. Napisati program kojim se izračunava potrebna dužina trake za ivicu stoljnjaka kružnog
# oblika čija je površina P
def traka(p):
    r = math.sqrt(p / math.pi)
    obim = 2* r * math.pi
    print(f'Potrebno je {obim} trake.')

# 9. Fudbalski teren dimenzija d×s treba ograditi pravougaonom ogradom tako da je
# rastojanje stranica ograde od linije terena r. Napiši program koji određuje dužinu ograde
def ograda():
    d = float(input("d = "))
    s = float(input("s = "))
    r = float(input("r = "))
    duzina = 2*(d + 2*r) + 2*(s + 2*r)

    print(f'Duzina ograde je {duzina}')


# 10. Date su koordinate donje desne(x1,y1) i gornje lijeve(x2,y2) ivice zida (pravougaonik). Izračunati
# povrsinu i obim zida

def zid(x1, y1, x2, y2):

    obim = 2*(x2 - x1) + 2*(y2 - y1)
    povrsina = (x2 - x1) * (y2 - y1)
    
    print(f'Povrsina zida je {povrsina}, a obim {obim}.')

# 11. Napisati program za euclide_distance((x1, x2), (y1, y2)) kojom se računa i vraća
# euklidsko rastojanje izmedju dvije tacke A i B. Tacka A par (x1, y1), dok je tačka B par
# (x2, y2)
def euclid_distance(x1, y1, x2, y2):
    razdaljina = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    return razdaljina

def euclid2(x1, y1, x2, y2):
    a = [x1, y1]
    b = [x2, y2]
    return math.dist(a, b)


# 12. Kreirati algoritam koji računa koje godine je rođen Miloš ukoliko je poznato da danas ima
# N godina.
def godiste(N):
    return 2024 - N

# 13. Zamislite da ste dobili tajanstveno pismo sa mapom i uputstvima za pronalaženje
# skrivenog blaga. Uputstva su sljedeća: "Trebate da krenete od starog hrasta koji ima
# sledeću poziciju G (x1,y1). Onda trebate ići pravo do stare kuće koja se nalazi na poziciji
# K(x2,y2). Blago je zakopano u susjedstvu, gdje se nalazi kuća, i to desno od pozicije
# kuće za dvije pozicije, i ispod za tri pozicije.
# a. Izračunajte koordinate blaga.
# b. Izračunajte (vazdušno) rastojanje od hrasta do blaga.
# c. Izračunajte rastojanje od hrasta do blaga tako da morate obići i kuću.
def blago(x1,y1,x2,y2):
    #a)
    blago_x = x2 + 2
    blago_y = y2 - 3
    print(f'Koordinate blaga su ({blago_x},{blago_y}).')
    #b)
    rastojanje_v = math.dist([x1,y1],[blago_x, blago_y])
    print(f'Rastojanje izmedju hrasta i blaga je {rastojanje_v}.')
    #c)
    hr_ku = math.dist([x1,y1],[x2, y2])
    ku_bl = math.dist([x2,y2],[blago_x, blago_y])
    rastojanje = hr_ku + ku_bl
    print(f'Rastojanje je {rastojanje}.')


# 14. Kreirati program za procjenu cijene stana. Na ukupnu cijenu najviše utiču sledeći
# parametrI: njegova veličina, lokacija (5 puta više nego veličina) i dostupnost parkinga (10
# puta više nego lokacija). Cijena kvadrata je 1200e. Fiksna cijena učešća je 1000e. Sve
# vrijednosti varijabli se mogu pretvoriti u numeričke. (parking ima = 1, parking nema = 0;
# zona 1 = 3, zona 2 =2, zona 3 = 1)
def cena_stana(vel, zona, park):
    velicina = vel * 1200 
    if(zona == 'zona 1'):
        lokacija = 3
    elif(zona == 'zona 2'):
        lokacija = 2
    elif(zona == 'zona 3'):
        lokacija = 1 

    if(park == 'ima'):
        parking = 1
    elif(park == 'nema'):
        parking = 0   

    ukupno = velicina + 5 * lokacija + 10*5*parking + 1000

    print(f'Procenjena vrednost stana je {ukupno}€.')


# 15. Napiši program koji izračunava površinu trougla ako su poznate koordinate njegovih
# tjemena. (pomoc: Heronov obrazac i euklidsko rastojanje)
def trougao(x1,y1,x2,y2,x3,y3):
    a = math.sqrt((x2-x1)**2+(y2-y1)**2)
    b = math.sqrt((x2-x3)**2+(y2-y3)**2)
    c = math.sqrt((x3-x1)**2+(y3-y1)**2)
    s = (a + b + c) /2
    povrsina = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f'Povrsina trougla je {int(povrsina)}.')


# 16. Ako je cijena taksija za jedan kilometar 0.5e, a početna cijena je 1e, napisati kod koji za
# unijeti broj pređenih kilometara računa cijenu vožnje.
def taksi(kilometri):
    cena = 1 + kilometri * 0.5
    print(f'Cena voznje je za {kilometri}km je {cena}€.')

# 17. Knjižara "Bukvarnica" je posebno mjesto gdje svaka knjiga ima svoju priču. Kako bi
# proslavili dolazak novog godišnjeg doba, knjižara je odlučila da uvede popust - svaka
# knjiga dobija popust koji se može otkriti samo uz pomoć programa. Kao pomoćnik u
# knjižari, vaš zadatak je da kreirate program koji će izračunati konačnu cijenu knjige
# nakon primijenjenog popusta.
def knjizara(cena_knjige, popust):
    konacna_cena = cena_knjige - cena_knjige * popust / 100

def knjizara2(cena_knjige):
    popust = random.randint(0,100)
    konacna_cena = cena_knjige - cena_knjige * popust / 100  
    print(f'Konacna cena knjige je {konacna_cena}€ sa {popust}% popusta.')

# 18. Cijena konzole za igre PlayStation 5 je prvo porasla 10%, pa je smanjena 10%. Ako je
# poznata početna cijena konzole, napisati program koji određuje cijenu nakon tih
# promjena.
def igra(cena):
    porasla = cena + cena*10/100
    # print(porasla)
    smanjila = porasla - porasla*10/100
    # print(smanjila)
    print(f'Cena PlayStation-a 5 nakon poslednje promene je {smanjila}€.')

# 19. Napisati program koji za zadati trocifreni broj računa zbir cifara tog broja.
def trocifreni(br):
    broj = br
    j = broj % 10
    broj = broj // 10
    d = broj % 10
    s = broj // 10

    zbir = j + d + s
    print(f'Zbir cifara broja {br} je {zbir}.')

# 20. Dobili ste zadatak da dešifrujete kod kojim se otvaraju tajna vrata. Otkrili ste da na
# osnovu poznatog trocifrenog broja možete pronaći kod koji otvara tajna vrata tako što od
# proizvoda cifara tog broja oduzmete zbir cifara istog broja.
def desifrovati(broj):
    br = broj
    j = br % 10
    br = br // 10
    d = br % 10
    s = br // 10
    proizvod = s*d*j
    zbir = s+d+j
    sifra = proizvod - zbir
    print(f'Sifra je {sifra}.')

# 21. Otkrili ste algoritam kojim možete doći do šifre koja otvara sef. U sefu se nalazi knjiga
# koja krije tajne o nastanku univerzuma. Šifra se dobija kada se od kvadrata zbira prve i
# poslednje cifre četvorocifrenog broja oduzme razlika kvadrata druge i trece cifre.
def sef(broj):
    br = broj
    j = br % 10
    br = br // 10
    d = br % 10
    br = br // 10
    s = br % 10
    h = br // 10

    sifra = (h + j)**2 - razlika_kvadrata(s,d)
    #s = (h**2 + 2*h*j + j**2) - ((s+d)*(s-d))
    print(f'Sifra je {sifra}.')

# 22. Na takmičenju iz matematike učestvovalo je N učenika. Izveštaj o broju poena
# odštampan je na dvije strane. Nastavnik greškom nije ponio prvu stranu izveštaja, ali se
# sjeća da je na dnu strane pisalo da je prosječan broj poena za tu stranu bio p1. Na
# drugoj strani (koju ima kod sebe) su podaci o K učenika i prosječan broj poena za tu
# stranu je p2. Napisati program kojim se određuje koliki je prosječan broj poena svih
# učenika.
def poeni(n,k,p1,p2):
    # n = int(input('Ukupan broj ucenika: '))
    # k = int(input('Broj ucenika na 2. strani: '))
    # p1 = float(input('Prosecan broj poena ucenika na 1. strani: '))
    # p2 = float(input('Prosecan broj poena ucenika na 2. strani: '))

    poena_uk = (n-k)*p1 + k*p2
    prosek = poena_uk / n
    print(f'Prosecan broj poena svih ucenika je {round(prosek, 2)}.')

# 23.Napisati program koji za unijete parametre a i b vraća srednju vrijednost.
# Npr. ako je a = 2, b = 3, rezultat funkcije treba da bude 2.5. Ako je a = -2, b = 4,
# rezultat treba da bude 1. Ako je a = -4, b = 2, rezultat treba da bude - 1.
def srednja_vr(a,b):
    srednja_vrednost = (a+b) / 2
    return srednja_vrednost

# 24.Za Milicu i Anu se čuva koliko puta su obišle teren u 40 minuta. Međutim,
# prilikom unosa podataka desila se zabuna, pa je u varijabli x sačuvana vrijednost
# koja je trebala biti sačuvana u varijabli y i obrnuto. Napisati kod koji mijenja
# mjesta vrijednostima u promjenljivim x i y. Npr. ako je x = 7 i y = 10, poslije
# izvršavanja koda treba da bude x=10 i y=7.
def zamena(x,y):
    tmp = x
    x = y
    y = tmp
    print(f'x = {x} y = {y}')

# 25.Dato je rastojanje u centimetrima između ulaza u dvije različite kancelarije.
# Odrediti koliko cijelih metara ima u tom rastojanju. Npr. 324cm imaju 3 metra.
def cm_m(centimetara):
    metara = centimetara // 100
    print(f'Rastojanje je {metara}m.') 

# 26.Dat je četvorocifreni prirodan broj koji predstavlja broj stambene jedinice u
# zgradi. Na osnovu zadatog broja potrebno je odrediti sprat na kome se nalazi
# stambena jedinica. Poznato je da se to može otkriti iz pretposlednje cifre zadatog
# broja.
def stan(broj):
    tmp = broj
    sprat = tmp//10%10
    print(f'Stan broj {broj} se nalazi na {sprat}. spratu.')

# 27.Dat je četvorocifreni prirodan broj. Napisati kod koji štampa kvadrat zbira cifara
# tog broja.
def kvadrat_zbira_cifara(broj):
    br = broj
    j = br % 10
    br = br // 10
    d = br % 10
    br = br // 10
    s = br % 10
    h = br // 10
    zbir = h+s+d+j
    return zbir**2

# 28.Dat je trocifren broj. Odrediti broj koji se dobija zamjenom prve i posljednje cifre.
def novi_broj(broj):
    j = broj % 10
    broj = broj // 10
    d = broj % 10
    s = broj // 10
    novi = j*100 + d*10 + s
    return novi


# 29.Korisnik unosi koordinate dvije tačke (x1, y1) i (x2, y2) koje predstavljaju početne
# tačke dva studenta koji su se dogovorili da se sretnu na lokaciji (x3, y3) koja je
# nalazi tačno na sredini njihovog puta. Program treba da odredi tu lokaciju i
# izračuna rastojanje od početne pozicije do tačke susreta, koristeći Euklidsko
# rastojanje.
def lokacija(x1, y1, x2, y2):
    #a = input([x1, y1])
    #b = input([x2, y2])

    x3 = (x1+x2)/2
    y3 = (y1+y2)/2

    rast1 = math.sqrt((x3-x1)**2+(y3-y1)**2)
    rast2 = math.sqrt((x3-x2)**2+(y3-y2)**2)

    print(f'Lokacija susreta: {x3,y3}.\nRastojanje 1. studenta od nje je {round(rast1,2)}, a drugog {round(rast2,2)}.')


# 30.Dimenzije pravougaonika su 543 i 130. Koliko kvadrata stranice 65 je moguće
# izrezati iz tog pravougaonika?
def kvadrati():
    v = 543
    s = 130
    a = 65
    moguce = v*s // (a**2)
    print(f'Moguce je iseci {moguce} kvadrata')

# 31.Napisati program koji računa površinu ekrana monitora pravougaonog oblika,
# ukoliko je poznata dužina njegove dijagonale (d = 50) i odnos stranica (aspect
# ratio = 16:9)
def ekran():
    d = 50
    s, v = 16,9
    x = (d**2 /s**2-v**2)**0.5
    a = s*x
    b=v*x
    print('Povrsina je ',a*b)

   

# 32.Dat je šestocifreni broj n (n=abcdef). Provjeriti da li važi a* c + 2 + f = b + d*e.
# Pomoć: razmisliti o provjeri uslova (boolean operator) - samostalno isprobati
# implementaciju iste u Python-u. Ovo ćemo svakako raditi tokom naredne
# sedmice
def sestocfreni(broj):
    br = broj
    f = br % 10
    br = br // 10
    e = br % 10
    br = br // 10
    d = br % 10
    br = br // 10
    c = br % 10
    br = br // 10
    b = br % 10
    a = br // 10

    if(a*c + 2 + f == b + d*e):
        return True
    else:
        return False
    
# 33.Napisati program koji provjerava koliko se poligona kvadratnog oblika i zadatih
# dimenzija može kreirati na jednoj poljani za koju su poznate njena širina i dužina.
def poligoni():
    s = 3   #dimenzije poljane
    d = 4
    a = 2   #dimenzija kvadratnog poligona
    moguce = s*d // (a**2)
    print(f'Moguce je kreirati {moguce} poligona')

# 34.Dobili ste zadatak da generišete specijalni identifikacioni broj za pristup tajnom
# laboratorijskom sektoru. Otkrili ste da se identifikacioni broj može dobiti na
# osnovu poznatog šestocifrenog broja tako što se kvadrira suma cifara tog broja,
# a zatim od tog rezultata oduzme proizvod treće i četvrte cifre istog broja. Kao
# rezultat prikazati identifikacioni broj.
def laboratorija(broj):
    br = broj
    f = br % 10
    br = br // 10
    e = br % 10
    br = br // 10
    d = br % 10
    br = br // 10
    c = br % 10
    br = br // 10
    b = br % 10
    a = br // 10
    suma  = a + b + c + d + e + f
    identif = suma**2 - c * d
    print(identif)


# 35.Dat je petocifreni prirodan broj koji predstavlja broj stambene jedinice u zgradi.
# Na osnovu zadatog broja potrebno je odrediti sprat na kome se nalazi stambena
# jedinica. Poznato je da se to može otkriti kada se na vrijednost srednje cifre
# zadatog broja doda vrijednost poslednje cifre. Štampati taj zbir.
def stambena_jedinica(broj):
    br = broj
    e = br % 10
    br = br // 10
    d = br % 10
    br = br // 10
    c = br % 10
    br = br // 10
    b = br % 10
    a = br // 10

    zbir = c + e
    print(zbir)




# prvi()
# drugi(2,9,5)
# print(razlika_kvadrata(2, 4))
# sportista(6, 2)
# print(povrsina_u_cm(160, 100))
# trinom(2, 3, 4)
# hidratizovan(11.8)
# traka(45)
# ograda()
# print(godiste(62))
# print(euclid_distance(3,3,6,12))
# print(euclid2(3,3,6,12))
# blago(3,3,6,12)
# cena_stana(80, 'zona 1', 'ima')
# taksi(3)
# trougao(-4,3,4,1,1,-2)
# knjizara(15,25)
# knjizara2(15)
# igra(50)
# trocifreni(625)
# desifrovati(625)
# sef(1235)
# poeni(80,30,78.20,89.30)
# print(srednja_vr(2,3))
# zamena(10,55)
# cm_m(325)
# stan(1245)
#print(kvadrat_zbira_cifara(1234))
#print(novi_broj(125))
# lokacija(2,3,3,1)
#kvadrati()
# print(sestocfreni(123456))
poligoni()
laboratorija(427811)
stambena_jedinica(45678)
    