# these are the necessary imports to start with the fake new detection.
import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# data from the datased will be read in to the computer
df=pd.read_csv('D:\\DataFlair\\news.csv')
#get shape and head
df.shape
df.head()

# get the label from the data frame

labels=df.label
labels.head()

#split the dataset
x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.2, random_state=7)

# initialize a TfidfVectorizer
tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)
# it is essential that we put the max prequency at 0.07
# fit and transform train set, transform test set
tfidf_train=tfidf_vectorizer.fit_transform(x_train) 
tfidf_test=tfidf_vectorizer.transform(x_test)

# initialize a PassiveAggressiveClassifier
pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)
# predict on the test set and calculate accuracy
y_pred=pac.predict(tfidf_test)
score=accuracy_score(y_test,y_pred)
print(f'Accuracy: {round(score*100,2)}%')

# build confusion matrix
confusion_matrix(y_test,y_pred, labels=['FAKE','REAL'])

# at the conclusion of this we will get an array of fake and real positive and negative news.