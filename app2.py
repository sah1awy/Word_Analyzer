from nltk.tokenize import word_tokenize,sent_tokenize
from nltk import WordNetLemmatizer
from nltk.stem import LancasterStemmer,PorterStemmer,RegexpStemmer,SnowballStemmer
from builtins import range
from sklearn.metrics.pairwise import pairwise_distances
from nltk.corpus import wordnet
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import spacy 
import numpy as np 

class Glove:
        
    def __init__(self):
        self.embedding = []
        self.word2vec = {}
        self.idx2word = []
        self.na = []
        with open(r"D:\glove.840B.300d\glove.840B.300d.txt",'r') as f:
            for line in f:
                try:
                    values = line.split()
                    vec = np.asarray(values[1:],dtype=np.float32)
                    w = values[0]
                    self.word2vec[w] = vec
                    self.embedding.append(vec)
                    self.idx2word.append(w)
                except:
                    self.na.append(line.split()[0])
                    continue

    def dist1(self,a,b):
        return np.linalg(a-b)

    def dist2(self,a,b):
        return 1 - a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))


    def nearest_neighbors(self,w,n=5):
        res =[]
        self.embedding = np.array(self.embedding)
        V,D = self.embedding.shape
        dist,metric = self.dist2, "euclidean"
        if w not in self.word2vec:
            return None
        vec = self.word2vec[w]
        distances = pairwise_distances(vec.reshape(1,D),self.embedding,metric).reshape(V)
        for i in distances.argsort()[1:n+1]:
            res.append(self.idx2word[i])
        return res
    
class Synset:
    def __init__(self,w):
        self.w = wordnet.synsets(w)

    def definition(self):
        return self.w[-1].definition()
    
    def syn_ant(self):
        ant = []
        syn = []
        for s in self.w:
            for l in s.lemmas():
                syn.append(l.name())
                if l.antonyms():
                    ant.append(l.antonyms()[0].name())

        return syn,ant