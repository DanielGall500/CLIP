from language.categories import UNIQUE_IRISH_NUMS,IRISH_RESUMPTIVE_PRONOUNS
from data_manager.focloir_interface import get_lookup_from_focloir
from tools.pos.pos_tagger import POSTagger 

"""
-- Irish POS Tagger --
This is a very basic part-of-speech tagger (or verifier, moreso) for Irish.
It checks whether a word is a:
* Adjective
* Noun
* Resumptive Pronoun

This should be expanded on to become a more comprehensive part-of-speech tagger in the future.
"""
IRISH_ADJ_PATH = "data/POS/focloir_adjectives.csv"
IRISH_NOUN_PATH = "data/POS/focloir_nouns.csv"

class IrishPOSTagger(POSTagger):

    def __init__(self):
        adj_lookup = get_lookup_from_focloir(IRISH_ADJ_PATH)
        noun_lookup = get_lookup_from_focloir(IRISH_NOUN_PATH)

        resumptive_lookup = {res:True for res in IRISH_RESUMPTIVE_PRONOUNS}
        number_lookup = {num:True for num in UNIQUE_IRISH_NUMS}

        self.POS_lookup = {
            "ADJ": adj_lookup,
            "NOUN": noun_lookup,
            "RES": resumptive_lookup,
            "NUM": number_lookup
        }

    def is_POS(self, lemma: str, pos: str):
        return lemma in self.POS_lookup[pos]

    def is_adjective(self, lemma: str):
        return self.is_POS(lemma, "ADJ")

    def is_noun(self, lemma: str):
        return self.is_POS(lemma, "NOUN")

    def is_number(self, lemma: str):
        return self.is_POS(lemma, "NUM")

    def is_resumptive_pronoun(self, lemma: str):
        return self.is_POS(lemma, "RES")