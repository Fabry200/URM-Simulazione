# Simulazione della Macchina Universale di Registro (URM)

Questo progetto implementa una simulazione della **Macchina Universale di Registro (URM)**, una macchina teorica che esegue operazioni aritmetiche su un registro di variabili, seguendo un codice specifico. Il progetto fornisce un'interfaccia per eseguire una sequenza di istruzioni con un registro iniziale e un codice in input.

## Funzionalità

### 1. **Classe URM**

La classe `URM` simula una macchina universale di registro con un insieme di istruzioni predefinite. È possibile eseguire un codice sulla macchina che modifica il registro e produce dei risultati numerici.

### 2. **Operazioni di registro**

Il programma simula varie operazioni sui registri, inclusi:
- **Z**: Imposta il valore di un registro a 0.
- **S**: Aggiunge 1 al valore di un registro.
- **T**: Copia il valore di un registro in un altro.
- **J**: Confronta i valori di due registri e, se uguali, salta a un'altra istruzione.

### 3. **Calcolo delle funzioni computabili**

Alla fine dell'esecuzione del codice, viene calcolato il numero di "funzioni computabili" in base alla sequenza di operazioni eseguite dalla macchina, restituendo un numero che rappresenta la complessità computazionale dell'operazione.

## Funzioni Principali

### `run()`

Esegue il codice sulla macchina universale di registro.

**Parametri**:
- Nessun parametro. Si usa il `registro` e il `codice` passati durante l'inizializzazione.

**Descrizione**:
- Esegue una sequenza di operazioni sui registri e calcola le "funzioni computabili". Le operazioni sui registri vengono eseguite in base al comando fornito nel `codice` (lista di istruzioni). Ogni comando può essere uno tra i seguenti:
  - **'Z'**: Azzera il valore di un registro.
  - **'S'**: Incrementa il valore di un registro.
  - **'T'**: Copia il valore di un registro in un altro.
  - **'J'**: Confronta due registri e salta a un altro punto del codice se i valori sono uguali.

**Restituisce**:
- Stampa il registro durante l'esecuzione, insieme al calcolo delle "funzioni computabili".

### Esempio di Codice

```python
# Inizializzazione della macchina universale di registro
a = URM([9,7], [['Z', (3)], ['S', (3)], ['T', (3, 0)], ['J', (1, 2, 1)], ['Z', (5)]])

# Esecuzione del codice sulla macchina
a.run()
