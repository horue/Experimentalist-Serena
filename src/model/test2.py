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

        
        convertedDict.append(resultDict)


        userInputS = np.array(convertedDict, dtype=float)
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
            convertedDict.append(internalDict)


        frasesS = np.array(convertedDict, dtype=float)
        return frasesS


if __name__ == "__main__":
    Preparer.tokenizeInput("estou triste")
    print(Preparer.tokenizeDataset())
    Preparer.tokenizeDataset()