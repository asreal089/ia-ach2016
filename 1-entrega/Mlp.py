import numpy as np

class MLP:

    def __init__(self, entrada, saida):
        np.random.seed(1)
        self.synapcticWeights = 2 * np.random.random((3,1)) -1
        self.entrada = entrada
        self.saida = saida

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
    
if __name__ == "__main__":
    mlp = MLP()
    print("pesos randomicos")
    print(mlp.synapcticWeights)

    trainingInputs = (self.entrada)
    trainingOutputs =(self.saida)

    mlp.train(trainingInput, trainingOutputs, 1000)