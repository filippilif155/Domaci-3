#ZAD1 ----------------------------------------------------------------------------------------------------------------

class Article:
    def __init__(self, title, author, description, category, views = 0, comments = []):
        self.__title = title
        self.__author = author
        self.__description = description
        self.__category = category
        self.__views = views
        self.__comments = comments
    def set_title(self, titl):
        if  provjera_titla(titl) == 1:
            self.__title = titl
            print(self.__title)
    def set_author(self, autor):
        if  provjera_autora(autor) == 1:
            self.__author = autor
    def set_desc(self, desc):
        if  provjera_opisa(desc) == 1:
            self.__description = desc
    def set_category(self, kat):
        if  provjera_kategorije(kat) == 1:
            self.__category = kat
    def set_views(self, pregled):
        if provjera_ocjene(pregled) == 1:
            self.__views = pregled
    def set_comments(self, komentar):
        if provjera_komentara(komentar) == 1:
            self.__comments = [komentar]

    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_desc(self):
        return self.__description
    def get_category(self):
        return self.__category
    def get_comments(self):
        return self.__comments
    def get_views(self):
        return self.__views

    def insert_new_comment(self, komentar):
        if provjera_komentara(komentar) == 1:
            self.__comments.append(komentar)
    def delete_comment_by_title(self, titl):
        for elem in self.__comments:
            if elem[0] == titl:
                self.__comments.remove(elem)
    def delete_comment_by_author(self, autor):
        for elem in self.__comments:
            if elem[1] == autor:
                del elem
    def get_comment_by_title (self, titl):
        diction = {}
        pokazivac=0
        for elem in self.__comments:
            if elem[0] == titl:
                pokazivac=1
                diction[titl] = [elem[1], elem[2]]
                break
        if pokazivac==0:
            return "Nema titla "
        else:
            return diction
    def get_comments_by_author (self, autor):
        lista_komentara = []
        greska = "Trazeni autor ne postoji!"
        for elem in self.__comments:
            if elem[1] == autor:
                lista_komentara.append(elem)
        if len(lista_komentara) != 0:
            return lista_komentara
        else:
            return greska
    def inc_views(self, br_pregleda = 0):
        if provjera_ocjene == 1:
            self.__views = self.__views + br_pregleda
    def __str__(self):
        diction = {'title':self.__title,'author':self.__author,'description':self.__description,'category':self.__category,'views':self.__views,'comments': len(self.__comments)}
        #tr_string = "title" + ':' + self.__title + ','  'author' + ':' + self.__author + ',' +  'description' + ':' + self.__description + ',' + 'category' + ':' + self.__category + ',' + 'views' + ':' + str(self.__views) + ',' + 'comments' + ':' + str(len(self.__comments))}
        #return tr_string
        return diction
        
    
        


def provjera_titla(titl):
    provjera = 1
    if len(titl) < 50 and titl.isspace() == False:
        lista_titl = titl.split()
        for elem in lista_titl:
            if elem.isalpha() != True:
                print('Nevalidan unos!')
                provjera = 0
                return provjera
        for i in lista_art:
            if i.get_title() == titl:
                print('Titl vec postoji!')
                provjera = 0
                return provjera 
    else:
        provjera = 0 
        print("Nevalidan unos!")      
    return provjera

def provjera_autora(autor):
    provjera = 1
    if len(autor) < 100 and autor.isspace() == False:
        lista_autor = autor.split()
        for elem in lista_autor:
            if elem.isalpha() != True:
                print("Nevalidan unos!")
                provjera = 0
    else:
        provjera = 0
        print("Nevalidan unos!")      
    return provjera

def provjera_opisa(opis):
    provjera = 1
    if len(opis) == 0 or len(opis) > 500:
        print("Nevalidan unos!")
        provjera = 0
    return provjera

def provjera_kategorije(kat):
    provjera = 1
    if 0 > len(kat) > 20:
        print("Nevalidan unos!")
        provjera = 0
    return provjera

def provjera_ocjene(ocjena):
    provjera = 1
    try:
        int(ocjena)
    except:
        ValueError
        print("Nevalidan unos!")
        provjera = 0
    return provjera
def provjera_komentara(komentar):
    provjera = 1
    if len(komentar) == 3:
        if len(komentar[0]) > 50 or len(komentar[1]) > 50 or len(komentar[2]) > 120:
            provjera = 0 
            print("Nevalidan unos!")
    else:
        provjera = 0
        print("Nevalidan unos!")
    return provjera
#ZAD2 ---------------------------------------------------------------------------------------------------------------
class TechArticle(Article):
    def __init__(self, title, author, description, creation_date, lang, views = 0, comments = [], category = 'Tech'):
        super().__init__(title, author, description, category, views, comments)
        self.__creation_date = creation_date
        self.__lang = lang

    def set_creation_date(self, datum):
        self.__creation_date = provjera_datuma(datum)
    def set_lang(self, jezik):
        if provjera_jezika(jezik) == 1:
            self.__lang=jezik
    def get_creation_date(self):
        return self.__creation_date
    def get_lang(self):
        return self.__lang
    def get_comments_by_therm(self, trm):
        lista_trmova = []
        for i in self.__comments:
            if i[0].startswith(trm):
                lista_trmova.append(i)
        return tuple(lista_trmova)
    def __str__(self):
        diction = {'title':self.__title,'author':self.__author,'description':self.__description,'category':self.__category,'views':self.__views,'comments': len(self.__comments), 'creation_date': self.__creation_date,'lang': self.__lang}
        stri = str(diction)[1:len(str(diction))]
        return stri

