# RATS

Rats (Rustico Analizzatore Testuale di Sentimenti) è un fallimentare tentativo di analisi automatica di un testo per la determinazione del sentimento (in particolare di _mood_ negativi o positivi).

Il sistema utilizza la libreria python [VU-sentiment-lexicon](https://github.com/opener-project/VU-sentiment-lexicon) e il dataset [Lessico Italiano dei Sentimenti](https://dspace-clarin-it.ilc.cnr.it/repository/xmlui/handle/20.500.11752/ILC-73) sviluppato in modo semi-automatico da ItalWordNet.

## Istruzioni

Installare nel sistema la libreria `libhunspell-dev` e create un ambiente virtuale python con:

    python3 -m venv rats-env
    source rats-env/bin/activate
    python3 -m pip install -r requirements.txt
    
A questo punto, tutte le volte successive sarà sufficiente attivare l'ambiente e lanciare l'analisi con:

    source rats-env/bin/activate
    python3 textAnalyzer.py -l it_IT -f sampletext.txt

## Limiti e problemi

1. RATS non funziona come dovrebbe.
2. Il punto 1. dovrebbe essere sufficiente, ma un forte limite è il dataset LIS, che non ha etichette per molte parole oggettivamente negative o positive.
3. Inoltre, il dataset LIS non contiene pesi con valore continuo ma solo valori discreti tripolari (+1/0/-1); sarebbe utile avere altri valori.
4. Il codice di RATS considera le singole parole e non tiene perciò conto, ad esempio, delle negazioni ("non brutto" è davvero doppiamente negativo? o dovrebbe essere positivo? e quanto più positivo rispetto a bello?).
5. Ci sarebbe molto altro da dire, ma bastano i primi 4 punti a rendere RATS un fallimento :-)
