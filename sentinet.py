import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import random
import sys

sentiments = []
content = []
x = []
args = ""

for i in range(1, len(sys.argv)):
	args += str(sys.argv[i]) + " "

x.append(args)

dataframe = pd.read_csv('./text_emotion.csv', encoding = 'latin-1')

#convert dataframe to matrix
conv_arr = dataframe.values

#split matrix into 3 columns each into 1d array

sentiments = np.delete(conv_arr,[0, 2, 3], axis = 1)
content = np.delete(conv_arr,[0, 1, 2], axis = 1)

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
sys.stdout.flush();
# print(len(X_test))
# j = random.randint(0, len(X_test) - 25)
# for i in range(j, j + 25):
#     print(y_pred[i])
#     ind = features_nd.tolist().index(X_test[i].tolist())
#     print(content[ind].strip())
