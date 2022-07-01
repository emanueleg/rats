import sqlite3

class Spatana:
    con = None
    cur = None

    def __init__(self, db):
        print(db)
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

    def getPolarityValue(self, txt):
        self.cur.execute("SELECT punti FROM sentiment WHERE lemma = :word;", {"word": txt})
        row = self.cur.fetchone()
        if row is not None and row[0] is not None:
            return int(row[0])
        else:
            return 0
    
    def __del__(self):
        self.cur.close()
        self.con.close()
