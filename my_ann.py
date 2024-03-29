# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

#Categorical data is there ! need to make them numerical
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])

labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])

onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
X=X[:,1:]
 
# Splitting the dataset into the Training set and Test set
# library name has changed
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Actually making the ANN
import keras
from keras.models import Sequential #for initializing the neural network
from keras.layers import Dense # for making the layers

classifier= Sequential()
#triple click to select a line!
#adding the input layer and the hidden layers(actually making the hidden layer) (makes a random layer  with inputs and no. of nodes)Not square brackets !
classifier.add(Dense(units=6,kernel_initializer='uniform', activation='relu',input_dim=11))
classifier.add(Dense(units=6,kernel_initializer='uniform', activation='relu'))
classifier.add(Dense(units=1,kernel_initializer='uniform', activation='sigmoid'))

#compiling the ann( appling gradient decent)
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#Time to fit the the data to the model !
classifier.fit(X_train,y_train,batch_size=10,epochs=100)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)


