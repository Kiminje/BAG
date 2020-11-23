import pickle
import numpy as np
import scipy.sparse


ner_dict = pickle.load(open('data/ner_dict.pickle', 'rb'))
data_extra = [d for d in pickle.load(open('train.json.extra.preprocessed.pickle', 'rb'))]
print("ner dict start")
print(ner_dict)
print("end")

print("data extra\n", data_extra)