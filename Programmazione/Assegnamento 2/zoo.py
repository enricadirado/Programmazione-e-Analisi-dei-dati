# Da completare con il codice

import string

#FUNZIONI AUSILIARIE

#1 - Funzione ausiliaria per il controllo di un parametro di tipo stringa
#La funzione controlla che il parametro passato sia di tipo stringa e che non sia una stringa vuota
def check_string(stringa):
    if type(stringa) is not str or stringa.strip()=="": #stringa.strip() elimina gli spazi iniziali e finali; se restituisce una stringa, la stringa in input era vuota o composta solo da spazi
        return False
    stringa_new = stringa.replace(" ", "") #Se la stringa passata è composta da due stringhe (ad esempio, "Pesce pagliaccio" ), unisce le due stringhe
    for x in stringa_new:
        if x not in string.ascii_letters:
            return False
    return True


#2 - Funzione ausiliaria per il controllo del parametro "ambiente" all'interno delle funzioni "inserisci" e "animali_ambiente"
#La funzione controlla che il parametro passato sia una lista composta da "ambienti" validi o, nel caso l'ambiente passato sia una stringa (come nella funzione "animali_ambiente") sia un ambiente valido
def check_ambiente(amb):
    ambienti_possibili= ["Acqua", "Terra", "Aria"]

    #controllo del parametro "ambiente" all'interno della funzione "inserisci"
    if type(amb)==list:
        if len(amb) == 0:
            return False
        for x in amb:
            y=amb.count(x)
            if x not in ambienti_possibili or y!=1 or not check_string(x): #Controlla se l'elemento della lista amb è presente o meno nella lista ambienti_possibili, che non ci siano duplicati e che sia una stringa
                return False
        return True

    #controllo del parametro "ambiente" all'interno della funzione "animali_ambiente"
    if type(amb)==str:
        if amb in ambienti_possibili and check_string(amb): #Controlla che la stringa amb sia presente nella lista ambienti_possibili e che sia una stringa
            return True
        return False


#3 - Funzione ausiliaria per il controllo del parametro "zona" all'interno delle funzioni "inserisci", "cambia_zona" e "animali_zona"
#La funzione controlla che la stringa passata sia conforme alla formattazione del parametro "zona" (stringa di due caratteri composta da una lettera maiuscola e una cifra)
def check_zona(zona):
    if type(zona)!=str or len(zona)!=2 or not zona[0].isupper() or not zona[1].isdigit():
        return False
    return True


#4 - Funzione ausiliaria per il controllo del parametro "classe" all'interno delle funzioni "inserisci", "animali_classe" e "conta_classe"
#La funzione controlla che la stringa "classe" sia presente nella lista classi_possibili e che sia una stringa
def check_classe(classe):
    classi_possibili = ["Mammifero", "Uccello", "Pesce", "Rettile", "Anfibio"]
    if classe in classi_possibili and check_string(classe):
        return True
    return False


