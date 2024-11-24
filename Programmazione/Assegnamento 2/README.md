# Assegnamento 2

L’assegnamento prevede la realizzazione di un insieme di funzioni per la gestione semplificata di animali vertebrati presenti in uno zoo. 

## Struttura dei dati

Ogni animale è rappresentato da una **tupla** con i seguenti campi:

- **nome**: stringa  
- **classe**: stringa (una tra `"Mammifero"`, `"Uccello"`, `"Rettile"`, `"Anfibio"`, `"Pesce"`)  
- **specie**: stringa  
- **numero_zampe**: intero  
- **sangue_caldo**: booleano (`True` o `False`)  
- **ambiente**: lista contenente almeno uno tra `"Acqua"`, `"Terra"`, `"Aria"`  
- **zona**: stringa composta da una lettera e un numero (es. `"A5"`) che identifica la zona dello zoo  
- **verso**: stringa 

### Esempio di tupla:
```python
("Alex", "Mammifero", "Leone", 4, True, ["Terra"], "A5", "Ruggito")
```


## Gestione degli animali

Gli animali dello zoo sono organizzati in un **dizionario**, strutturato come segue:  

- La **chiave** è il nome dell'animale (che deve essere **univoco**).  
- Il **valore** è la relativa tupla contenente tutte le informazioni sull'animale.

### Funzioni richieste

1. È necessario implementare **almeno le funzioni** specificate nel file `zoo.py`.  
2. È consentito definire **funzioni ausiliarie** per migliorare la soluzione o per dividere il codice in moduli più piccoli e comprensibili.  
3. È possibile **estendere le funzionalità** del catalogo aggiungendo nuove funzioni a discrezione.

### Controllo dei parametri

Per ogni funzione implementata:  
- Verificare che i **parametri in ingresso** rispettino i tipi attesi.  
- In caso di parametri non validi, stampare a schermo **messaggi di errore chiari** per segnalare le situazioni errate.  
