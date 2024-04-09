import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import warnings
import pickle
warnings.filterwarnings("ignore")

#Read and separate the training data
EEG = pd.read_csv('lie-detection/RawWavesCombined.csv')
Y_EEG = EEG[['Lie/Truth']]
X_EEG = EEG[['EEG.AF3', 'EEG.T7', 'EEG.Pz', 'EEG.T8', 'EEG.AF4']]

X_train, X_test, Y_train, Y_test = train_test_split(X_EEG, Y_EEG, test_size= 0.15, random_state=8)
X_train, X_validation, Y_train, Y_validation = train_test_split(X_train, Y_train, test_size=0.20, random_state=8)

#model training
classifier = GradientBoostingClassifier(n_estimators=500, learning_rate=0.05, max_depth=7, random_state=0)
classifier.fit(X_train, Y_train)

pickle.dump(classifier,open('model.pkl', 'wb'))
model = pickle.load(open('model.pkl','rb'))