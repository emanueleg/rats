import argparse
import sqlite3

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--db', type=str, required=False, default='mydb.sqlite3')
parser.add_argument('-s', '--sin-table', type=str, required=False, default='lemmi')
parser.add_argument('-m', '--sent-table', type=str, required=False, default='sentiment')
parser.add_argument('-i', '--stronger-weight', type=int, required=False, default=5)
parser.add_argument('-f', '--weaker-weight', type=int, required=False, default=1)
args = parser.parse_args()

START_WEIGHT = args.stronger_weight
STOP_WEIGHT = args.weaker_weight

con = sqlite3.connect(args.db, isolation_level='DEFERRED'   )
cur = con.cursor()
cur.execute('''PRAGMA synchronous = OFF''')
cur.execute('''PRAGMA journal_mode = OFF''')


cur.execute("UPDATE sentiment SET punti = :punti WHERE punti > 0;", {"punti": START_WEIGHT})
cur.execute("UPDATE sentiment SET punti = :punti WHERE punti < 0;", {"punti": -1*START_WEIGHT})
con.commit()

for i in [1, -1]:
    for ref_pt in range(i*START_WEIGHT, i*STOP_WEIGHT, -1*i):
        cur.execute("SELECT lemma, percorso FROM sentiment WHERE punti = :punti;", {"punti": ref_pt})
        rows = cur.fetchall()
        for lemma in rows:
            ref_lemma = lemma[0]
            percorso = ref_lemma
            if lemma[1]:
                percorso = lemma[1] + ";" + percorso
            cur.execute("SELECT sinonimi FROM lemmi WHERE lemma = :parola;", {"parola": ref_lemma} )
            synonyms = cur.fetchone()
            if not synonyms:
                continue
            new_pt = ref_pt - 1*i
            for sin in synonyms[0].split('|'):
                cur.execute("UPDATE sentiment SET punti = :new_pt, percorso = :percorso WHERE lemma = :sin AND ABS(punti) < ABS(:new_pt);", {"new_pt": new_pt, "ref_lemma": ref_lemma, "sin": sin, "percorso": percorso} )
                #print(ref_lemma, sin, new_pt)
            con.commit()
        print("Done weight ", ref_pt)
con.commit()

cur.execute("DELETE FROM sentiment WHERE punti = 0;")
con.commit()
cur.close()
con.close()
