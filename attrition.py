import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

ann = tf.keras.models.load_model('AttritionANN')

# dataset = pd.read_csv('web/sample.csv')

def predict_attrition(input_filepath, output_filepath):
    dataset = pd.read_csv(input_filepath)
    dataset_final = pd.read_csv(input_filepath)
    dataset = dataset.drop(["Over18"], axis = 1)
    dataset = dataset.values

    le1 = LabelEncoder()
    dataset[: ,10] = le1.fit_transform(dataset[:, 10])

    ct1 = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder= "passthrough")
    dataset = np.array(ct1.fit_transform(dataset))

    ct2 = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [8])], remainder= "passthrough")
    dataset = np.array(ct2.fit_transform(dataset))

    ct3 = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [11])], remainder= "passthrough")
    dataset = np.array(ct3.fit_transform(dataset))

    ct4 = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [23])], remainder= "passthrough")
    dataset = np.array(ct4.fit_transform(dataset))

    ct5 = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [33])], remainder= "passthrough")
    dataset = np.array(ct5.fit_transform(dataset))

    le2 = LabelEncoder()
    dataset[: ,-13] = le2.fit_transform(dataset[:, -13])

    dataset = StandardScaler().fit_transform(dataset)

    results = ann.predict(dataset)
    results = (results > 0.5)
    results = pd.DataFrame(results, columns=['Attrition Results'])

    results = pd.concat([dataset_final, results], axis=1)
    if (results.to_csv(output_filepath)):
        return 'Results Predicted'
    else:
        return 'Input Error'



