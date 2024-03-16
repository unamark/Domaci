import random


# 1.
def get_words_ends_with_letter(string, slovo):
    recenice = string.split('.')
    lista_torki = []
    reci = []
    broj = 0

    for recenica in recenice:
        rec = recenica.split(' ')
        for r in rec:
            if r.endswith(slovo):
                reci.append(r)
                broj += 1
        reci.append(broj)
        if len(reci) > 1:
            lista_torki.append(tuple(reci))
        reci.clear()
        broj = 0
    return lista_torki


# print(get_words_ends_with_letter(
    # 'Print only the words that end with the chosen letter in those sentences. Example can contains one or more sentences.', 's'))

# 2.
def ponavljajuca_sekvenca(niz):
    sub = []
    proiz = 1
    max_p = 1
    m_sekv = []

    for i in range(len(niz)):
        for j in range(i + 1, len(niz)):
            proiz = niz[i]
            if niz[j] == niz[i]:
                sub = niz[i:j+1]
                proiz *= niz[j]
                if proiz > max_p:
                    max_p = proiz
                    m_sekv = sub
    return m_sekv, max_p


# print(ponavljajuca_sekvenca([1, 2, 2, 2, 4, 4]))

# 3.
def testerasti(niz):
    for i in range(len(niz)-1):
        if i % 2 == 0 and niz[i] > niz[i + 1]:
            return False

        elif i % 2 == 1 and niz[i] < niz[i + 1]:
            return False

    return True


def max_testerasti_podniz(niz):
    najduzi = []
    for i in range(len(niz)):
        for j in range(i+2, len(niz)):
            if testerasti(niz[i:j+1]):
                sub = niz[i:j+1]
                duzina = len(sub)
                # print(sub)
                if duzina > len(najduzi):
                    najduzi = sub

    return najduzi


# print(max_testerasti_podniz([1, 2, 3, 1, 5, 3, 1]))
# print(max_testerasti_podniz([0, 2, 1, 4, 3, 5]))


# 4.
def ponavljanje_susednih(string):
    maks = 0
    for i in range(len(string)):
        tmp = 0
        for j in range(i, len(string)):
            if string[i] == string[j]:
                tmp += 1
                if tmp > maks:
                    maks = tmp
            else:
                tmp = 0
    return maks


# print(ponavljanje_susednih('aabaaac'))

# 5.
def podkast(niz):
    najgori = ''
    los = 10000
    for film in niz:
        tmp = int(film['br_pozitivni']) / int(film['br_negativni'])
        if tmp < los:
            los = tmp
            najgori = film['naziv']
    return najgori


# print(podkast([{'naziv': 'Español para principiantes', 'br_pozitivni': 1000, 'br_negativni': 10}, {'naziv': 'Philophize This!', 'br_pozitivni': 500, 'br_negativni': 30}, {'naziv': 'Science VS. ',
    # 'br_pozitivni': 600, 'br_negativni': 45}]))


# 6.
class Televizor:
    def __init__(self):
        self._kanali = []
        self._broj_tekuceg_kanala = 0
        self._naziv_tekuceg_kanala = ''
        self._jacina_tona = 3

    def get_kanali(self):
        return self._kanali

    def set_kanali(self, novi_kanali):
        self._kanali = novi_kanali

    def get_broj_tekuceg_kanala(self):
        return self._broj_tekuceg_kanala

    def set_broj_tekuceg_kanala(self, br_kanala):
        if 0 <= br_kanala < len(self._kanali):
            self._broj_tekuceg_kanala = br_kanala
            # self._naziv_tekuceg_kanala = self._kanali[br_kanala]
        else:
            print('Nepostojeci broj kanala.')

    def get_naziv(self):
        return self._naziv_tekuceg_kanala

    def get_jacina_tona(self):
        return self._jacina_tona

    def set_jacina_tona(self, jacina):
        if 0 <= jacina <= 10:
            self._jacina_tona = jacina
        else:
            print('Neispravna jačina tona.')

    def get_info(self):
        print("Trenutni kanal:", self._naziv_tekuceg_kanala)
        print("Jačina tona:", self._jacina_tona)

    def dodaj_kanal(self, naziv):
        self._kanali.append(naziv)

    def obrisi_kanal(self, naziv):
        if naziv in self._kanali:
            self._kanali.remove(naziv)

    def pojacaj_ton(self):
        if self._jacina_tona < 10:
            self._jacina_tona += 1

    def ime_kanala(self, broj):
        if 1 <= broj <= len(self._kanali):
            return self._kanali[broj-1]
        else:
            print('Nepostojeci kanal.')


