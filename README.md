# Controllo Cittadinanza(con vecchia autenticazione, con SPID non fuziona)

Questo script Python è stato creato per automatizzare il processo di controllo dello stato della pratica di cittadinanza italiana sul portale del Ministero dell'Interno. L'autore ha sviluppato questo strumento per evitare di dover navigare manualmente attraverso le varie pagine del sito.

## Motivazione

L'idea alla base di questo script è nata dalla necessità di semplificare e automatizzare il controllo periodico dello stato della propria pratica di cittadinanza.

## Funzionalità

* Accede al portale del Ministero dell'Interno (`https://nullaostalavoro.dlci.interno.it/Ministero/Index2`).
* Gestisce il login inserendo le credenziali (email e password) fornite dall'utente.
* Naviga automaticamente attraverso le sezioni del sito fino alla pagina relativa allo stato della pratica di cittadinanza.
* Estrae e visualizza lo stato più recente della pratica.
* Esegue il logout al termine dell'operazione.
* Opera in modalità headless, ovvero senza aprire un'interfaccia grafica del browser.
* Include una gestione base degli errori, ad esempio segnalando se è necessario aggiornare la password.

## Prerequisiti

* Python 3.x
* Google Chrome installato
* ChromeDriver compatibile con la versione di Google Chrome installata e presente nel PATH di sistema o nella directory dello script.
* Le librerie Python elencate nel file `requirements.txt`.

## Installazione

1.  **Clonare il repository:**
    ```bash
    git clone [https://github.com/skrypnyk81/control-citizenship.git](https://github.com/skrypnyk81/control-citizenship.git)
    cd control-citizenship
    ```

2.  **Installare le dipendenze:**
    Si consiglia di creare un ambiente virtuale:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Su Windows usare `venv\Scripts\activate`
    ```
    Installare le librerie necessarie:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configurare le credenziali:**
    Modificare il file `credential.py` con la propria email e password di accesso al portale:
    ```python
    LOGIN = 'tua_email_login' # Sostituire con la propria email
    PASSWORD = 'tua_password'   # Sostituire con la propria password
    ```

## Utilizzo

Per avviare lo script ed eseguire il controllo dello stato della pratica, eseguire il seguente comando dalla directory principale del progetto:

```bash
python cittadinanza.py
