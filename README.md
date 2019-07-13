<!-- textpp-ptbr documentation master file, created by
sphinx-quickstart on Sun Jul  7 15:45:21 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# Common Text Pre-Processing for Portuguese

The purpose of this library is to provide a set of functions commonly
used for cleaning texts and similar tasks. The focus of the library is
Brazilian Portuguese.

## Common Usage

```
from textpp_ptbr.preprocessing import TextPreProcessing as tpp

 text = '''\
 Escrever é esquecer. A literatura é a maneira mais agradável de ignorar a vida.
 A música embala, as artes visuais animam, as artes vivas (como a dança e a arte
 de representar) entretêm. A primeira, porém, afasta-se da vida por fazer dela
 um sono; as segundas, contudo, não se afastam da vida - umas porque usam de
 fórmulas visíveis e portanto vitais, outras porque vivem da mesma vida humana.
 Não é o caso da literatura. Essa simula a vida. Um romance é uma história do
 que nunca foi e um drama é um romance dado sem narrativa. Um poema é a
 expressão de ideias ou de sentimentos em linguagem que ninguém emprega, pois
 que ninguém fala em verso.

 Fernando Pessoa'''

 tpp.remove_accents(text)
 print(tpp.remove_accents(text))

 # Output:
 # Escrever e esquecer. A literatura e a maneira mais agradavel de ignorar a vida.
 # A musica embala, as artes visuais animam, as artes vivas (como a danca e a arte
 # de representar) entretem. A primeira, porem, afasta-se da vida por fazer dela
 # um sono; as segundas, contudo, nao se afastam da vida - umas porque usam de
 # formulas visiveis e portanto vitais, outras porque vivem da mesma vida humana.
 # Nao e o caso da literatura. Essa simula a vida. Um romance e uma historia do
 # que nunca foi e um drama e um romance dado sem narrativa. Um poema e a
 # expressao de ideias ou de sentimentos em linguagem que ninguem emprega, pois
 # que ninguem fala em verso.
 #
 # Fernando Pessoa
```

## Main features


#### class textpp_ptbr.preprocessing.TextPreProcessing()
Collection of static methods used to perform common text cleanup tasks focused on portuguese language.

This class use dictionaries and regular expressions to expose a set of features to help 
process Portuguese texts.


#### static get_stopwords()
Returns a list of brazilian portuguese stopwords.

All stopwords were copied from NLTK.


#### static remove_hour(text)
Remove hour patterns from texts.

Usage:

    ‘some text with 12h or another 13hs time explicit’

Returns:

    ‘some text with   or another   time explicit’


#### static remove_person_names(text)
Remove common person names.

This feature uses a dictionary with brazilian common names.


#### static remove_pronouns(text)
Remove pronouns.

Feature based on a dictionary with commmon portuguese pronouns extracted from wikitionary.

<!-- Indices and tables -->
<!-- ================== -->
<!-- * :ref:`genindex` -->
<!-- * :ref:`modindex` -->
<!-- * :ref:`search` -->
