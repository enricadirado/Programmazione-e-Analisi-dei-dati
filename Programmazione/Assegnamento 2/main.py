# Script di test Assegnamento 2py 622AA 2024/25 (non modificare)
from testMy import *
from zoo import *

def controllo():
    #contiamo i test falliti
    testFalliti=0
    print("==========> Inizio nuovo test <=============\n\n")
    # creo un dizionario
    x = {}
    y = {}

    # test inserimenti corretti
    print("==========> Test 1")
    testFalliti += testEqual(inserisci(x, "Alex", "Mammifero", "Leone", 4, True, ["Terra"], "A1", "Ruggito"), True)
    testFalliti += testEqual(inserisci(x, "Marty", "Mammifero", "Zebra", 4, True, ["Terra"], "A1", "Nitrito"), True)
    testFalliti += testEqual(inserisci(x, "Melman", "Mammifero", "Giraffa", 4, True, ["Terra"], "A1", "Landito"), True)
    testFalliti += testEqual(inserisci(x, "Gloria", "Mammifero", "Ippopotamo", 4, True, ["Terra", "Acqua"], "A1", "Ruggito"), True)
    testFalliti += testEqual(inserisci(x, "Skipper", "Uccello", "Pinguino", 2, True, ["Terra", "Acqua"], "A2", "Garrito"), True)
    testFalliti += testEqual(inserisci(x, "Kowalski", "Uccello", "Pinguino", 2, True, ["Terra", "Acqua"], "A2", "Garrito"), True)
    testFalliti += testEqual(inserisci(x, "Rico", "Uccello", "Pinguino", 2, True, ["Terra", "Acqua"], "A2", "Garrito"), True)
    testFalliti += testEqual(inserisci(x, "Soldato", "Uccello", "Pinguino", 2, True, ["Terra", "Acqua"], "A2", "Garrito"), True)
    testFalliti += testEqual(inserisci(x, "Kaa", "Rettile", "Pitone", 0, False, ["Terra"], "A3", "Sibilo"), True)
    testFalliti += testEqual(inserisci(x, "Flounder", "Pesce", "Pesce pagliaccio", 0, False, ["Acqua"], "A3", ""), True)
    testFalliti += testEqual(inserisci(x, "Nemo", "Pesce", "Pesce pagliaccio", 0, False, ["Acqua"], "A3", ""), True)
    testFalliti += testEqual(inserisci(x, "Titti", "Uccello", "Canarino", 2, True, ["Aria"], "A2", "Cinguettio"), True)
    testFalliti += testEqual(inserisci(x, "Anacleto", "Uccello", "Gufo", 2, True, ["Aria"], "A2", "Bubbolio"), True)
    testFalliti += testEqual(inserisci(x, "Coco", "Rettile", "Coccodrillo", 4, False, ["Terra", "Acqua"], "A3", "Trimbulio"), True)

    # test inserimenti sbagliati
    print("==========> Test 2")
    # duplicato
    ("Tizio", "Mammiferi","Uomo", 2, True, ["Terra"], "A1", "Parla")
    testFalliti += testEqual(inserisci(x, "Alex", "Mammifero", "Leone", 4, True, ["Terra"], "A1", "Ruggito"), False)
    # tipo
    testFalliti += testEqual(inserisci(x, "Tizio", 25,"Uomo", 2, True, ["Terra"], "A1", "Parla"), False)
    testFalliti += testEqual(inserisci(x, "Tizio", "Mammifero",1, 2, True, ["Terra"], "A1", "Parla"), False)
    testFalliti += testEqual(inserisci(x, "Tizio", "Mammifero","Uomo", "due", True, ["Terra"], "A1", "Parla"), False)
    testFalliti += testEqual(inserisci(x, "Tizio", "Mammifero","Uomo", 2, "True", "Terra", "A1", "Parla"), False)
    testFalliti += testEqual(inserisci(x, "Tizio", "Mammifero","Uomo", 2, "True", "Terra", 25, "Parla"), False)
    testFalliti += testEqual(inserisci(x, "Tizio", "Mammifero","Uomo", 2, "True", "Terra", "A1", 123456), False)
    # valore
    testFalliti += testEqual(inserisci(x, "Tizio", "Mammiferi","Uomo", 2, True, ["Terra"], "A1", "Parla"), False)
    testFalliti += testEqual(inserisci(x, "Tizio", "Mammifero","Uomo", 2, True, ["Pisa"], "A1", "Parla"), False)
    testFalliti += testEqual(inserisci(x, "Tizio", "Mammifero","Uomo", 2, True, ["Terra"], "A", "Parla"), False)
    testFalliti += testEqual(inserisci(x, "Tizio", "Mammifero","Uomo", 2, True, ["Terra"], "AA", "Parla"), False)

    # test su serializza
    print("==========> Test 3")
    testFalliti += testSerializza(serializza(x), x)
    testFalliti += testEqual(serializza(y), "")

    # test su animale
    print("==========> Test 4")
    testFalliti += testEqual(animale(x, "Alex"), y=("Alex", "Mammifero", "Leone", 4, True, ["Terra"], "A1", "Ruggito"))
    testFalliti += testEqual(animale(x, "Tizio"), None)
    testFalliti += testEqual(animale(y, "Alex"), None)

    # test su elimina
    print("==========> Test 5")
    testFalliti += testEqual(elimina(x, "Soldato"), True)
    testFalliti += testEqual(elimina(x, "Soldato"), False)
    testFalliti += testEqual(elimina(y, "Soldato"), False)

    # test su cambia_zona
    print("==========> Test 6")
    testFalliti += testEqual(cambia_zona(x, "Coco", "A4"), True)
    testFalliti += testEqual(cambia_zona(x, "Coco", "AA"), False)
    testFalliti += testEqual(cambia_zona(x, "Coco", 123), False)
    testFalliti += testEqual(cambia_zona(x, "Coco", "A"), False)

    # test su zone
    print("==========> Test 7")
    testFalliti += testEqual(zone(x), ["A1", "A2", "A3", "A4"])
    testFalliti += testEqual(zone(y), [])

    # test su animali_zona
    print("==========> Test 8")
    testFalliti += testEqual(animali_zona(x, "A1"), ["Alex", "Marty", "Melman", "Gloria"])
    testFalliti += testEqual(animali_zona(y, "A2"), [])
    
    # test su zone_animali
    print("==========> Test 9")
    testFalliti += testEqual(zone_animali(x), {'A1': ['Alex', 'Marty', 'Melman', 'Gloria'], 'A2': ['Skipper', 'Kowalski', 'Rico', 'Titti', 'Anacleto'], 'A3': ['Kaa', 'Flounder', 'Nemo'], 'A4': ['Coco']})
    testFalliti += testEqual(zone_animali(y), {})

    # test su animali_classe
    print("==========> Test 10")
    testFalliti += testEqual(animali_classe(x, "Mammifero"), ['Alex', 'Marty', 'Melman', 'Gloria'])
    testFalliti += testEqual(animali_classe(y, "Uccello"), [])


    # test su animali_specie
    print("==========> Test 11")
    testFalliti += testEqual(animali_specie(x, "Pinguino"), ['Skipper', 'Kowalski', 'Rico'])
    testFalliti += testEqual(animali_specie(y, "Pinguino"), [])

    # test su animali_ambiente
    print("==========> Test 12")
    testFalliti += testEqual(animali_ambiente(x, "Acqua"), ['Gloria', 'Skipper', 'Kowalski', 'Rico', 'Flounder', 'Nemo', 'Coco'])
    testFalliti += testEqual(animali_ambiente(y, "Acqua"), [])

    #test animali zampe almeno
    print("==========> Test 13")
    testFalliti += testEqual(animali_con_zampe_almeno(x, 4), ['Alex', 'Marty','Melman', 'Gloria', 'Coco'])
    testFalliti += testEqual(animali_con_zampe_almeno(x), ['Alex', 'Marty','Melman', 'Gloria', 'Skipper', 'Kowalski', 'Rico', 'Titti', 'Anacleto', 'Coco'])
    testFalliti += testEqual(animali_con_zampe_almeno(y, 2), [])

    # test conta
    print("==========> Test 14")
    testFalliti += testEqual(conta_sangue(x, True), 9)
    testFalliti += testEqual(conta_sangue(y, True), 0)
    testFalliti += testEqual(conta_classe(x, "Mammifero"), 4)
    testFalliti += testEqual(conta_classe(y, "Mammifero"), 0)
    testFalliti += testEqual(conta_specie(x, "Pinguino"), 3)
    testFalliti += testEqual(conta_specie(y, "Pinguino"), 0)

    #stampa finale zoo
    print("==========> Stampa finale zoo")
    print(serializza(x))

    # abbiamo finito ?
    if testFalliti == 0:
        print("\t****Test completati -- effettuare la consegna come da README")
    else:
        print("Test falliti: ",testFalliti)

# eseguo i test automatici
controllo()

