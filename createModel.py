import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.naive_bayes import MultinomialNB
import time
import pickle

start = time.time()

# Import Datasets
df_seq = pd.read_csv('pdb_data_seq-1.csv')
df_char = pd.read_csv('pdb_data_no_dups.csv')

print('Datasets have been loaded...')

# Filter for only proteins
protein_char = df_char[df_char.macromoleculeType == 'Protein']
protein_seq = df_seq[df_seq.macromoleculeType == 'Protein']

# Select only necessary variables to join
protein_char = protein_char[['structureId','classification']]
protein_seq = protein_seq[['structureId','sequence']]

# Join two datasets on structureId
model_f = protein_char.set_index('structureId').join(protein_seq.set_index('structureId'))


model_f.isnull().sum()

# Drop rows with missing values
model_f = model_f.dropna()

csv = model_f.to_csv(index=False)
f = open('dataset.csv', 'w+')
f.write(csv)

#
# # Look at classification type counts
# counts = model_f.classification.value_counts()
#
#
# # Get classification types where counts are over 1000
# types = np.asarray(counts[(counts > 1000)].index)
#
# # Filter dataset's records for classification types > 1000
# data = model_f[model_f.classification.isin(types)]
#
# # print(types)
# # print('%d is the number of records in the final filtered dataset' %data.shape[0])
#
#
# # 3). ----- Train Test Split -----
#
# # Split Data
# X_train, X_test,y_train,y_test = train_test_split(data['sequence'], data['classification'], test_size = 0.2, random_state = 1)
#
# # Create a Count Vectorizer to gather the unique elements in sequence
# vect = CountVectorizer(analyzer = 'char_wb', ngram_range = (4,4))
#
# # Fit and Transform CountVectorizer
# vect.fit(X_train)
# X_train_df = vect.transform(X_train)
# X_test_df = vect.transform(X_test)
#
# # 4). ------ Machine Learning Models ------
#
# # Make a prediction dictionary to store accuracys
# prediction = dict()
#
# # Naive Bayes Model
# model = MultinomialNB()
# model.fit(X_train_df, y_train)
# NB_pred = model.predict(X_test_df)
# prediction["MultinomialNB"] = accuracy_score(NB_pred, y_test)
# print( prediction['MultinomialNB'])
#
# #Print F1 score metrics
# print(classification_report(y_test, NB_pred, target_names = types))
#
#
# end = time.time()
#
# print("%s minutos" % (str((end - start) / 60)))
#
# pickle.dump(model, open("model.p", "wb"))
