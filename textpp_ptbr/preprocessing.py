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

    @classmethod
    def __get_dicionary(cls, dict_name):
        path = os.path.join(BASE_DIR, 'dictionaries', dict_name)
        with open(path, 'r', encoding='utf-8') as dictionary:
            return [p.replace('\n', '') for p in dictionary]

    @classmethod
    def get_stopwords(cls):
        """Returns a list of brazilian portuguese stopwords.

        All stopwords were extracted from NLTK. 
        """
        return cls.__get_dicionary('stopwords.dic')

    @classmethod
    def remove_hour(cls, text):
        """Remove hour patterns from texts.

        .. code-block::

            In [ ]: from textpp_ptbr.preprocessing import TextPreProcessing as tpp
               ...: tpp.remove_hour('some text with 12h or another 13hs time explicit')
            Out[ ]: 'some text with   or another   time explicit'            

        """
        return cls.__re_hour_pattern.sub(' ', text)

    @classmethod
    def remove_person_names(cls, text):
        """Remove common person names.

        All accents are removed before identify names.
        This method uses a dictionary with brazilian common names to build a regular 
        expression that match common names.

        .. code-block::

            In [ ]: from textpp_ptbr.preprocessing import TextPreProcessing as tpp
               ...: tpp.remove_person_names('Afirma o réu que seu funcionário Mário Tadeu dirigia o veículo na ocasião.')
            Out[ ]: 'Afirma o reu que seu funcionario     dirigia o veiculo na ocasiao.'            


        """
        text = cls.remove_accents(text)
        if not cls.__re_common_person_names:
            dictionary = cls.__get_dicionary('common_person_names.dic')
            dictionary = [cls.remove_accents(p) for p in dictionary]
            cls.__re_common_person_names = re.compile(r'(^|\b)(' + r'|'.join(dictionary) + r')($|\b)')
        return cls.__re_common_person_names.sub(' ', text)

    @classmethod
    def remove_pronouns(cls, text):
        """Remove pronouns.

        Method based on a dictionary.

        .. code-block::

            In [ ]: from textpp_ptbr.preprocessing import TextPreProcessing as tpp
               ...: tpp.remove_pronouns('Ninguém sabe ao certo donde partiram os gritos.')
            Out[ ]: 'Ninguém sabe   certo   partiram os gritos.'            


        """
        if not cls.__re_pronouns:
            palavras = cls.__get_dicionary('pronouns.dic')
            cls.__re_pronouns = re.compile(r'(^|\b)(' + r'|'.join(palavras) + r')($|\b)', re.IGNORECASE)
        return cls.__re_pronouns.sub(' ', text)

    @classmethod
    def remove_reduced_or_contracted_words(cls, text):
        """Remove reduced or crontracted words.

        Method based on a dictionary.

        .. code-block::

            In [ ]: from textpp_ptbr.preprocessing import TextPreProcessing as tpp
               ...: tpp.remove_pronouns('Ninguém sabe ao certo donde partiram os gritos.')
            Out[ ]: 'Ninguém sabe   certo   partiram os gritos.'            

        """

        if not cls.__re_reduced_or_contracted_words:
            palavras = TextPreProcessing.__get_dicionary('contracted_words.dic')
            cls.__re_reduced_or_contracted_words = re.compile(r'(^|\b)(' + r'|'.join(palavras) + r')($|\b)')
        return cls.__re_reduced_or_contracted_words.sub(' ', text)

    @classmethod
    def remove_adverbs(cls, text):
        """Remove reduced or crontracted words.

        Method based on a dictionary.

        .. code-block::

            In [ ]: from textpp_ptbr.preprocessing import TextPreProcessing as tpp
               ...: tpp.remove_pronouns('Chegaram tarde para o Jantar. Era a moça mais bonita da festa. Partiram ontem apressadamente.')
            Out[ ]: 'Chegaram   para o Jantar. Era a moça   bonita da festa. Partiram    .'            
        
        """

        if not cls.__re_adverbs:
            palavras = cls.__get_dicionary('adverbs.dic')
            cls.__re_adverbs = re.compile(r'(^|\b)(' + r'|'.join(palavras) + r')($|\b)')
        return cls.__re_adverbs.sub(' ', text)

    @staticmethod
    def remove_special_characters(text):
        lista = '-#?º°ª.:/;~^`[{]}\\|!$%"\'&*()=+,><\t\r\n…'
        result = text
        for i in range(0, len(lista)):
            result = result.replace(lista[i], ' ')
        return result

    @classmethod
    def remove_excessive_spaces(cls, texto):
        if texto is None or len(texto.strip()) == 0:
            # return texto
            return re.sub(' +', ' ', texto)
        return cls.__re_remove_excessive_spaces.sub(' ', texto)

    @staticmethod
    def remove_accents(text):
        if text is None or len(text.strip()) == 0:
            return text
        result = text
        result = unicodedata.normalize('NFKD', result).encode(
            'ASCII', 'ignore').decode('ASCII')
        return result

    @classmethod
    def remove_symbols_from_numbers(cls, text):
        resultado = text
        resultado = cls.__re_numbers_with_symbols.sub(r'\1\3', resultado)
        return resultado

    @classmethod
    def remove_numbers(cls, text):
        return cls.__re_pure_numbers.sub(r' ', text)

    @classmethod
    def remove_numbers_in_full(cls, text):
        if not TextPreProcessing.__re_numbers_in_full:
            palavras = cls.__get_dicionary('numbers_in_full.dic')
            cls.__re_numbers_in_full = re.compile(r'(^|\b)(' + r'|'.join(palavras) + r')($|\b)')
        return cls.__re_numbers_in_full.sub(' ', text)

    @classmethod
    def remove_urls(cls, text):
        resultado = text
        resultado = cls.__re_urls.sub(r' ', resultado)
        return resultado

    @classmethod
    def remove_stopwords(cls, texto):
        if not cls.__re_stopwords:
            stopwords = cls.get_stopwords()
            cls.__re_stopwords = re.compile(r'(^|\b)(' + r'|'.join(stopwords) + r')($|\b)')
        return cls.__re_stopwords.sub(' ', texto)
