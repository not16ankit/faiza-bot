import joblib
from sklearn.metrics import classification_report
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
class waddle:
     def add_data(self):
         self.data = pd.read_csv("dataset.csv");
         self.data.fillna("rexa",inplace=True)
         self.sim = self.data['Symptom_1']
         for i in range(1,18):
              self.data['Symptom_'+str(i)] = self.data['Symptom_'+str(i)].str.strip() 
              if(i!=1):
                  self.sim = self.sim.append(self.data['Symptom_'+str(i)])


     def preprocess_data(self):
           le = LabelEncoder().fit(self.sim)
           joblib.dump(le,"encoder.pkl")
           for i in range(1,18):
                 self.data['Symptom_'+str(i)] = le.transform(self.data['Symptom_'+str(i)])

           X = self.data.drop("Disease",axis=1)
           Y = self.data['Disease']
           f = open("simps.txt","r+")
           for r in le.classes_:
                 f.write(r+"\n")

           f.close()
           self.train(X,Y)



     def train(self,X,Y):
          faiza = DecisionTreeClassifier()
          faiza.fit(X,Y)
          joblib.dump(faiza,"faiza.pkl")



waddle = waddle()
waddle.add_data()
waddle.preprocess_data()
