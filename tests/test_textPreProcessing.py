from unittest import TestCase
import os
from textpp_ptbr.preprocessing import TextPreProcessing as tpp

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestTextPreProcessing(TestCase):

    def test_stopwords(self):
        sw = tpp.get_stopwords()
        for w in ['de', 'do', 'das']:
            assert w in sw, 'Should "{}" be in dict'.format(w)

    def test_remove_hour(self):
        text = 'texto de teste 11h outro 15hs teste 16 h novamente 17hrs algum'
        assert tpp.remove_hour(text) == 'texto de teste   outro   teste   novamente   algum'

    def test_remove_person_names(self):
        text = 'Afirma o réu que seu funcionário Mário Tadeu dirigia o veículo na ocasião.'
        assert tpp.remove_person_names(text) == 'Afirma o reu que seu funcionario     dirigia o veiculo na ocasiao.'

    def test_remove_pronouns(self):
        text = 'Afirma o réu que seu funcionário Mário Tadeu dirigia o veículo na ocasião.'
        assert tpp.remove_pronouns(text) == 'Afirma   réu     funcionário Mário Tadeu dirigia   veículo na ocasião.'

    def test_remove_reduced_or_contracted_words(self):
        text = "Ninguém sabe ao certo donde partiram os gritos."
        assert tpp.remove_reduced_or_contracted_words(text) == "Ninguém sabe   certo   partiram os gritos."

    def test_remove_adverbs(self):
        text = "Chegaram tarde para o Jantar. Era a moça mais bonita da festa. Partiram ontem apressadamente."
        assert tpp.remove_adverbs(text) == "Chegaram   para o Jantar. Era a moça   bonita da festa. Partiram    ."

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