tv = Televizor()
tv.set_kanali(['Kanal 1', 'Kanal 2', 'Kanal 3'])
# tv.set_broj_tekuceg_kanala(1)
tv.set_jacina_tona(6)
# tv.get_info()
tv.pojacaj_ton()
# print(tv.get_jacina_tona())
# print(tv.obrisi_kanal('Kanal 2'))
# print(tv.get_kanali())
# print(tv.obrisi_kanal('Kanal 2'))


# 7.
class Book:
    def __init__(self, naslov, autor, godina, kopije):
        self._naslov = naslov
        self._autor = autor
        self._godina_izdanja = godina
        self._broj_kopija = kopije

    def get_naslov(self):
        return self._naslov

    def set_naslov(self, novi_naslov):
        self._naslov = novi_naslov

    def get_autor(self):
        return self._autor

    def set_autor(self, naziv_autora):
        self._autor = naziv_autora

    def get_godina_izdanja(self):
        return self._godina_izdanja

    def set_godina_izdanja(self, godina_izdanja):
        self._godina_izdanja = godina_izdanja

    def get_broj_kopija(self):
        return self._broj_kopija

    def set_broj_kopija(self, broj):
        self._broj_kopija = broj

    def get_info(self):
        return [self._naslov, self._autor, self._godina_izdanja, self._broj_kopija]


class Library():
    def __init__(self):
        self.__dostupne_knjige = []

    def dodaj_knjigu_rucno(self):
        naslov = input('Unesite naslov knjige: ')
        autor = input('Unesite autora knjige: ')
        godina = input('Unesite godinu izdanja knjige: ')
        kopije = input('Unesite broj kopija knjige u inventaru: ')
        knjiga = Book(naslov, autor, godina, kopije)
        self.__dostupne_knjige.append(knjiga)

    def dodaj_knjigu(self, knjiga):
        self.__dostupne_knjige.append(knjiga)

    def pregled_po_naslovu(self, naslov):
        lista = [
            knjiga.get_info() for knjiga in self.__dostupne_knjige if knjiga.get_naslov() == naslov]
        return lista

    def pregled_po_autoru(self, autor):
        lista = [
            knjiga.get_info() for knjiga in self.__dostupne_knjige if knjiga.get_autor() == autor]
        return lista

    def prikaz_trenutno_dostupnih(self):
        for knjiga in self.__dostupne_knjige:
            print(knjiga.get_info())

    def brisanje_knjige(self, naslov):
        for knjiga in self.__dostupne_knjige:
            if knjiga.get_naslov() == naslov:
                self.__dostupne_knjige.remove(knjiga)

    def uredi(self, naslov_knjige):
        akcija = input(
            'Unesite broj atributa koji zelite da izmenite.\n0 -> izmana naslova\n1 -> izmena autora\n2 -> izmena godine izdanja\n3 -> izmena broja kopija u inventaru')
        izmena = input('Unesite novu vrednost: ')
        for knjiga in self.__dostupne_knjige:
            if knjiga._naslov == naslov_knjige:
                if akcija == '0':
                    knjiga._naslov = izmena
                elif akcija == '1':
                    knjiga._autor = izmena
                elif akcija == '2':
                    knjiga._godina_izdanja = izmena
                elif akcija == '3':
                    knjiga._broj_kopija = int(izmena)