#(nome, classe, specie, numero_zampe, sangue_caldo, ambiente, zona, verso)
def inserisci(zoo, nome, classe, specie, numero_zampe, sangue_caldo, ambiente, zona, verso):
    """
    Inserisce un nuovo animale (evitando duplicati) nel dizionario zoo controllando che i tipi dei
    parametri attuali abbiano il tipo corretto (specificato fra parentesi) e siano
    nel range di valori ammessi senza modificare maiuscole e minuscole
    Esempio:
    inserisci("Kowalski", "Uccello", "Pinguino", 2, True, ["Terra", "Acqua"], "A2", "Garrito")

    :param nome: nome dell'animale (stringa)
    :param classe: classe dell'animale (stringa) uno fra: "Mammifero", "Uccello", "Pesce", "Rettile", "Anfibio"
    :param specie: specie dell'animale (stringa)
    :param numero_zampe: numero di zampe (intero positivo)
    :param sangue_caldo: sangue caldo (booleano)
    :param ambiente: ambiente in cui vive (lista di stringhe) almeno uno fra: "Acqua", "Terra", "Aria"
    :param zona: zona in cui si trova (stringa) composta da una lettera maiuscola seguita da un numero intero (es. "A1")
    :param verso: verso che emette (stringa)

    :return: True se l'inserimento e' stato effettuato con successo,
    :return: False  se i parametri non hanno il tipo corretto o non sono corretti
    """

    risultato=True #Variabile usata per catturare gli eventuali errori; ogni volta che viene riscontrato un parametro non corretto, risultato viene impostato a False per catturare e stampare tutti gli errori

    if type(zoo)!=dict:
        print("Il primo valore deve essere un dizionario")
        risultato=False

    if nome in zoo:
        print("Il nome inserito è già presente nel dizionario")
        risultato=False

    if not check_string(nome) or not check_string(specie): #Invocazione della funzione "check_string" per controllare che i parametri "specie" e "nome" siano stringhe; se "check_string" restituisce False, la stringa non è valida, quindi not lo trasforma in True
        print("Nome e specie devono essere stringhe non vuote, contenenti solo caratteri alfabetici")
        risultato=False

    if verso!="": #Se il parametro "verso" è presente (ovvero non è una stringa vuota) viene richiamata la funzione "check_string" per controllare che il parametro "verso" sia una stringa valida
        if not check_string(verso):
            print("Nome, specie, e verso devono essere stringhe alfabetiche")
            risultato=False

    if not check_classe(classe): #Invocazione della funzione "check_classe" per controllare che il parametro "classe" sia una classe valida
        print("La classe deve essere una tra Mammifero, Uccello, Pesce, Rettile o Anfibio")
        risultato=False

    if type(numero_zampe)!=int or numero_zampe<0:
        print("Il numero di zampe deve essere positivo")
        risultato=False

    if type(sangue_caldo)!=bool:
        print("Il parametro sangue_caldo deve essere di tipo booleano")
        risultato=False

    if type(ambiente)!=list or not check_ambiente(ambiente): #viene richiamata la funzione "check_ambiente" per verificare che il parametro "ambiente" sia un ambiente valido
        print("L'ambiente deve essere una lista non vuota e contenere almeno un elemento fra Acqua, Terra, Aria")
        risultato=False

    if not check_zona(zona): #Invocazione della funzione "check_zona" per controllare che il parametro "zona" sia una zona valida
        print("La zona deve essere una stringa composta da una lettera maiuscola e un numero")
        risultato=False

    if risultato: #Se nessun controllo è errato, risultato è ancora True
        zoo[nome]= (nome, classe, specie, numero_zampe, sangue_caldo, ambiente, zona, verso)

    return risultato #Se ci sono stati errori, la funzione restituisce False (ovvero, almeno un controllo ha impostato "risultato" su False), altrimenti l'inserimento è stato effettuato correttamente e la funzione restituisce True
    

def serializza(zoo):
    """
    Serializza tutti gli animali nel dizionario zoo creando una singola stringa.
    La sottostringa relativa all'animale puo' essere stampata con il formato che si preferisce,
    basta che siano presenti tutte le informazioni dell'animale.
    Le stringhe relative a animali diversi devono essere separati dal carattere "a capo" --> "\n"
    Ad esempio, posso serializzare il dizionario
    {'Alex': ('Alex', 'Mammifero', 'Leone', 4, True, ['Terra'], 'A1', 'Ruggito'),
    'Kowalski': ('Kowalski', 'Uccello', 'Pinguino', 2, True, ['Terra', 'Acqua'], 'A2', 'Garrito')
    'Nemo': ('Nemo', 'Pesce', 'Pesce pagliaccio', 0, False, ['Acqua'], 'A3', '')}
    come
    "Alex è un Leone (Mammifero) con 4 zampe, sangue caldo e vive in in zona A1 (Terra) facendo un Ruggito\n
    Kowalski è un Pinguino (Uccello) con 2 zampe, sangue freddo e vive in zona A2 (Terra e Acqua) facendo un Garrito\n
    Nemo è un Pesce pagliaccio (Pesce) con 0 zampe, sangue freddo e vive in in zona A3 (Acqua)\n"
    :param zoo: il dizionario da serializzare
    :return: una stringa che rappresenta il dizionario
    """

    stringa=""
    sangue_caldo_str=""

    if type(zoo)!=dict: #Si verifica se il parametro "zoo" è un dizionario o meno
        print ("Il valore deve essere un dizionario")
        return stringa

    for x in zoo:

        if zoo[x][4]: #Se "sangue_caldo" è True
            sangue_caldo_str="caldo"
        else:  #Se "sangue_caldo" è False
            sangue_caldo_str="freddo"

        if len(zoo[x][5])==1: #Se "ambiente" è composto da un solo elemento
            ambiente_str=zoo[x][5][0]
        if len(zoo[x][5])>1: #Se "ambiente" è composto da più elementi
            ambiente_str=' e '.join(zoo[x][5]) #Si crea una stringa composta dagli elmenti di "ambiente"

        stringa=stringa + str(x) + " è un " + zoo[x][2] + " ("+ zoo[x][1] + ") con " + str(zoo[x][3]) + " zampe, sangue " + sangue_caldo_str + " e vive in zona " + zoo[x][6] + " ("+ambiente_str + ") facendo un " + zoo[x][7] + "\n"

    return stringa


