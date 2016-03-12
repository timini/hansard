from gensim import corpora, models, similarities
import logging
from datetime import datetime
import os

DICT_PATH = './data/hansard_corpus.dict'
CORPUS_PATH = './data/large_files/corpus.mm'
LDA_MODEL_PATH = './data/large_files/lda.model'

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

if os.path.exists(LDA_MODEL_PATH):
    # load dictionary
    lda_model = models.ldamulticore.LdaMulticore.load(LDA_MODEL_PATH)
else:
    dictionary = corpora.Dictionary.load(DICT_PATH)
    corpus = corpora.MmCorpus(CORPUS_PATH)

    start = datetime.now()
    print("started at:", start)
    lda_model = models.ldamulticore.LdaMulticore(corpus, num_topics=100, workers=3) # num_cores() - 1
    print("took: ", datetime.now() - start)

    lda_model.save(LDA_MODEL_PATH)