k1 = Book('1984', 'George Orwell', '1949.', 3)
k2 = Book('To Kill a Mockingbird', 'Harper Lee', '1960', 1)
k3 = Book('The Catcher in the Rye', 'J.D. Salinger', '1951', 18)
k4 = Book('The Great Gatsby', 'F. Scott Fitzgerald', '1925', 4)
k5 = Book('Tender Is the Night', 'F. Scott Fitzgerald', '1934', 7)
k6 = Book('This Side of Paradise', 'F. Scott Fitzgerald', '1920', 1)
k7 = Book('The Beautiful and Damned', 'F. Scott Fitzgerald', '1922', 19)
biblioteka = Library()
# biblioteka.dodaj_knjigu(k1)
# biblioteka.dodaj_knjigu(k6)
# biblioteka.dodaj_knjigu(k3)
# biblioteka.dodaj_knjigu(k7)
# biblioteka.dodaj_knjigu(k2)
# biblioteka.dodaj_knjigu(k4)
# biblioteka.prikaz_trenutno_dostupnih()
# biblioteka.brisanje_knjige('1984')
# biblioteka.prikaz_trenutno_dostupnih()
# print(biblioteka.pregled_po_autoru('F. Scott Fitzgerald'))
# biblioteka.dodaj_knjigu_rucno()
# biblioteka.uredi('1984')
# biblioteka.prikaz_trenutno_dostupnih()


# 8.
class Player:
    def __init__(self, x, y, width, height, health):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__health = health

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_width(self):
        return self.__width

    def set_width(self, sirina):
        self.__width = sirina

    def get_height(self):
        return self.__height

    def set_height(self, visina):
        self.__height = visina

    def get_health(self):
        return self.__health

    def set_health(self, zdravlje):
        if zdravlje < 0:
            self.__health = 0
        elif zdravlje > 100:
            self.__health = 100
        else:
            self.__health = zdravlje

    def decrease_health(self, steta):
        z = self.__health - steta
        if z < 0:
            self.__health = 0
        else:
            self.__health = z


class Enemy:
    def __init__(self, x, y, width, height, damage):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__damage = damage

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_width(self):
        return self.__width

    def set_width(self, sirina):
        self.__width = sirina

    def get_height(self):
        return self.__height

    def set_height(self, visina):
        self.__height = visina

    def get_damage(self):
        return self.__damage

    def set_damage(self, napad):
        if napad < 0:
            self.__damage = 0
        elif napad > 100:
            self.__damage = 100
        else:
            self.__damage = napad


def check_collision(player, enemy):
    p_levo_x = player.get_x()
    p_desno_x = player.get_x() + player.get_width()
    p_gore_y = player.get_y()
    p_dole_y = player.get_y() + player.get_height()

    e_levo_x = enemy.get_x()
    e_desno_x = enemy.get_x() + enemy.get_width()
    e_gore_y = enemy.get_y()
    e_dole_y = enemy.get_y() + enemy.get_height()

    if p_desno_x >= e_levo_x and p_levo_x <= e_desno_x and p_dole_y >= e_gore_y and p_gore_y <= e_dole_y:
        return True
    else:
        return False


def decrease_health(player, enemy):
    if check_collision(player, enemy):
        player.decrease_health(enemy.get_damage())


player1 = Player(200, 223, 50, 55, 100)
# print(player1.get_health())
# player1.set_health(120)
# print(player1.get_health())
# player1.set_health(-10)
# print(player1.get_health())
enemy1 = Enemy(200, 260, 40, 30, 60)
enemy2 = Enemy(150, 320, 85, 10, 85)
# print(check_collision(player1, enemy1))
# print(player1.get_health())
# decrease_health(player1, enemy1)
# print(player1.get_health())
# decrease_health(player1, enemy2)
# # print(player1.get_health())


# 9.


