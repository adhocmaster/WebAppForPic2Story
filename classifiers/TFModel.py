from keras.models import model_from_json, load_model
from tensorflow import Graph
import tensorflow as tf
import numpy as np

class TFModel:

    def __init__(self, modelPath, weightPath):

        print(modelPath)
        print(weightPath)

        self.graph = tf.Graph()

        with self.graph.as_default():
            self.session = tf.Session(graph=self.graph)
            
            with self.session.as_default():
                # with open(modelPath, 'r', encoding='utf-8') as f:
                #     self.model = model_from_json(f.read())
                self.model = load_model(modelPath)
                self.model.load_weights(weightPath)
                
    
    def predictClassIndex(self, input):

        input = np.expand_dims(input, axis=0)
        print(f'input shape: {input.shape}')
        with self.graph.as_default():
            with self.session.as_default():
                probs = self.model.predict(input, batch_size=1)
                # result = self.model.predict(input, batch_size=1)

        return np.argmax(probs)      
