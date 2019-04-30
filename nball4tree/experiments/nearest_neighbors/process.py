import numpy as np
import pprint
import gensim
from bs4 import BeautifulSoup

w2v_model = gensim.models.Word2Vec.load('../../dataset/arabic/word2vec/models/n-gram/full_grams_sg_300_wiki.mdl').wv

def sense2word(sense, wordnet_path='../../dataset/arabic/arb2-lmf.xml'):
    wordnet_file = open(wordnet_path).read()
    wordnet = BeautifulSoup(wordnet_file, "xml")

    entries = list(filter((lambda lexicalEntry: lexicalEntry.Sense['synset'] == sense), wordnet.findAll('LexicalEntry')))
    words = list(map((lambda entry: entry.Lemma['writtenForm']), entries))

    return ','.join(words)

def simCos(word, dic, num=5, ball=True):
    vLst = []
    for k, v in dic.items():
        if word != k:
            if ball:
                vLst.append([word, k, np.dot(dic[word][:-2], dic[k][:-2])])
            else:
                vLst.append([word, k, np.dot(dic[word], dic[k])])

    vLst = sorted(vLst,key=lambda x: x[2], reverse=True)
    rlt = vLst[:min(num, len(vLst))]
    return [[ele[1], ele[2]] for ele in rlt]


def nearest_neighbors_of_word_sense(tlst = None, dic=None, simFunc=simCos, numOfNeighbors=0, isBall=True):
    neigbors = {}
    neigbors_w2v = {}
    keys = list(dic.keys())
    for word in tlst:
        if word in keys:
            neigbors[sense2word(word)] = [sense2word(ele[0]) for ele in simFunc(word, dic, num=numOfNeighbors, ball=isBall)]
            token = sense2word(word).replace(" ", "_")
            most_similar = w2v_model.most_similar(token, topn=10 )
            neigbors_w2v[sense2word(word)] = [term for term, _ in most_similar]

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(neigbors)
    pp.pprint(neigbors_w2v)
    return neigbors