class Turnir:
    def __init__(self, naziv, runde):
        self.__lista_igraca = []
        self.__naziv_turnira = naziv
        self.__broj_igraca = 0
        self.__broj_rundi = runde

    def get_turnir(self):
        return self.__naziv_turnira

    def set_turnir(self, naziv):
        self.__naziv_turnira = naziv

    def get_igraci(self):
        return self.__lista_igraca

    def set_igraci(self, lista):
        self.__lista_igraca = lista
        self.__broj_igraca = len(lista)

    def get_runde(self):
        return self.__broj_rundi

    def set_runde(self, broj):
        if 0 < broj < 10:
            self.__broj_rundi = broj
        else:
            print('Neispravan broj.')

    def dodaj_igraca(self, ime_igraca):
        igrac = (ime_igraca, 0)
        self.__lista_igraca.append(igrac)
        self.__broj_igraca += 1

    def obrisi_igraca(self, ime_igraca):
        for igrac in self.__lista_igraca:
            if igrac[0] == ime_igraca:
                self.__lista_igraca.remove(igrac)
                print(f'Igrac {ime_igraca} je obrisan.')
                break

    def prikazi_najboljeg_igraca(self):
        if len(self.__lista_igraca) == 0:
            print('trenutno nema igraca na turniru.')
        else:
            # return self.__lista_igraca.sort(key=lambda x: x[1])[-1]
            naj = max(self.__lista_igraca, key=lambda x: x[1])
            return naj[0]

    def povecaj_bodove(self, igrac_ime):
        for i, (ime, bodovi) in enumerate(self.__lista_igraca):
            if ime == igrac_ime:
                self.__lista_igraca[i] = (ime, bodovi+1)
                break

    def pokreni_rundu(self):
        if self.__broj_igraca > 2:
            igrac1, igrac2 = random.sample(self.__lista_igraca, 2)

            if igrac1[1] > igrac2[1]:
                verovatnoca1 = 0.6
            else:
                verovatnoca1 = 0.4

            rezultat = random.random()

            if rezultat < verovatnoca1:
                pobednik = igrac1
                self.povecaj_bodove(igrac1[0])
            else:
                pobednik = igrac2
                self.povecaj_bodove(igrac2[0])

            self.__broj_rundi += 1
            print(
                f'pobednik duela {igrac1[0]} : {igrac2[0]} je {pobednik[0]}!')
        else:
            print('Nema dovoljno igraca na turniru.')


turnir = Turnir("Teniski turnir", 5)
turnir.dodaj_igraca('Novak Djokovic')
turnir.dodaj_igraca('Rafael Nadal')
turnir.dodaj_igraca('Danil Medvedev')
turnir.dodaj_igraca('Roger Federer')
turnir.dodaj_igraca('Jannik Sinner')
turnir.dodaj_igraca('Carlos Alcaraz')
# print(turnir.get_igraci())
# print(turnir.pokreni_rundu())
# print(turnir.prikazi_najboljeg_igraca())
# print(turnir.get_igraci())


# 10.
class Color:
    def __init__(self, red, green, blue):
        self.__red = red
        self.__green = green
        self.__blue = blue

    def get_red(self):
        return self.__red

    def set_red(self, red):
        if isinstance(red, int) and 0 <= red <= 255:
            self.__red = red
        else:
            print('Neispravan broj. Uneti celi broj izmedju 0 i 255.')

    def get_green(self):
        return self.__green

    def set_green(self, green):
        if isinstance(green, int) and 0 <= green <= 255:
            self.__green = green
        else:
            print('Neispravan broj. Uneti celi broj izmedju 0 i 255.')

    def get_blue(self):
        return self.__blue

    def set_blue(self, blue):
        if isinstance(blue, int) and 0 <= blue <= 255:
            self.__blue = blue
        else:
            print('Neispravan broj. Uneti celi broj izmedju 0 i 255.')

    def add_red(self, change):
        if change < 0 and self.__red + change >= 0:
            self.__red += change
        elif change > 0 and self.__red + change <= 255:
            self.__red += change
        else:
            print(
                'Vrednost ostaje nepromenjena. Doslo bi do ispadanja iz segmenta 0-255.')

    def add_green(self, change):
        if change < 0 and self.__green + change >= 0:
            self.__green += change
        elif change > 0 and self.__green + change <= 255:
            self.__green += change
        else:
            print(
                'Vrednost ostaje nepromenjena. Doslo bi do ispadanja iz segmenta 0-255.')

    def add_blue(self, change):
        if change < 0 and self.__blue + change >= 0:
            self.__blue += change
        elif change > 0 and self.__blue + change <= 255:
            self.__blue += change
        else:
            print(
                'Vrednost nepromenjena. Doslo bi do ispadanja iz segmenta 0-255.')

    def __lt__(self, color2):
        return self.__red < color2.__red and self.__green < color2.__green and self.__blue < color2.__blue

    def __eq__(self, color2):
        return self.__red == color2.__red and self.__green == color2.__green and self.__blue == color2.__blue

    def __gt__(self, color2):
        return self.__red > color2.__red and self.__green > color2.__green and self.__blue > color2.__blue

    def __str__(self):
        return f'red: {self.__red}, green: {self.__green}, blue: {self.__blue}'