def animale(zoo, nome):
    """
    Restituisce la tupla relativa all'animale con nome "nome"
    :param zoo: il dizionario
    :param nome: il nome dell'animale da estrarre
    :return t: la tupla relativa all'animale
    :return None: se l'animale non e' presente nel dizionario
    """

    if type(zoo)!=dict: #Si verifica se il parametro "zoo" è un dizionario o meno
        print("Il primo valore deve essere un dizionario")
        return None

    if not check_string(nome): #Si verifica se il parametro "nome" è una stringa corretta o meno richiamando la funzione "check_string"
        print("Il secondo valore deve essere una stringa")
        return None

    if nome not in zoo: #Si verifica se il "nome" passato come parametro è presente o meno nel dizionario "zoo"
        print("L'animale " + nome + " non è presente nello zoo")
        return None

    return zoo[nome]


def elimina(zoo, nome):
    """
    Elimina l'animale con nome "nome" dal dizionario zoo
    :param zoo: il dizionario
    :param nome: il nome dell'animale da eliminare
    :return: True se l'eliminazione e' avvenuta con successo
    :return: False se l'animale non e' presente nel dizionario
    """

    #viene richiamata la funzione "animale" che effettua i controlli sui parametri "zoo" e "nome" passati come parametri all'interno della funzione "elimina" e restituisce la tupla dell'animale corrispondente
    nome_animale=animale(zoo, nome) 
    if not nome_animale: #Verifica se la funzione "animale" ha restituito una tupla valida o meno
        return False #Se "animale" restituisce None, "elimina" restituisce False
    else:
        del zoo[nome] #Altrimenti, se "animale" ha restituito una tupla valida, elimina l'elemento dal dizionario zoo con chiave "nome"
        return True


def cambia_zona(zoo, nome, zona):
    """
    Cambia la zona dell'animale con nome "nome"
    :param zoo: il dizionario
    :param nome: il nome dell'animale da spostare
    :param zona: la nuova zona in cui si trova l'animale
    :return: True se lo spostamento e' avvenuto con successo
    :return: False se l'animale non e' presente nel dizionario o la zona non e' corretta
    """
    
    if not check_zona(zona): #Si verifica se il parametro "zona" è una zona corretta o meno richiamando la funzione "check_zona"
        print("La zona deve essere una stringa composta da una lettera maiuscola e un numero")
        return False

    nome_animale=animale(zoo, nome) 
    if not nome_animale: #Verifica se la funzione "animale" ha restituito una tupla valida o meno
        return False #Se "animale" restituisce None, "cambia_zona" restituisce False
    
    new_tupla = zoo[nome][:6] + (zona,) + zoo[nome][7:]  #Creazione di una tupla formata dai primi 6 elementi, concatenata alla nuova zona e il restante elemento
    zoo[nome] = new_tupla  #Assegnazione della tupla alla chiave corrispondente
    return True


def zone(zoo):
    """
    Restituisce la lista delle zone presenti nel dizionario zoo
    :param zoo: il dizionario
    :return: la lista delle zone presenti nel dizionario zoo
    """

    lista_zone=[]

    if type(zoo)!=dict: #Si verifica se il parametro "zoo" è un dizionario o meno
        print("Il valore inserito deve essere un dizionario")
        return lista_zone

    for x in zoo:
        if zoo[x][6] not in lista_zone: #Si verifica che non vengano restituite zone duplicate
            lista_zone.append(zoo[x][6]) 
    return lista_zone


