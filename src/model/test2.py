import tensorflow as tf
import pandas as pd
import numpy

csvPath = r"src\data\dataset.csv"
sentences = ["eu gosto de sorvete.", "você também gosta de sorvete?"]
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

for internalDict in resultDict:
    print(internalDict.cumsum())


#print("Vectorized Output:", output.numpy())