boja1 = Color(15, 155, 46)
boja2 = Color(0, 0, 0)
boja3 = Color(255, 255, 255)
# boja1.set_green(5)
# print(boja1.add_blue(255))
# print(boja1)
# print(boja1 < boja3)
# print(boja2 > boja3)
# print(boja3 == boja3)
# print(boja3)


# 11.
class AlphaColor(Color):
    def __init__(self, red, green, blue, alpha):
        super().__init__(red, green, blue)
        self.__alpha = alpha

    def get_alpha(self):
        return self.__alpha

    def set_alpha(self, alpha):
        if isinstance(alpha, float) and 0 < alpha < 1:
            self.__alpha = alpha
        else:
            print('Uneti decimalnu vrednost izmedju 0 i 1.')

    def update_color_by_alpha(self, alpha):
        nova_red = self.get_red() - self.get_red() * alpha
        nova_green = self.get_green() - self.get_green() * alpha
        nova_blue = self.get_blue() - self.get_blue() * alpha

        self.set_red(int(nova_red))
        self.set_green(int(nova_green))
        self.set_blue(int(nova_blue))
        print(self)

    def __str__(self):
        return super().__str__() + f', alpha: {self.__alpha}'


boja4 = AlphaColor(15, 155, 46, 0.3)
boja5 = AlphaColor(0, 100, 0, 0.1)
boja6 = AlphaColor(255, 255, 255, 0.5)
# print(boja6)
# print(boja4.get_alpha(), boja4.get_blue())
# boja5.set_alpha(5)
# print(boja5)
# boja6.update_color_by_alpha(0.5)


# 12.
class Company:
    def __init__(self, name, area, balance, max_num_of_employees):
        self.__name = name
        self.__area = area
        self.__employees = []
        self.__balance = balance
        self.__max_num_of_employees = max_num_of_employees

    def get_name(self):
        return self.__name

    def set_name(self, novo_ime_kompanije):
        self.__name = novo_ime_kompanije

    def get_area(self):
        return self.__area

    def set_area(self, oblast_delovanja):
        self.__area = oblast_delovanja

    def get_balance(self):
        return self.__balance

    def set_balance(self, trenutni_finansijski_balans_kompanije):
        if trenutni_finansijski_balans_kompanije >= 0:
            self.__balance = trenutni_finansijski_balans_kompanije
        else:
            print('Unesena vrednost mora biti >= 0 !')

    def get_max_num_of_employees(self):
        return self.__max_num_of_employees

    def set_max_num_of_employees(self, maksimalno_zaposlenih):
        if maksimalno_zaposlenih >= 0:
            self.__max_num_of_employees = maksimalno_zaposlenih
        else:
            print('Unesena vrednost mora biti >= 0 !')

    def add_employee(self, employee):
        if len(self.__employees) + 1 <= self.__max_num_of_employees:
            self.__employees.append(employee)
            print('Zaposleni dodat.')
        else:
            print('Kompanija trenutno ne moze da primi nove zaposlene.')

    def remove_employee(self, employee_name, employee_surname):
        for i in range(len(self.__employees)):
            if self.__employees[i]['name'] == employee_name and self.__employees[i]['surname'] == employee_surname:
                self.__employees.pop(i)
                print('Zaposleni uklonjen.')
                break
        else:
            print(f'Nema zaposlenog sa {employee_name, employee_surname}.')

    def __str__(self):
        return f'name: {self.__name}, area: {self.__area}, balance: {self.__balance}'

    def can_pay_employees(self):
        placanje = sum(zaposleni['salary'] for zaposleni in self.__employees)

        if self.__balance >= placanje:
            return True
        else:
            return False

    def __gt__(self, kompanija_B):
        return len(self.__employees) > len(kompanija_B.__employees)


