from gensim.models import Doc2Vec
from gensim.models.doc2vec import LabeledSentence

from gensim import corpora
from collections import defaultdict
import csv
import numpy as np

documents = []
p_id = []
topic_documents = []

with open('newResultWith40TagwithoutD.csv') as dfile:
    f_csv = csv.reader(dfile)
    for line in f_csv:
        if len(line[1]) == 0:
            documents.append("x")
        l = line[1][1:len(line[1]) - 1]
        tmp = l.split(', ')
        documents.append(tmp)
        p_id.append(line[0])

for i in range(len(documents)):
    topic_documents.append(LabeledSentence(documents[i], [p_id[i]]) )

model = Doc2Vec(size=128,window=15, min_count=1, workers=4,sample=1e-5,negative=5,iter=100,dm=0,hs=0,dbow_words=1,dm_concat=1)
model.build_vocab(topic_documents)
model.train(topic_documents,total_examples=model.corpus_count, epochs=model.iter)

sentence_vec=np.zeros((len(documents),128))
for i in range(len(documents)):
    sentence_vec[i]=model.docvecs[p_id[i]]
    
print "done"

#similarity_value=np.zeros((len(documents),len(documents)))
#with open('edge_list.csv', 'wb') as csvfile:
#    fieldnames = ['source', 'target']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#    writer.writeheader() 
#    for i in range(len(documents)):
#        for j in range(i, len(documents)):
#            similarity_value[i,j]=model.n_similarity(documents[i],documents[j])
#            if i!=j and similarity_value[i,j]>0.9:
#                write_dict = {}
#                write_dict["source"]=i
#                write_dict["target"]=j
#                writer.writerow(write_dict)
        

#import logging
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#
#model.save('/tmp/my_model.doc2vec')
#
#model_loaded = Doc2Vec.load('/tmp/my_model.doc2vec')
