import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.naive_bayes import MultinomialNB
import time
import pickle

start = time.time()

# Import Datasets
data = pd.read_csv('dataset.csv')

classes = []

for col in data['classification']:
    if not col in classes:
        classes.append(col)

# 3). ----- Train Test Split -----

# Split Data
X_train, X_test,y_train,y_test = train_test_split(data['sequence'], data['classification'], test_size = 0.2, random_state = 1)

# Create a Count Vectorizer to gather the unique elements in sequence
vect = CountVectorizer(analyzer = 'char_wb', ngram_range = (4,4))

# Fit and Transform CountVectorizer
vect.fit(X_train)
X_train_df = vect.transform(X_train)
X_test_df = vect.transform(X_test)

# 4). ------ Machine Learning Models ------

# Naive Bayes Model
model = MultinomialNB()
model.fit(X_train_df, y_train)
NB_pred = model.predict(X_test_df)
print(accuracy_score(NB_pred, y_test))


#Print F1 score metrics
print(classification_report(y_test, NB_pred, target_names = classes))


end = time.time()

print("%s minutos" % (str((end - start) / 60)))

pickle.dump(model, open("model.p", "wb"))
