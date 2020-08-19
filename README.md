# faiza-bot

I guess it works.
The model uses a decision tree to predict a disease given particular symptoms. The dataset used can be found here : https://www.kaggle.com/itachi9604/disease-symptom-description-dataset?rvi=1
The encoder is a universal LabelEncoder which is made everytime a new model is trained as the encodings are different each time. Can't help it.

P.s : Use python3 to run.

Right now there is no script to encode inputs. So, if you load the model, either load the encoder too, or give an input as [[23,43,23....]] which has to be a 17 dimensional vector.
Peace.