def animali_zona(zoo, zona):
    """
    Restituisce la lista degli animali presenti nella zona "zona"
    :param zoo: il dizionario
    :param zona: la zona di interesse
    :return: la lista degli animali presenti nella zona "zona"
    """

    lista_animali_zona = []

    if type(zoo)!=dict: #Si verifica se il parametro "zoo" è un dizionario o meno
        print("Il valore inserito deve essere un dizionario")
        return lista_animali_zona

    if not check_zona(zona): #Si verifica se il parametro "zona" è una zona corretta o meno richiamando la funzione "check_zona"
        print("La zona deve essere una stringa composta da una lettera maiuscola e un numero")
        return lista_animali_zona

    for x in zoo:
        if zoo[x][6] == zona: #per ogni animale nel dizionario si verifica se la "zona" dell'animale corrisponde alla "zona" passata come parametro
            lista_animali_zona.append(x)
    return lista_animali_zona



def zone_animali(zoo):
    """
    Restituisce un dizionario che ha come chiavi le zone e come valori la lista degli animali presenti in quella zona
    Ad esempio, posso restituire il dizionario
    {'A1': ['Alex'], 'A2': ['Skipper', 'Kowalski']}

    :param zoo: il dizionario
    :return: il dizionario con le zone e gli animali presenti in ciascuna zona
    """

    dict_zone_animali={}

    if type(zoo)!=dict: #Si verifica se il parametro "zoo" è un dizionario o meno
        print("Il valore inserito deve essere un dizionario")
        return dict_zone_animali

    for x in zoo:
        if zoo[x][6] not in dict_zone_animali: #Verifica se la zona è presente o meno nel dizionario dict_zone_animali
            dict_zone_animali[zoo[x][6]]=[x] #Se non è presente, crea la chiave in dict_zone_animali con nome "zona" e le associa una lista che ha come unico valore il nome dell'animale
        else: 
            dict_zone_animali[zoo[x][6]].append(x) #Altrimenti, se la zona è già presente come chiave, aggiunge alla lista della zona passata il nome dell'animale
    return dict_zone_animali



def animali_classe(zoo, classe):
    """
    Restituisce la lista degli animali della classe "classe"
    :param zoo: il dizionario
    :param classe: la classe di interesse
    :return: la lista degli animali della classe "classe"
    """

    lista_animali_classe=[]
    if type(zoo)==dict: #Si verifica se il parametro "zoo" è un dizionario o meno
        if check_classe(classe): #Si verifica se il parametro "classe" è una classe corretta o meno richiamando la funzione "check_classe"
            for x in zoo:
                if zoo[x][1] == classe: #Per ogni animale nello zoo si verifica se ha come "classe" quella passata come parametro
                    lista_animali_classe.append(x)
            return lista_animali_classe
        else:
            print("Il secondo valore inserito deve essere una classe tra Mammifero, Uccello, Pesce, Rettile o Anfibio")
            return lista_animali_classe
    else:
        errore = "Il valore inserito deve essere un dizionario"
        return lista_animali_classe



def animali_specie(zoo, specie):
    """
    Restituisce la lista degli animali della specie "specie"
    :param zoo: il dizionario
    :param specie: la specie di interesse
    :return: la lista degli animali della specie "specie"
    """

    lista_animali_specie=[]
    if type(zoo)==dict: #Si verifica se il parametro "zoo" è un dizionario o meno
        if check_string(specie):  #Invocazione della funzione "check_string" per controllare che il parametro "specie" sia una stringa
            for x in zoo:
                if zoo[x][2] == specie: #Controlla se la specie (indice 2 nella tupla) corrisponde al parametro "specie"
                    lista_animali_specie.append(x)
            return lista_animali_specie
        else:
            print("Il secondo valore inserito deve essere una stringa corrispondente a una specie")
            return lista_animali_specie
    else:
        print("Il primo valore inserito deve essere un dizionario")
        return lista_animali_specie