kompanija_A = Company('Coinis', 'ad-tech', 150000, 1000)
kompanija_B = Company('Google', 'tehnology', 5000, 1)
'''
kompanija_A.add_employee(
    {'name': 'Una', 'surname': 'Markovic', 'salary': 6600})
kompanija_A.add_employee({'name': 'John', 'surname': 'Doe', 'salary': 4500})
kompanija_A.add_employee(
    {'name': 'Alice', 'surname': 'Smith', 'salary': 16500})
kompanija_A.add_employee(
    {'name': 'Milica', 'surname': 'Bjelica', 'salary': 5500})
kompanija_A.add_employee(
    {'name': 'Taylor', 'surname': 'Swift', 'salary': 3500})

kompanija_B.add_employee(
    {'name': 'Sundrai', 'surname': 'Pichai', 'salary': 5500})
'''
# print(kompanija_B.can_pay_employees())
# print(kompanija_A > kompanija_B)
# print(kompanija_B)
# kompanija_A.remove_employee('Taylor', 'Swift')
# kompanija_B.add_employee({'name': 'Larry', 'surname': 'Page', 'salary': 5000})
# kompanija_B.set_max_num_of_employees(2)
# kompanija_B.add_employee({'name': 'Larry', 'surname': 'Page', 'salary': 5000})
# print(kompanija_A.get_balance())
# kompanija_A.set_balance(50000)
# print(kompanija_A.get_balance())
# print(kompanija_A)


# 13.
class Student:
    def __init__(self, ime, prezime, godina):
        self.__ime = ime
        self.__prezime = prezime
        self.__predmeti = []
        self.__godina = godina

    def get_ime(self):
        return self.__ime

    def set_ime(self, ime):
        self.__ime = ime

    def get_prezime(self):
        return self.__prezime

    def set_prezime(self, prezime):
        self.__prezime = prezime

    def get_godina(self):
        return self.__godina

    def set_godina(self, godina):
        if 0 < godina <= 8:
            self.__godina = godina
        else:
            print('Neodgovarajuca godina studija.')

    def insert_subject(self, predmet):
        self.__predmeti.append(predmet)

    def remove_subject(self, predmet):
        for i in self.__predmeti:
            if i['naziv'] == predmet:
                self.__predmeti.remove(i)
                print(f'Predmet {predmet} je obrisan.')
                break
        else:
            print(f'Predmet ne postoji, niste polozili {predmet}.')

    def compute_average(self):
        ukupan_broj_ostvarenih_kredita = 0
        suma = 0
        if len(self.__predmeti) == 0:
            return 0
        else:
            for predmet in self.__predmeti:
                ocena = predmet['ocena']
                if ocena == 'A':
                    suma += 10*predmet['broj_kredita']
                    ukupan_broj_ostvarenih_kredita += predmet['broj_kredita']
                elif ocena == 'B':
                    suma += 9*predmet['broj_kredita']
                    ukupan_broj_ostvarenih_kredita += predmet['broj_kredita']
                elif ocena == 'C':
                    suma += 8*predmet['broj_kredita']
                    ukupan_broj_ostvarenih_kredita += predmet['broj_kredita']
                elif ocena == 'D':
                    suma += 7*predmet['broj_kredita']
                    ukupan_broj_ostvarenih_kredita += predmet['broj_kredita']
                elif ocena == 'E':
                    suma += 6*predmet['broj_kredita']
                    ukupan_broj_ostvarenih_kredita += predmet['broj_kredita']
                else:
                    continue

            return round(suma/ukupan_broj_ostvarenih_kredita, 2)

    def __str__(self):
        return f'ime: {self.__ime}, prezime: {self.__prezime}, prosek: {self.compute_average()}'


student1 = Student('Ana', 'Jovanovic', 4)
'''student1.insert_subject(
    {'naziv': 'Engleski jezik 1', 'ocena': 'B', 'broj_kredita': 2})
student1.insert_subject(
    {'naziv': 'Programiranje 1', 'ocena': 'E', 'broj_kredita': 6})
student1.insert_subject({'naziv': 'Fizika', 'ocena': 'B', 'broj_kredita': 6})
student1.insert_subject(
    {'naziv': 'Periferije i interfejsi', 'ocena': 'A', 'broj_kredita': 6})
'''
# student1.set_ime('Goran')
# print(student1)

student2 = Student('Kosta', 'Zivkovic', 7)
# print(student2.compute_average())
'''student2.insert_subject(
    {'naziv': 'Engleski jezik 1', 'ocena': 'B', 'broj_kredita': 2})
student2.insert_subject(
    {'naziv': 'Programiranje 1', 'ocena': 'D', 'broj_kredita': 6})
student2.insert_subject(
    {'naziv': 'Programiranje 2', 'ocena': 'F', 'broj_kredita': 5})
student2.insert_subject(
    {'naziv': 'Arhitektura racunarskih sistema', 'ocena': 'B', 'broj_kredita': 7})
student2.insert_subject(
    {'naziv': 'Softver inzenjering', 'ocena': 'A', 'broj_kredita': 6})
student2.insert_subject(
    {'naziv': 'Kriptografija', 'ocena': 'A', 'broj_kredita': 4})'''
