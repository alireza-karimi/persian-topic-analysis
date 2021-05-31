import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, svm
from sklearn.metrics import accuracy_score
from hazm import *


class SVMModel:

    def __init__(self, data):
        self.data = data

    def text_normalizer(self):
        text_normalizer = Normalizer()
        self.data.x.dropna(inplace=True)
        self.data.x = [text_normalizer.normalize(i) for i in self.data.x]

    def train_test_split(self):
        train_data, test_data = train_test_split(self.data, train_size=0.8)
        self.y_train = train_data.y
        self.x_train = train_data.x
        self.y_test = test_data.y
        self.x_test = test_data.x

    def label_encoder(self):
        self.encoder = LabelEncoder()
        self.y_train_encoded = self.encoder.fit_transform(self.y_train)
        self.y_test_encoded = self.encoder.fit_transform(self.y_test)

    def perform_tfidf(self):
        self.Tfidf_vect = TfidfVectorizer(max_features=5000)
        self.Tfidf_vect.fit(self.data.x)
        self.x_train_tfidf = self.Tfidf_vect.transform(self.x_train)
        self.x_test_tfidf = self.Tfidf_vect.transform(self.x_test)

    def train_model(self):
        self.text_normalizer()
        self.train_test_split()
        self.label_encoder()
        self.perform_tfidf()
        self.svm_model = svm.SVC()
        self.svm_model.fit(self.x_train_tfidf, self.y_train_encoded)

    def model_acuraccy(self):
        self.train_model()
        svm_prediction = self.svm_model.predict(self.x_test_tfidf)
        return accuracy_score(svm_prediction, self.y_test_encoded)

    def predict(self, text):
        input = [text]
        prediction = self.svm_model.predict(self.Tfidf_vect.transform(input))
        return self.encoder.inverse_transform(prediction)[0]

    def normalize_and_predict(self, text):
        text_normalizer = Normalizer()
        text = text_normalizer.normalize(text)
        input = [text]
        prediction = self.svm_model.predict(self.Tfidf_vect.transform(input))
        return self.encoder.inverse_transform(prediction)[0]


if __name__ == "__main__":
    file_address = 'dataset.csv'
    data = pd.read_csv(file_address, error_bad_lines=False, sep=";")
    data.columns = ['y', 'x']
    model = SVMModel(data)
    print(model.model_acuraccy())
    print(model.predict("ﺖﺳا ﻥایﻉیﺵ ﻝﻭا ﻡﺎﻣا یﻞﻋ ﺕﺮﻀﺣ"))
