import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import random
import sys
import csv

sentiments = []
content = []
genre1l = []
genre2l = []
temp = []
mdict = {}
x = []
args = ""

for i in range(1, len(sys.argv)):
	args += str(sys.argv[i]) + " "

x.append(args)

dataframe = pd.read_csv('./text_emotion.csv', encoding = 'latin-1')

#convert dataframe to matrix
conv_df_arr = dataframe.values

#split matrix into 3 columns each into 1d array
sentiments = np.delete(conv_df_arr,[0, 2, 3], axis = 1)
content = np.delete(conv_df_arr,[0, 1, 2], axis = 1)

#converting into 1D array
sentiments = sentiments.ravel().tolist()
content = content.ravel().tolist()

vectorizer = CountVectorizer(
    analyzer = 'word',
    lowercase = False,
)

features = vectorizer.fit_transform(
    content
)
features_nd = features.toarray()

X_train, X_test, y_train, y_test = train_test_split(
        features_nd,
        sentiments,
        train_size = 0.5,
        random_state = 1234)

log_model = LogisticRegression()
log_model = log_model.fit(X = X_train, y = y_train)
X_test = vectorizer.transform(x)
y_pred = log_model.predict(X_test)
print(y_pred)

if (y_pred == "anger"):
    genre1 = "Rock"
    genre2 = "Loud-Rock"
if (y_pred == "boredom"):
    genre1 = "Avant-Garde"
    genre2 = "Experimental Pop"
if (y_pred == "empty"):
    genre1 = "Field Recordings"
    genre2 = "Noise"
if (y_pred == "enthusiasm"):
    genre1 = "Pop"
    genre2 = "Electronic"
if (y_pred == "fun"):
    genre1 = "Krautrock"
    genre2 = "Folk"
if (y_pred == "happiness"):
    genre1 = "Hip-Hop"
    genre2 = ""
if (y_pred == "hate"):
    genre1 = "Metal"
    genre2 = ""
if (y_pred == "love"):
    genre1 = "Jazz"
    genre2 = ""
if (y_pred == "neutral"):
    genre1 = "Post-Rock"
    genre2 = ""
if (y_pred == "relief"):
    genre1 = "Post-Punk"
    genre2 = ""
if (y_pred == "sadness"):
    genre1 = "Lo-Fi"
    genre2 = ""
if (y_pred == "surprise"):
    genre1 = "Punk"
    genre2 = ""
if (y_pred == "worry"):
    genre1 = "Blues"
    genre2 = ""

asdf = "hello"
print(asdf == "")

with open('./fma_metadata/raw_tracks_mod.csv') as datafile:
    csvReader = csv.reader(datafile, delimiter = '\n')
    for row in csvReader:
        print(row[0])
        # if (row[9][0]['genre_title'] == genre1):
        #     genre1l.append(row[0])
        # if (row[9][0]['genre_title'] == genre2):
        #     genre2l.append(row[0])

sys.stdout.flush();
# print(len(X_test))
# j = random.randint(0, len(X_test) - 25)
# for i in range(j, j + 25):
#     print(y_pred[i])
#     ind = features_nd.tolist().index(X_test[i].tolist())
#     print(content[ind].strip())
