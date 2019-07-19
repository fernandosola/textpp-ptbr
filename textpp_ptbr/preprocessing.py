"""
:Authors:
    Fernando Sola Pereira
"""

import re
import os
import unicodedata

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class TextPreProcessing:
    """Collection of static methods used to perform common text cleanup tasks focused on portuguese language.

    This class use dictionaries and regular expressions to expose a set of features to help 
    process Portuguese texts.
    """

    __re_hour_pattern = re.compile(r'(^|\b)(\d)+(\s)*(h|hr|hrs|hs)($|\b)', re.IGNORECASE)
    __re_common_person_names = None
    __re_stopwords = None
    __re_reduced_or_contracted_words = None
    __re_numbers_in_full = None
    __re_pronouns = None
    __re_adverbs = None

    __re_remove_excessive_spaces = re.compile(' +')
    __re_numbers_with_symbols = re.compile(r'([\d]+)([./-])*([\d ])')
    __re_pure_numbers = re.compile(r'(^|\b)(\d+)(\b|$)')
    __re_urls = re.compile(r'[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?')

    @staticmethod
    def __get_dicionary(dict_name):
        path = os.path.join(BASE_DIR, 'dictionaries', dict_name)
        palavras = []
        with open(path, 'r', encoding='utf-8') as arq_dic:
            palavras = [p.replace('\n', '') for p in arq_dic]
        return palavras

    @staticmethod
    def get_stopwords():
        """Returns a list of brazilian portuguese stopwords.

        All stopwords were copied from NLTK. 
        """


        return TextPreProcessing.__get_dicionary('stopwords.dic')

    @staticmethod
    def remove_hour(text):
        """Remove hour patterns from texts.

        .. code-block::

            In [ ]: from textpp_ptbr.preprocessing import TextPreProcessing as tpp
               ...: tpp.remove_hour('some text with 12h or another 13hs time explicit')
            Out[ ]: 'some text with   or another   time explicit'            

        """
        return TextPreProcessing.__re_hour_pattern.sub(' ', text)

    @staticmethod
    def remove_person_names(text):
        """Remove common person names.
        All accents are removed before identify names.
        This feature uses a dictionary with brazilian common names to build a regular expression that match common names.

        .. code-block::

            In [ ]: from textpp_ptbr.preprocessing import TextPreProcessing as tpp
               ...: tpp.remove_person_names('Afirma o réu que seu funcionário Mário Tadeu dirigia o veículo na ocasião.')
            Out[ ]: 'Afirma o reu que seu funcionario     dirigia o veiculo na ocasiao.'            


        """
        text = TextPreProcessing.remove_accents(text)
        if not TextPreProcessing.__re_common_person_names:
            def tratar(t):
                return TextPreProcessing.remove_accents(t)
            palavras = TextPreProcessing.__get_dicionary('common_person_names.dic')
            palavras = [tratar(p) for p in palavras]
            TextPreProcessing.__re_common_person_names = re.compile(r'(^|\b)(' + r'|'.join(palavras) + r')($|\b)')
        return TextPreProcessing.__re_common_person_names.sub(' ', text)

    @staticmethod
    def remove_pronouns(text):
        """Remove pronouns.

        Feature based on a dictionary with commmon portuguese pronouns extracted from wikitionary.
        """
        if not TextPreProcessing.__re_pronouns:
            palavras = TextPreProcessing.__get_dicionary('pronouns.dic')
            TextPreProcessing.__re_pronouns = re.compile(r'(^|\b)(' + r'|'.join(palavras) + r')($|\b)')
        return TextPreProcessing.__re_pronouns.sub(' ', text)

    @staticmethod
    def remove_reduced_or_contracted_words(text):
        if not TextPreProcessing.__re_reduced_or_contracted_words:
            palavras = TextPreProcessing.__get_dicionary('contracted_words.dic')
            TextPreProcessing.__re_reduced_or_contracted_words = re.compile(r'(^|\b)(' + r'|'.join(palavras) + r')($|\b)')
        return TextPreProcessing.__re_reduced_or_contracted_words.sub(' ', text)

    @staticmethod
    def remove_adverbs(texto):
        if not TextPreProcessing.__re_adverbs:
            palavras = TextPreProcessing.__get_dicionary('adverbs.dic')
            TextPreProcessing.__re_adverbs = re.compile(r'(^|\b)(' + r'|'.join(palavras) + r')($|\b)')
        return TextPreProcessing.__re_adverbs.sub(' ', texto)

    @staticmethod
    def remove_special_characters(texto):
        lista = '-#?º°ª.:/;~^`[{]}\\|!$%"\'&*()=+,><\t\r\n…'
        resultado = texto
        for i in range(0, len(lista)):
            resultado = resultado.replace(lista[i], ' ')
        return resultado

    @staticmethod
    def remove_excessive_spaces(texto):
        if texto is None or len(texto.strip()) == 0:
            # return texto
            return re.sub(' +', ' ', texto)
        return TextPreProcessing.__re_remove_excessive_spaces.sub(' ', texto)

    @staticmethod
    def remove_accents(text):
        if text is None or len(text.strip()) == 0:
            return text
        resultado = text
        resultado = unicodedata.normalize('NFKD', resultado).encode(
            'ASCII', 'ignore').decode('ASCII')
        return resultado

    @staticmethod
    def remove_symbols_from_numbers(text):
        resultado = text
        resultado = TextPreProcessing.__re_numbers_with_symbols.sub(r'\1\3', resultado)
        return resultado

    @staticmethod
    def remove_numbers(text):
        return TextPreProcessing.__re_pure_numbers.sub(r' ', text)

    @staticmethod
    def remove_numbers_in_full(text):
        if not TextPreProcessing.__re_numbers_in_full:
            palavras = TextPreProcessing.__get_dicionary('numbers_in_full.dic')
            TextPreProcessing.__re_numbers_in_full = re.compile(r'(^|\b)(' + r'|'.join(palavras) + r')($|\b)')
        return TextPreProcessing.__re_numbers_in_full.sub(' ', text)

    @staticmethod
    def remove_urls(text):
        resultado = text
        resultado = TextPreProcessing.__re_urls.sub(r' ', resultado)
        return resultado

    @staticmethod
    def remove_stopwords(texto):
        if not TextPreProcessing.__re_stopwords:
            stopwords = TextPreProcessing.get_stopwords()
            TextPreProcessing.__re_stopwords = re.compile(r'(^|\b)(' + r'|'.join(stopwords) + r')($|\b)')
        return TextPreProcessing.__re_stopwords.sub(' ', texto)

    @staticmethod
    def tratar_texto(text, remover_caracteres_especiais=True):
        if not text or len(text) == 0:
            return ''

        result = text
        result = TextPreProcessing.remove_person_names(result)
        result = TextPreProcessing.remove_reduced_or_contracted_words(result)
        result = TextPreProcessing.remove_pronouns(result)
        result = TextPreProcessing.remove_adverbs(result)
        result = TextPreProcessing.remove_numbers_in_full(result)
        result = TextPreProcessing.remove_symbols_from_numbers(result)
        result = TextPreProcessing.remove_urls(result)
        result = result.lower()
        result = TextPreProcessing.remove_stopwords(result)

        if remover_caracteres_especiais:
            result = TextPreProcessing.remove_special_characters(result)

        result = TextPreProcessing.remove_accents(result)
        result = TextPreProcessing.remove_numbers(result)
        result = TextPreProcessing.remove_excessive_spaces(result)
        result = result.strip()

        return result
