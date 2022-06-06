import argparse
from Rats import Rats

### PARSE INPUT ARGUMENT ####

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', help='input file', metavar='BASEFILENAME', required=True)
parser.add_argument('-d', '--dictdir', help='language dir', metavar='DIRPATH', default="/usr/share/hunspell/")
parser.add_argument('-l', '--lang', help='language', metavar='ISOLANG', default="it_IT")
parser.add_argument('--csvoutput', default=False, action=argparse.BooleanOptionalAction)
parser.add_argument('--csvheadings', default=True, action=argparse.BooleanOptionalAction)

args = parser.parse_args()


### PREPARE GLOBAL VARIABLES ###

HUNSPELL_DIC = args.dictdir + '/' + args.lang + '.dic'
HUNSPELL_AFF = args.dictdir + '/' + args.lang + '.aff'
LANG = args.lang[:2]
TRANSCRIPTION = args.filename


### CORE FUNCTIONS ###

sent = Rats(LANG, HUNSPELL_DIC, HUNSPELL_AFF)

with open(TRANSCRIPTION, 'r') as file:
    data = file.read()

sent.analyze(data)


### EXTRACT METRICS ###

out_fields = [
    {"desc": "Number of words", "fmt": "{}", "val": sent.get_wordcount()},
    {"desc": "Sentiment overall score (%)", "fmt": "{:+}", "val": sent.get_normalized_sentiment_score()},
    {"desc": "Polarized-terms ratio (%)", "fmt": "{}", "val": sent.get_polarized_language_ratio()},
    {"desc": "Lexical richness (%)", "fmt": "{}", "val": sent.get_lexical_richness()}
    ]

desc = [x["desc"] for x in out_fields]
fmt = [x["fmt"] for x in out_fields]
val = [x["val"] for x in out_fields]


### OUTPUT RESULTS ###

if args.csvoutput:
    if args.csvheadings:
        print(",".join(desc))
    print(",".join(fmt).format(*val))
else:
    for i in range(len(out_fields)):
        print((desc[i] + ": " + fmt[i]).format(val[i]))
