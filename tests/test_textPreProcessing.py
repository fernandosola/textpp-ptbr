from unittest import TestCase
import os
from textpp_ptbr.preprocessing import TextPreProcessing as ttp

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestTextPreProcessing(TestCase):
    def test_get_dicionary(self):
        d = ttp.__get_dicionary(os.path.join(BASE_DIR, 'textpp_ptbr', 'dictionaries', 'adverbs.dic'))
        assert len(d) > 0, 'Should be greater than 0'
        d = ttp.__get_dicionary(os.path.join(BASE_DIR, 'textpp_ptbr', 'dictionaries', 'common_person_names.dic'))
        assert len(d) > 0, 'Should be greater than 0'
        d = ttp.__get_dicionary(os.path.join(BASE_DIR, 'textpp_ptbr', 'dictionaries', 'contracoes.dic'))
        assert len(d) > 0, 'Should be greater than 0'
        d = ttp.__get_dicionary(os.path.join(BASE_DIR, 'textpp_ptbr', 'dictionaries', 'numbers_in_full.dic'))
        assert len(d) > 0, 'Should be greater than 0'
        d = ttp.__get_dicionary(os.path.join(BASE_DIR, 'textpp_ptbr', 'dictionaries', 'pronouns.dic'))
        assert len(d) > 0, 'Should be greater than 0'
        d = ttp.__get_dicionary(os.path.join(BASE_DIR, 'textpp_ptbr', 'dictionaries', 'stopwords.dic'))
        assert len(d) > 0, 'Should be greater than 0'

    def test_stopwords(self):
        sw = ttp.get_stopwords()
        for w in ['de', 'do', 'das']:
            assert w in sw, 'Should "{}" be in dict'.format(w)

    def test_remove_hour(self):
        text = 'texto de teste 11h outro 15hs teste 16 h novamente 17hrs algum'
        assert ttp.remove_hour(text) == 'texto de teste   outro   teste   novamente   algum'

    def test_remove_person_names(self):
        self.fail()

    def test_remove_pronouns(self):
        self.fail()

    def test_remove_reduced_or_contracted_words(self):
        self.fail()

    def test_remove_adverbs(self):
        self.fail()

    def test_remove_special_characters(self):
        self.fail()

    def test_remove_excessive_spaces(self):
        self.fail()

    def test_remove_accents(self):
        self.fail()

    def test_remove_symbols_from_numbers(self):
        self.fail()

    def test_remove_numbers(self):
        self.fail()

    def test_remove_numbers_in_full(self):
        self.fail()

    def test_remove_urls(self):
        self.fail()

    def test_remove_stopwords(self):
        self.fail()

    def test_tratar_texto(self):
        self.fail()
