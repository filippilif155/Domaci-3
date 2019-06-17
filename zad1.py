class Article:
    def __init__(self, title = "AAA", author = "Marko Markovic", description = "Ako sa sada ja da sam ja da sam ja...", category = "blokblok", views = 0, comments = ""):
        self.__title = title
        self.__author = author
        self.__description = description
        self.__category = category
        self.__views = views
        self.__comments = comments
    def set_title(self, titl):
        if  provjera_titla(titl) == 1:
            self.__title = titl
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
        if provjera_komentara == 1:
            self.__comments.append(komentar)

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

    def insert_new_comment(self, titl, autor = "Anonim", opis):
        komentar = [titl, autor, opis]
        if provjera_komentara == 1:
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
        diction = {'title':'Titl ne postoji!'}
        for elem in self.__comments:
            if elem[0] == titl:
                diction['title'] = [elem[1], elem[2]]
                break
        return diction
    def get_comments_by_author (autor):
        lista_komentara = []
        greska = "Trazeni autor ne postoji!"
        for elem in self.__comments:
            if elem[1] == titl:
                lista_komentara.append(elem)
        if len(lista_komentara) != 0:
            return lista_komentara
        else:
            return greskaw
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

