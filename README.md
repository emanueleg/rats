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

1. RATS non funziona come dovrebbe: considera le singole parole e non tiene conto, ad esempio, del contesto e delle negazioni ("non brutto" è davvero doppiamente negativo? o dovrebbe essere positivo? e quanto più positivo rispetto a bello?).
2. Il punto 1. dovrebbe essere sufficiente, ma... il dataset LIS contiene solo pesi discreti tripolari +1/0/-1 (sarebbe utile avere altri valori) e non ha etichette per molte parole oggettivamente negative o positive.
3. Ci sarebbe molto altro da dire, ma basta questo punti a rendere RATS un fallimento :-)
