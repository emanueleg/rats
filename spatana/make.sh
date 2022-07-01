#!/bin/sh
#wget https://raw.githubusercontent.com/LibreOffice/dictionaries/master/it_IT/th_it_IT_v2.dat
#patch < it_IT_Thesaurus_typo.patch
cp th_it_IT_v2.dat th.dat
sed -i 's/|\([0-9]\+\)/;/g' th.dat
sed -i 's/([^)]*)/*/g' th.dat
sed -i ':a;N;/\n\*/s/\n//;ta;P;D' th.dat
sed -i 's/;\*|/;/g' th.dat
sed -i 's/\*|/|/g' th.dat
cat th.dat | sort > th.txt
rm th.dat

#wget https://raw.githubusercontent.com/LibreOffice/dictionaries/master/it_IT/it_IT.dic
cut -d/ -f1 it_IT.dic > dic.txt
sed -i '1d' dic.txt
sed -i '/^$/d' dic.txt
sed -i 's/[0-9]*//g' dic.txt
sed -i '/^$/d' dic.txt
cat dic.txt | sort > diz.txt
rm dic.txt

join -t";" diz.txt th.txt -11 -21 -a1 -a2 --nocheck-order -o 0,2.2 > sinonimi.csv
rm th.txt diz.txt
sqlite3 mydb.sqlite3 < prepare-table-script.sql
rm sinonimi.csv
python3 sent.py
echo "VACUUM 'main';" | sqlite3 mydb.sqlite3