def animali_ambiente(zoo, ambiente):
    """
    Restituisce la lista degli animali che vivono nell'ambiente "ambiente"
    :param zoo: il dizionario
    :param ambiente: l'ambiente di interesse
    :return: la lista degli animali che vivono nell'ambiente "ambiente"
    """

    lista_animali_ambiente=[]
    if type(zoo)==dict: #Si verifica se il parametro "zoo" è un dizionario o meno
        if check_ambiente(ambiente):  #Invocazione della funzione "check_ambiente" per controllare che il parametro "ambiente" sia un ambiente valido
            for x in zoo:
                for j in zoo[x][5]: #Iterazione sugli elementi nella lista "ambiente" (indice 5 della tupla)
                    if j == ambiente: #Se la stringa della lista "ambiente" (indice 5 della tupla) è uguale al parametro "ambiente" passato
                        lista_animali_ambiente.append(x)
            return lista_animali_ambiente
        else:
            print("Il secondo valore inserito deve essere una lista non vuota e contenere almeno un elemento fra Acqua, Terra, Aria")
            return lista_animali_ambiente
    else:
        print("Il primo valore inserito deve essere un dizionario")
        return lista_animali_ambiente



def animali_con_zampe_almeno(zoo, numero_zampe=2):
    """
    Restituisce la lista degli animali che hanno almeno "numero_zampe" zampe
    :param zoo: il dizionario
    :param numero_zampe: il numero minimo di zampe (default=2)
    :return: la lista degli animali che hanno almeno "numero_zampe" zampe
    """
    lista_animali_zampe=[]
    if type(zoo)==dict: #Si verifica se il parametro "zoo" è un dizionario o meno
        if type(numero_zampe)==int and numero_zampe>=0: 
            for x in zoo:
                if zoo[x][3]>=numero_zampe: #Per ogni animale nello zoo si verifica se ha almeno 2 zampe
                    lista_animali_zampe.append(x)
            return lista_animali_zampe
        else:
            print("Il secondo valore inserito deve essere un numero intero positivo")
            return lista_animali_zampe
    else:
        print("Il primo valore inserito deve essere un dizionario")
        return lista_animali_zampe



def conta_sangue(zoo, sangue_caldo):
    """
    Restituisce il numero di animali con sangue caldo o freddo
    :param zoo: il dizionario
    :param sangue_caldo: True se si vogliono contare gli animali con sangue caldo, False altrimenti
    :return: il numero di animali con sangue caldo o freddo
    """
    lista_conta_sangue=[]

    if type(zoo)==dict: #Si verifica se il parametro "zoo" è un dizionario o meno
        if type(sangue_caldo)==bool:
            for x in zoo:
                if zoo[x][4]==sangue_caldo: #Per ogni animale del dizionario si controlla se la tipologia di sangue è uguale a quella passata come parametro
                    lista_conta_sangue.append(x)
            return len(lista_conta_sangue)
        else:
            print("Il primo valore inserito deve essere di tipo booleano")
            return len(lista_conta_sangue)
    else:
        print("Il primo valore inserito deve essere un dizionario")
        return len(lista_conta_sangue)



def conta_classe(zoo, classe):
    """
    Restituisce il numero di animali della classe "classe"
    :param zoo: il dizionario
    :param classe: la classe di interesse
    :return: il numero di animali della classe "classe"
    """
    #viene richiamata la funzione "animale_classe" che effettua i controlli sui parametri "zoo" e "classe" passati come parametri all'interno della funzione "conta_classe"
    lista_conta_classe = animali_classe(zoo, classe)
    return len(lista_conta_classe) #Ritorna il numero di animali che appartengono alla "classe" passata come parametro


def conta_specie(zoo, specie):
    """
    Restituisce il numero di animali della specie "specie"
    :param zoo: il dizionario
    :param specie: la specie di interesse
    :return: il numero di animali della specie "specie"
    """

    #viene richiamata la funzione "animale_specie" che effettua i controlli sui parametri "zoo" e "specie" passati come parametri all'interno della funzione "conta_specie"
    lista_conta_specie = animali_specie(zoo, specie)
    return len(lista_conta_specie) #Ritorna il numero di animali che appartengono alla "specie" passata come parametro



