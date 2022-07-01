# RATS

Rats (Rustico Analizzatore Testuale di Sentimenti) è un fallimentare tentativo di analisi automatica di un testo per la determinazione del sentimento (in particolare di _mood_ negativi o positivi).

Il sistema utilizza la libreria python [VU-sentiment-lexicon](https://github.com/opener-project/VU-sentiment-lexicon) e il dataset [Lessico Italiano dei Sentimenti](https://dspace-clarin-it.ilc.cnr.it/repository/xmlui/handle/20.500.11752/ILC-73) sviluppato in modo semi-automatico da ItalWordNet. In alternativa, il sistema utilizza [Spatana](/spatana), un dataset lessicale realizzato appositamente per questo progetto.

## Istruzioni

Installare nel sistema la libreria `libhunspell-dev` e create un ambiente virtuale python con:

    python3 -m venv rats-env
    source rats-env/bin/activate
    python3 -m pip install -r requirements.txt
    
A questo punto, tutte le volte successive sarà sufficiente attivare l'ambiente e lanciare l'analisi con:

    source rats-env/bin/activate
    python3 textAnalyzer.py -l it_IT -f sampletext.txt --use-spatana

## Limiti e problemi

1. RATS effetta _sempre_ lo stemming per determinare il lemma radice: il codice andrebbe modificato per effettuare lo stemming solo se il lemma non è presente nel database.
2. Essendo basato sul solo lessico, RATS considera le singole parole e non tiene conto, ad esempio, del contesto, dei polarity shifter, degli intensificatori, etc. Inoltre non distingue tra aggettivi, sostantivi, verbi.
3. Il dataset LIS contiene solo pesi discreti tripolari +1/0/-1 (sarebbe utile avere altri valori), non ha etichette per parole oggettivamente negative o positive e altri pesi, calcolati in modo semi-automatico, sono alquanto discutibili.
4. SPATANA ha molte [limitazioni indicate qui](/spatana#limiti-del-sistema-attuale)
5. Ci sarebbe molto altro da dire, ma basta questo punti a rendere RATS un fallimento :-)
