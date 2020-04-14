import numpy as np
import pandas as pd
import glob as glob
import csv
import os
import Mlp as Mlp
import re


class Start:
    def __init__(self):
        self.dirEntrada = os.getcwd() + '/entrada/'
        self.dirSaida = os.getcwd() + '/saida/'
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
            entrada = np.genfromtxt(fileName, delimiter=",")
            
            if(re.search("caracteres", fileName)):
                with open(fileName) as file:
                    csvReader = csv.reader(file, delimiter=",")
                    index = 0
                    for row in csvReader:
                            
                        relatedNumber  = self.handleCaracterInput(row)
                        pFinal = len(entrada[index]) - 1
                        entrada[index][pFinal] = relatedNumber
                        index = index + 1

            saida = re.sub("entrada", "saida", fileName)
            #arquivoSaida = re.sub(".csv", "", saida)
            print(saida)
            mpl = Mlp.MLP( entrada, saida)

if __name__ == "__main__":
    st = Start()
    st.runNMPL()