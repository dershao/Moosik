import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import random as r
import sys
import csv
import json
import ast
import pickle

sentiments = []
content = []
genre1l = []
genre2l = []
genre1 = ""
genre2 = ""
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

filename = 'finalized_model.sav'
pickle.dump(log_model, open(filename, 'wb'))

print(y_pred[0])

if (y_pred[0] == "anger"):
    genre1 = "Rock"
    genre2 = "Loud-Rock"
if (y_pred[0] == "boredom"):
    genre1 = "Avant-Garde"
    genre2 = "Experimental Pop"
if (y_pred[0] == "empty"):
    genre1 = "Field Recordings"
    genre2 = "Noise"
if (y_pred[0] == "enthusiasm"):
    genre1 = "Pop"
    genre2 = "Electronic"
if (y_pred[0] == "fun"):
    genre1 = "Krautrock"
    genre2 = "Folk"
if (y_pred[0] == "happiness"):
    genre1 = "Electronic"
    genre2 = "Hip-Hop"
if (y_pred[0] == "hate"):
    genre1 = "Metal"
    genre2 = ""
if (y_pred[0] == "love"):
    genre1 = "Jazz"
    genre2 = ""
if (y_pred[0] == "neutral"):
    genre1 = "Punk"
    genre2 = "Experimental Pop"
if (y_pred[0] == "relief"):
    genre1 = "Post-Punk"
    genre2 = ""
if (y_pred[0] == "sadness"):
    genre1 = "Lo-Fi"
    genre2 = ""
if (y_pred[0] == "surprise"):
    genre1 = "Punk"
    genre2 = ""
if (y_pred[0] == "worry"):
    genre1 = "Blues"
    genre2 = ""

with open('./raw_tracks_mod.csv') as datafile:
	count = 0
	csvReader = csv.reader(datafile)
	for row in csvReader:
		if (count == 0):
			count += 1
			continue
		genres = ast.literal_eval(row[27])
		if (genres[0]['genre_title'] == genre1):
			genre1l.append({'image': row[28], 'trackUrl': row[38]})
		elif (genres[0]['genre_title'] == genre2):
			genre2l.append({'image': row[28], 'trackUrl': row[38]})

randomGenreChoice = r.randint(0,2)
if (genre2 == ""):
	randomGenreChoice = 1

if (randomGenreChoice == 1):
	randomSongChoice = r.randint(0, len(genre1l) - 1)
	randomSong = genre1l[randomSongChoice]
	print(randomSong['image'])
	print(randomSong['trackUrl'])
else:
	randomSongChoice = r.randint(0, len(genre2l) - 1)
	randomSong = genre2l[randomSongChoice]
	print(randomSong['image'])
	print(randomSong['trackUrl'])

sys.stdout.flush();
# print(len(X_test))
# j = random.randint(0, len(X_test) - 25)
# for i in range(j, j + 25):
#     print(y_pred[i])
#     ind = features_nd.tolist().index(X_test[i].tolist())
#     print(content[ind].strip())
