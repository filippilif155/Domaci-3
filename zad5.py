def zeljeni_dict(lista):
    zeljeni_dictionary = {}
    for elem in lista:
        zeljeni_dictionary.update({elem["country"]:elem["spent"]})
    return zeljeni_dictionary
 
pocetna_lista = [
    {
      "country": "GB",
      "spent": 100
    },
    {
      "country": "RU",
      "spent": 200
    }
]
print(zeljeni_dict(pocetna_lista))