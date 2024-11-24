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

    # test su check_string
    print("==========> Test check_string")
    testFalliti += testEqual(check_string("Alex"), True)
    testFalliti += testEqual(check_string("Pesce pagliaccio"), True)
    testFalliti += testEqual(check_string(1), False)
    testFalliti += testEqual(check_string("1"), False)
    testFalliti += testEqual(check_string("*"), False)
    testFalliti += testEqual(check_string("Al3x"), False) 
    testFalliti += testEqual(check_string(""), False) 
    testFalliti += testEqual(check_string(" "), False) 
    testFalliti += testEqual(check_string("  "), False) 

    # test su check_ambiente
    print("==========> Test check_ambiente")
    testFalliti += testEqual(check_ambiente("Acqua"), True)
    testFalliti += testEqual(check_ambiente(["Acqua", "Terra"]), True)
    testFalliti += testEqual(check_ambiente("Alex"), False)
    testFalliti += testEqual(check_ambiente(["Acqua", "Acqua"]), False)
    testFalliti += testEqual(check_ambiente(["Terra","Acqua", "Acqua"]), False) #NUOVO
    testFalliti += testEqual(check_ambiente(["Terra", "Acqua", "Acqua", "Terra"]), False)  # NUOVO
    testFalliti += testEqual(check_ambiente(["Terra", "Terra", "Acqua"]), False)  # NUOVO
    testFalliti += testEqual(check_ambiente([]), False)  
    testFalliti += testEqual(check_ambiente(""), False)  
    testFalliti += testEqual(check_ambiente(" "), False)  
    testFalliti += testEqual(check_ambiente("  "), False)  


    # test su check_zona
    print("==========> Test check_zona")
    testFalliti += testEqual(check_zona("A4"), True)
    testFalliti += testEqual(check_zona("AA"), False)
    testFalliti += testEqual(check_zona("1A"), False)
    testFalliti += testEqual(check_zona(123), False)
    testFalliti += testEqual(check_zona("A"), False)
    testFalliti += testEqual(check_zona("AA1"), False) 
    testFalliti += testEqual(check_zona("A11"), False) 
    testFalliti += testEqual(check_zona(""), False) 
    testFalliti += testEqual(check_zona(" "), False) 
    testFalliti += testEqual(check_string("  "), False) 

    # test su check_classe
    print("==========> Test check_classe")
    testFalliti += testEqual(check_classe("Mammifero"), True)
    testFalliti += testEqual(check_classe("Alex"), False)
    testFalliti += testEqual(check_classe(123), False)
    testFalliti += testEqual(check_classe("A"), False)
    testFalliti += testEqual(check_classe("Mammifero1"), False) 
    testFalliti += testEqual(check_classe(""), False) 
    testFalliti += testEqual(check_classe(" "), False) 
    testFalliti += testEqual(check_classe("  "), False) 

    # abbiamo finito ?
    if testFalliti == 0:
        print("\t****Test completati -- effettuare la consegna come da README")
    else:
        print("Test falliti: ",testFalliti)

# eseguo i test automatici
controllo()
