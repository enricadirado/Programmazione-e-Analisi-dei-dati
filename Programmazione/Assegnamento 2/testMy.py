# test interi stringhe
def testEqual(x, y):
    """ Controlla se x e y sono uguali e restituisce 1 se non lo sono e
    0 se lo sono"""
    if x == y:
        print("Pass")
        return 0
    else:
        print("Not Passing")
        return 1


def testSerializza(s,zoo):
    """ Controlla che nella stringa s ci siano tutti gli elementi delle tuple dello zoo
    """
    for a in zoo:
        for e in zoo[a]:
            if isinstance(e, bool):
                if str(e) in s or "caldo" in s:
                    continue
                elif str(e) in s or "freddo" in s:
                    continue
                else:
                    print("Not Passing")
                    return 1
            elif isinstance(e, list):
                for i in e:
                    if i in s:
                        continue
                    else:
                        print("Not Passing")
                        return 1
            elif str(e) not in s:
                print("Not Passing")
                return 1
    print("Pass")
    return 0