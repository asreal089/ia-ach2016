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
        for fileName in glob.glob(self.dirEntrada + '*.csv'):
            x = np.genfromtxt(fileName, delimiter=",")
            #inserir aqui chamada da função de saida.
            print(fileName)
            

st = Start()
st.runNMPL()