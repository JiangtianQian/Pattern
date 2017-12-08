from gensim.models import Doc2Vec
from gensim.models.doc2vec import LabeledSentence

from gensim import corpora
from collections import defaultdict
from pprint import pprint

documents = [['human', 'interface', 'computer'],
 ['survey', 'user', 'computer', 'system', 'response', 'time'],
 ['eps', 'user', 'interface', 'system'],
 ['system', 'human', 'system', 'eps'],
 ['user', 'response', 'time'],
 ['trees'],
 ['graph', 'trees'],
 ['graph', 'minors', 'trees'],
 ['graph', 'minors', 'survey']]


frequency = defaultdict(int)
for text in documents:
     for token in text:
         frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
         for text in documents]

print texts

topic_documents = []

topic_documents.append( LabeledSentence(texts[0], [u'SENT_1']) )
topic_documents.append( LabeledSentence(texts[1], [u'SENT_2']) )
topic_documents.append( LabeledSentence(texts[2], [u'SENT_3']) )

model = Doc2Vec(size=10, window=8, min_count=0, workers=4)
model.build_vocab(topic_documents)
model.train(topic_documents,total_examples=model.corpus_count, epochs=model.iter)

sentence_vec=model.docvecs[u'SENT_3']

value=model.n_similarity(u'SENT_3', u'SENT_2')

