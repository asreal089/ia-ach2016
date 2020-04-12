import numpy as np
import pandas as pd
import glob as glob
import os

class Start:
    def __init__(self):
        self.dirEntrada = os.getcwd() + '/entrada/'
        self.dirSaida = os.getcwd() + '/saida/'
    def createOutDir(self):
        if not os.path.exists(self.dirSaida):
            os.makedirs(self.dirSaida)
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
            x = np.genfromtxt(fileName, delimiter=",")
            print(fileName)
            

st = Start()
st.runNMPL()