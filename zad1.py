#zad1

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
        else:
            print("FAil")

    def get_titl(self):
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
        
    
        


lista_art = []
def provjera_titla(titl):
    provjera = 1
    if len(titl) < 50 and titl[0] != " ":
        lista_titl = titl.split()
        for elem in lista_titl:
            if elem.isalpha() != True:
                print('Nevalidan unos!')
                provjera = 0
                return provjera
        for i in lista_art:
            if i.get_titl() == titl:
                print('Titl vec postoji!')
                provjera = 0
                return provjera 
    else:
        provjera = 0       
    return provjera

def provjera_autora(autor):
    provjera = 1
    if len(autor) < 100 and autor[0] != " ":
        lista_autor = autor.split()
        for elem in lista_autor:
            if elem.isalpha() != True:
                print("Nevalidan unos!")
                provjera = 0
    return provjera

def provjera_opisa(opis):
    provjera = 1
    if 0 > len(opis) > 500:
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
#zad2
class TechArticle(Article):
    def __init__(self, title, author, description, creation_date, lang, views = 0, comments = [], category = 'Tech'):
        super().__init__(title, author, description, category, views, comments)
        self.__creation_date = creation_date
        self.__lang = lang

    def set_creation_date(self, datum):
        self.__creation_date = provjera_datuma(datum)
    def set_lang(self, jezik):
        if provjera_jezika(jezik)==1:
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
    for (count, i) in enumerate(pom_lista):
        if count < 2:
            if int(pom_lista[i]) < 10:
                pom_lista[i] == "0" + pom_lista[i]
        else:
            break
    return datum
def provjera_jezika(jezik):
    if jezik_lista.count(jezik):
        return 1
    else:
        return 0
a = TechArticle("ghgh","autor", "description","11/11/2010", "en", 2, [['asdaqwert','aaa']] )
print(a.get_category())

'''
i = 0
while 1:
    lista_art[i] = Article()
    lista_art[i].set_title("ZA DAS")
    lista_art[i].set_author("MARKO MArkovic")
    lista_art[i].set_desc("werwer werewr")
    lista_art[i].set_category("knjizurina")
    lista_art[i].set_views(42)
    lista_art[i].set_comments("komentar")
    break

print(lista_art[0]._Article__views)

lista_art.append(Article("ghgh","autor", "description", "kategorija", 2, [['asdaqwert','aaa']]))
print(lista_art[1].get_comments())
lista_art[1].set_comments(["Andrea","iiii","lalalal"])
lista_art[1].insert_new_comment(["Andrea1","iiii1","lalalal1"])
print(lista_art[1].get_comments())
print(lista_art[1].get_comments_by_author("iiii12"))
'''
print("AAA")