nazwa_pliku = "example1.txt"

def prt_softset(sf):
    for obj in sf:
        print (obj)

def load_softset():
    """
        Pobieranie wierszy.
    """
    softset = []
    for li in open(nazwa_pliku):
        obj = li.strip("\n").split(",")
        obj = [float(c) for c in obj]
        softset.append(obj)
    return softset

def wektor(v1, v2):
    """ Mnozenie wektora: sum(e1*w1+e2*w2...en*wn)
    """
    tmp = []
    for i in range(0, len(v1)):
        tmp.append(v1[i] * v2[i])
    return sum(tmp)

def wartosc_wazona(sf, waga):
    """Wybór na podstawie wagi
    Argumenty:
        sf: Tablica wartoci
        wagi:podane wagi
    Return:
        decyzja: Wybrany/a rzecz 
    """
    decyzja = []
    #kandydat,pos = np.dot(sf[0], waga), 0
    kandydat,pos = wektor(sf[0], waga), 0
    decyzja.append([kandydat, pos])
    #pos = 0

    for obj in sf[1:]:
        pos += 1
        #wybrana_wartosc = np.dot(obj, waga)
        wybrana_wartosc = wektor(obj, waga)
        if  wybrana_wartosc > decyzja[0][0]:
            decyzja = []
            decyzja.append([wybrana_wartosc, pos])
        elif wybrana_wartosc == decyzja[0][0]:
            decyzja.append([wybrana_wartosc, pos])
    return decyzja

if __name__ == '__main__':
    sfset = load_softset()
    prt_softset(sfset)
    """ E={drogie, tanie, jeans, dresowe, klasyczne, modern, fit, granatowe, czarne, na zamek, na guziki}"""
    """A={jeans, modern, na zamek} """
    waga = [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0]
    """B={jeans, klasyczne, granatowe, na guziki} 
        waga = [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1]
    """
    print (waga)
    result = wartosc_wazona(sfset, waga)
    for ret in result:
        print ("Zwycieska wartosc to:%.3f na pozycji :%d" % \
            (ret[0], ret[1]))