import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import MultinomialNB
from joblib import dump, load
import time

start = time.time()

# Import Datasets
data = pd.read_csv('dataset.csv')

classes = []

for col in data['classification']:
    if not col in classes:
        classes.append(col)


dump(classes, open("clases.p", "wb"))

# 3). ----- Train Test Split -----
X_train, X_test,y_train,y_test = train_test_split(data['sequence'], data['classification'], test_size = 0.2, random_state = 1)

# Create a Count Vectorizer to gather the unique elements in sequence
vect = CountVectorizer(analyzer = 'char_wb', ngram_range = (4,4))

# Fit and Transform CountVectorizer
vect.fit(X_train)

dump(vect, open("parseador.p", "wb"))
print("parseador listo")
X_train_df = vect.transform(X_train)

# 4). ------ Machine Learning Models ------

model = MultinomialNB()
model.fit(X_train_df, y_train)

dump(model, open("model.p", "wb"))

end = time.time()

print("%s minutos" % (str((end - start) / 60)))

