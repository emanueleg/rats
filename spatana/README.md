# SPATANA

SPATANA è semplice database semantico-lessicale che associa ad alcuni termini un peso positivo o negativo in modo semi automatico.

Spatana utilizza il peso (positivo o negativo) di alcuni termini noti per determinare, per analogia, il peso di altri termini ad essi affini.
Per determinare i sinonimi è utilizzato il [dizionario](https://raw.githubusercontent.com/LibreOffice/dictionaries/master/it_IT/th_it_IT_v2.dat) e il [thesaurus](https://raw.githubusercontent.com/LibreOffice/dictionaries/master/it_IT/it_IT.dic) del dizionario Italiano di OpenOffice/LibreOffice.

## Istruzioni

Installare nel sistema `python3` e `sqlite3`, poi lanciare la generazione del database con:

    sh make.sh

Al termine, il database `mydb.sqlite3` conterrà una tabella `sentiment` con tutti i lemmi e il peso calcolato (più è lontano dal lemma di partenza, più è debole).

## Limiti del sistema attuale

1. non distingue tra sostantivi, aggettivi, verbi
2. non considera diverse accezioni del termine: viene considerato solo quello con peso più significativo in valore assoluto
3. il database iniziale di lemmi etichettati manualmente è limitatissimo
