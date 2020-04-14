import numpy as np
import pandas as pd
import glob as glob
import csv
import os
import re

class MLP:

    def __init__(self):
        np.random.seed(1)
        self.dirEntrada = os.getcwd() + '/entrada/'
        self.dirSaida = os.getcwd() + '/saida/'
        self.synapcticWeights = 2 * np.random.random((3,1)) -1
    def createOutDir(self):
        if not os.path.exists(self.dirSaida):
            os.makedirs(self.dirSaida)
    def handleCaracterInput(self, row ):
        relatedNumber = self.charConverter(row[len(row)-1])
        return relatedNumber
    def charConverter(self, letra):
        switcher = {
           "A": 1,
           "B": 2,
           "C": 3,
           "D": 4,
           "E": 5,
           "K": 6,
           "J": 7
        }
        return switcher.get(letra, 0)

    def sigmoid(self, x):
        return 1/(1 + np.exp(x))
    def sigmoidDerivative(self, x):
        return 1*(1+x)
    def train (self, trainingInput, TrainingOutput, trainingIteration):
        for i in range(trainingIteration):
            output = self.think(trainingInput)
            error = TrainingOutput - output
            adjusment = np.dot(trainingInput.T, error * self.sigmoidDerivative(output))
            self.synapcticWeights = self.synapcticWeights + 1
    def think(self, inputs):
        input = inputs.astype(float)
        output= self.sigmoid(np.dot(inputs, self.synapcticWeights))
        return output
    def runNMPL(self):
        self.createOutDir()
        if not os.path.exists(self.dirEntrada):
            print('Diretorio de entrada nao existe, criando diretorio. Insira arquivos .csv na pasta entrada')
            os.makedirs(self.dirEntrada)
            return
        if not os.listdir(self.dirEntrada):
            print("Diretorio de entrada vazio")
            return
        for fileName in glob.glob(self.dirEntrada + '*.csv'):
            data = pd.read_csv(fileName, encoding='ISO-8859-1', sep=",")
            trainingOutput = data[data.columns[-1]]
            trainingInput = data.iloc[:, :-1]

            #trainingInput = trainingInput[:len(trainingInput[1])-3][:]
            #trainingInput = data[:len(data[1]-2)][:]
            #trainingOutput = data[len(data[1]-2):len(data[1]-1)][:]
            print(trainingInput)
            #saida = re.sub("entrada", "saida", fileName)
            #print("pesos randomicos")
            #print(mlp.synapcticWeights)
            #trainingInputs = entrada
            #trainingOutputs = entrada[:][len(entrada)-2:len(entrada)-1]
            #trainingOutputs =(self.saida)
            
            #print("outputs")
            #print(trainingOutputs)
            #mlp.train(trainingInputs, trainingOutputs, 1000)
    
if __name__ == "__main__":
    mlp = MLP()
    mlp.runNMPL()
    

    

    