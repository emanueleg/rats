import argparse
import re
import hunspell  # install libhunspell-dev
import collections
from LexiconMod import LexiconSent # from https://dspace-clarin-it.ilc.cnr.it/repository/xmlui/handle/20.500.11752/ILC-73


# RATS - Rustico Analizzatore Testuale di Sentimenti
class Rats:
    lex = None
    text = ""
    arr = []
    wc = 0
    distinct_wc = 0
    sentiment_score = 0
    posw = 0
    negw = 0

    def __init__(self, language, dict_path, aff_path):
        self.lex = LexiconSent(language)
        self.text = ""
        self.hobj = hunspell.HunSpell(dict_path, aff_path)
        self.arr = []

    def analyze(self, txt):
        self.text = txt
        
        aText = self._clean_string(self.text)
        aText = self._tokenize_string(aText)
        aText = self._stem_words(aText)
        self.arr = aText
        self._compute_stats()

    def get_wordcount(self):
        return self.wc
    
    def get_polarized_wordcount(self):
        return abs(self.posw) + abs(self.negw)

    def get_distinct_wordcount(self):
        return self.distinct_wc

    def get_positive_wordcount(self):
        return self.posw

    def get_negative_wordcount(self):
        return self.negw

    def get_abs_sentiment_score(self):
        return +1*abs(self.posw) -1*abs(self.negw)

    def get_normalized_sentiment_score(self):
        return round(100*self.get_abs_sentiment_score()/self.get_polarized_wordcount())

    def get_polarized_language_ratio(self):
        return round(100*self.get_polarized_wordcount()/self.get_wordcount())

    def get_lexical_richness(self):
        return round(100*self.get_distinct_wordcount()/self.get_wordcount())

    def _compute_stats(self):
        elements_count = collections.Counter(self.arr)

        self.sentiment_score = 0
        self.wc = len(self.arr)
        self.distinct_wc = len(set(self.arr))
        self.posw = 0
        self.negw = 0
        
        for key, value in elements_count.items():
            pol = self.lex.getPolarityValue(key)
            self.posw += value*pol if pol > 0 else 0
            self.negw += value*pol if pol < 0 else 0

    def _clean_string(self, dirty):
        dirty = dirty.replace('\n', ' ')
        dirty = dirty.replace('\r', ' ')
        dirty = dirty.replace('\t', ' ')
        #dirty = dirty.translate(str.maketrans(' ', ' ', string.punctuation))
        dirty = re.sub(r'[^\w\s]', ' ', dirty)
        dirty = dirty.strip()
        while dirty != dirty.replace("  ", " "):
            dirty = dirty.replace("  ", " ")
        return dirty

    def _tokenize_string(self, text):
        return text.split()

    def _fix_broken_it_dic(self):
        self.hobj.remove("quindo")
        self.hobj.add("quindi")

    def _stem_words(self, word_array):
        suggested = []
        self._fix_broken_it_dic()
        for w in word_array:
            if not self.hobj.spell(w):
                if self.hobj.suggest(w):
                    w = self.hobj.suggest(w)[0]
                else:
                    w = ""
                
            for ww in w.split():
                ww = self.hobj.stem(ww)[0]
                ww = ww.lower()
                ww = ww.decode('UTF-8')
                suggested.append(ww)
        return suggested

#################