# print(student2.compute_average())
# student2.remove_subject('Programiranje 2')
# student2.set_godina(0)
# print(student2)


# 14.
class Drzava:
    def __init__(self, name, population, border, cities):
        self.__name = name
        self.__population = population
        self.__border = border
        self.__cities = cities

    def get_name(self):
        return self.__name

    def set_name(self, ime):
        self.__name = ime

    def get_population(self):
        return self.__population

    def set_population(self, broj_stanovnika):
        if broj_stanovnika > 0:
            self.__population = broj_stanovnika

    def get_border(self):
        return self.__border

    def set_border(self, granice):
        self.__border = granice

    def get_cities(self):
        return self.__cities

    def set_cities(self, gradovi):
        self.__cities = gradovi

    def add_border(self, nova_drzava):
        self.__border.append(nova_drzava)

    def grad_najmanje_stanovnika(self):
        if self.__cities:
            grad = min(self.__cities, key=lambda x: x['broj_stanovnika'])
            print('Grad sa najmanje stanovnika je: ', grad['naziv'])
        else:
            return None

    def grad_najvise_stanovnika(self):
        if not self.__cities:
            return None
        grad = max(self.__cities, key=lambda x: x['broj_stanovnika'])
        print('Grad sa najvise stanovnika je: ', grad['naziv'])

    def __str__(self):
        gradovi = [grad['naziv'] for grad in self.__cities]
        return f'Drzava: {self.__name}; Broj stanovnika: {self.__population}; Gradovi: {gradovi}.'


class Federacija(Drzava):
    def __init__(self, name, population, border, cities, countries):
        super().__init__(name, population, border, cities)
        self.__countries = countries

    def get_countries(self):
        return self.__countries

    def set_countries(self, drzave):
        self.__countries = drzave

    def __lt__(self, druga):
        return len(self.__countries) < len(druga.__countries)

    def __gt__(self, druga):
        return len(self.__countries) > len(druga.__countries)

    def __eq__(self, druga):
        return len(self.__countries) == len(druga.__countries)

    def __str__(self):
        drzave = [drzava for drzava in self.__countries]
        return f'Federacija: {self.get_name()}; Broj drzava: {len(self.__countries)}; Drzave: {drzave}.'


drzava1 = Drzava(
    'Crna Gora', 622781, ['Srbija', 'Hrvatska',
                          'Bosna i Hercegovina', 'Albanija'],
    [
        {'naziv': 'Podgorica', 'broj_stanovnika': 150977},
        {'naziv': 'Nikšić', 'broj_stanovnika': 58212},
        {'naziv': 'Pljevlja', 'broj_stanovnika': 19235},
        {'naziv': 'Herceg Novi', 'broj_stanovnika': 12343}
    ]
)
# drzava1.grad_najmanje_stanovnika()
# drzava1.grad_najvise_stanovnika()
# print(drzava1)
drzava2 = Drzava('Srbija', 7000000, ['Hrvatska', 'Bosna i Hercegovina'], [
                 {'naziv': 'Beograd', 'broj_stanovnika': 1500000}, {'naziv': "Novi Sad", 'broj_stanovnika': 500000}])
# print(drzava2)
# drzava2.add_border('Crna Gora')
# print(drzava2.get_border())
federacija1 = Federacija('Evropska unija', 500000000, ['Srbija', 'Hrvatska'], [{'naziv': 'Berlin', 'broj_stanovnika': 3500000}, {
    'naziv': 'Pariz', 'broj_stanovnika': 2200000}], ['Francuska', 'Nemacka'])
federacija2 = Federacija('Američka federacija', 50, [
                         'SAD', 'Kanada', 'Meksiko'], [], ['SAD', 'Kanada', 'Meksiko'])

# print(federacija2)
# print(federacija1.get_countries())
# print(federacija1 > federacija2)