jezik_lista=["en", "rs"] 
def provjera_datuma(datum):
    pom_lista = datum.split("/")
    for (count, k) in enumerate(pom_lista):
        if count < 2:
            if k[0] != '0':
                if int(k) < 10:
                    pom_lista[count] = "0" + k
    datum_dva = pom_lista[0] + '/' + pom_lista[1] + '/' + pom_lista[2]
    return datum_dva
def provjera_jezika(jezik):
    if jezik_lista.count(jezik):
        return 1
    else:
        return 0
#ZAD3 ----------------------------------------------------------------------------------------------------------------
lista_art = []
lista_kategorija = ["Tech", "Culture", 'World']
global i 
i = 0
broj_techart = 0
broj_art = 0
while 1:
    while 1:
        kategorija_unos = input(f"Unesite neku od kategorija {lista_kategorija}:\n")
        if lista_kategorija.count(kategorija_unos):
            break
        else:
            print('Nevalidan unos!')
            continue
    while 1:
        unos_titla = input('Unesite titl vaseg artikla (od 1-50 slova):\n')
        if provjera_titla(unos_titla):
            break
        else:
            continue
    while 1:
        unos_autora = input('Unesite ime autora (od 1-100 slova):\n')
        if provjera_autora(unos_autora):
            break
        else:
            continue
    while 1:
        unos_opisa = input('Unesite opis (od 1-500 karaktera):\n')
        if provjera_opisa(unos_opisa):
            break
        else:
            continue
    while 1:
        unos_pregleda = input('Unesite broj pregleda (nije obavezno):\n')
        if provjera_ocjene(unos_pregleda):
            break
        else:
            continue
    if kategorija_unos != "Tech":
        lista_art.append(Article(unos_titla, unos_autora, unos_opisa, kategorija_unos, unos_pregleda))
        broj_art += 1
    else:
        lista_art.append(TechArticle(unos_titla, unos_autora, unos_opisa, '', '', unos_pregleda))
        broj_techart += 1
        while 1:
            unos_datuma = input("Unesite datum kreacije u obliku dd/mm/yyyy:\n")
            if provjera_datuma(unos_datuma):
                lista_art[i].set_creation_date(unos_datuma)
                break
            else:
                print("Nevalidan unos!")
                continue
        while 1:
            unos_lang = input("Unesite neki od jezika (en, rs):\n")
            if provjera_jezika(unos_lang):
                lista_art[i].set_lang(unos_lang)
                break
            else:
                print("Nevalidan unos!")
                continue
    i += 1
    if broj_art >= 1 and broj_techart >= 0:
        jos_art = input("Da li zelite da unesete jos artikala? y/n \n")
        if jos_art != 'y':
            break
for i in lista_art:
    print(i.get_title())
    print(i.get_author())
    print(i.get_desc())
    print(i.get_comments())
    print(i.get_views())
    print(i.get_category())
    if i.get_category() == "Tech":
        print (i.get_creation_date())
        print(i.get_lang())
    print('\n')
#unos komentara
y_n = input("Zelite li da unesete komentar? y/n \n")
while y_n == 'y':
    provjera = 0
    titl = input('Unesite titl zeljenog artikla:\n')
    for elem in lista_art:
        if elem.get_title() == titl:
            titl_komentara = input('Unesite titl (ne vise od 50 karaktera):\n')
            autor_komentara = input('Unesite autora (ne vise od 50 karaktera):\n')
            sadrzina = input('Unesite sadrzaj komentara (ne vise 0d 120 karaktera):\n')
            komentar = [titl_komentara, autor_komentara, sadrzina]
            if provjera_komentara(komentar):
                elem.insert_new_comment(komentar)
                provjera = 1
                break
    if provjera == 0:
        print("Pokusajte ponovo!")
    else:
        print('Uspjesno unijet komentar!')
    y_n = input('Zelite li da unesete komentar? y/n \n')
#filtriranje po kategoriji
while 1:
    kategorija = input(f"Unesite po kojoj lategoriji zelite filtriranje {lista_kategorija} :\n")
    if lista_kategorija.count(kategorija) == 0:
        print("Nevalidan unos!")
        continue
    lista_filtriranja = list(filter(lambda x: x.get_category() == kategorija, lista_art))
    lista_filtriranja_po_pregledima = sorted(lista_filtriranja, key = lambda x: x.get_views(), reverse = True)
    lista_filtriranja_po_broju_komentara = sorted(lista_filtriranja, key = lambda x: len(x.get_comments()), reverse = True)
    f = open(f"{kategorija}_sorted_by_views.txt", "w")
    for elem in lista_filtriranja_po_pregledima:
        print(elem.get_title(),';',elem.get_author(), ';', elem.get_desc(), ';', file = f)
        brojac = 0
        while brojac < len(elem.get_comments()):
            print(elem.get_comments()[brojac],'|', file = f)
            brojac += 1
        print(elem.get_comments()[brojac - 1],';', elem.get_views(), '\n', file = f)
    f.close()
    f_a = open(f"{kategorija}_sorted_by_comments.txt", "w")
    for elem in lista_filtriranja_po_broju_komentara:
        print(elem.get_title(),';',elem.get_author(), ';', elem.get_desc(), ';', file = f_a)
        brojac = 0
        while brojac < len(elem.get_comments()):
            print (elem.get_comments()[brojac],'|', file = f_a)
            brojac += 1
        print (elem.get_comments()[brojac - 1],';', elem.get_views(), '\n', file = f_a)
    f_a.close()
    break
            

for i in lista_filtriranja_po_pregledima:
    print(i.get_title())
    print(i.get_author())
    print(i.get_desc())
    print(i.get_comments())
    print(i.get_views())
    print(i.get_category())
    if i.get_category() == "Tech":
        print (i.get_creation_date())
        print(i.get_lang())
    print('\n\n')
