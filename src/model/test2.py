import tensorflow as tf
import pandas as pd
import numpy as np


class Dataset():
    csvPath = r"src\data\dataset.csv"
    dataset = pd.read_csv(csvPath)
    datasetFrases = dataset["frase"]
    datasetPoints = dataset["label"].to_list()


class Preparer:
    def tokenizeInput(data: str):
        text_vectorization_layer = tf.keras.layers.TextVectorization(
            max_tokens=1000,
            output_mode='int'
        )

        text_vectorization_layer.adapt(Dataset.datasetFrases)
        output = text_vectorization_layer(data)
        print(output)

        resultDict = output.numpy()
        convertedDict = []

        
        valueSum = resultDict.cumsum()[-1]
        convertedDict.append(valueSum)


        userInputS = np.array(convertedDict, dtype=float)
        print(userInputS)
        return userInputS

    def tokenizeDataset():
        #print(datasetFrases)
        #print(datasetPoints)

        text_vectorization_layer = tf.keras.layers.TextVectorization(
            max_tokens=1000,
            output_mode='int'
        )



        text_vectorization_layer.adapt(Dataset.datasetFrases)
        output = text_vectorization_layer(Dataset.datasetFrases)

        resultDict = output.numpy()
        convertedDict = []

        for internalDict in resultDict:
            valueSum = internalDict.cumsum()[-1]
            convertedDict.append(valueSum)


        frasesS = np.array(convertedDict, dtype=float)
        print(frasesS)


Preparer.tokenizeInput("estou feliz")
Preparer.tokenizeDataset()