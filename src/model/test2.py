import tensorflow as tf
import pandas as pd
import numpy as np

class Preparer:
    def tokenize():
        csvPath = r"src\data\dataset.csv"
        dataset = pd.read_csv(csvPath)
        datasetFrases = dataset["frase"]
        datasetPoints = dataset["label"].to_list()


        #print(datasetFrases)
        #print(datasetPoints)

        text_vectorization_layer = tf.keras.layers.TextVectorization(
            max_tokens=1000,
            output_mode='int'
        )



        text_vectorization_layer.adapt(datasetFrases)
        output = text_vectorization_layer(datasetFrases)

        resultDict = output.numpy()
        convertedDict = []

        for internalDict in resultDict:
            valueSum = internalDict.cumsum()[-1]
            convertedDict.append(valueSum)


        frasesS = np.array(convertedDict, dtype=float)
        print(frasesS)


Preparer.tokenize()