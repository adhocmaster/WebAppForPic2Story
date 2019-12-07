from keras.models import load_model
import tensorflow as tf
from classifiers.TFModel import TFModel
from library.Configuration import Configuration

class Classifiermanager:

    def __init__(self, configuration:Configuration):

        self.configuration = configuration

        self.models = {
            'DoodleClassifier': None,
            'GPT2': None
        }

        print(self.configuration.get('doodle.modelPath'))
        self.modelPaths = {
            
            'DoodleClassifier': {
                'modelPath': self.configuration.get('doodle.modelPath'),
                'weightPath': self.configuration.get('doodle.weightPath')
            },
            'GPT2': None
        }

        for key, val in self.modelPaths.items():
            if val is not None:
                self.load(key, val['modelPath'], val['weightPath'])



    def load(self, name, modelPath, weightPath):

        self.models[name] = TFModel(modelPath, weightPath)

    
    def get(self, name):
        return self.models[name]