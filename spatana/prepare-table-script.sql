DROP TABLE IF EXISTS lemmi;
CREATE TABLE lemmi (
  lemma TEXT NOT NULL,
  sinonimi TEXT
);
DELETE FROM lemmi;
.mode csv
.separator ;
.import ./sinonimi.csv lemmi

DROP TABLE IF EXISTS sentiment;
CREATE TABLE sentiment (
  lemma TEXT NOT NULL,
  punti INTEGER DEFAULT 0,
  percorso TEXT
);
INSERT INTO sentiment (lemma) SELECT lemma FROM lemmi;

DROP TABLE IF EXISTS known;
CREATE TABLE known (
  lemma TEXT NOT NULL,
  punti INTEGER
);
.mode csv
.separator ;
.import ./known.csv known

UPDATE sentiment SET punti = known.punti FROM known WHERE known.lemma=sentiment.lemma;
DROP TABLE known;
