import unittest2
from classifiers.ClassifierManager import Classifiermanager
from dataProcessors.DoodleDataStats import DoodleDataStats
from library.Configuration import Configuration
import numpy as np

class DoodleTest(unittest2.TestCase):

    def testDoodle(self):

        configuration = Configuration()
        print(configuration.get('doodle.modelPath'))
        print(configuration.get('doodle.weightPath'))
        print(configuration.get('doodle.stats'))
        dataStats = DoodleDataStats()
        dataStats.load(configuration.get('doodle.stats'))
        classifierManager = Classifiermanager(configuration)
        classes = list(dataStats.stats['classes'].keys())
        imgStr = "0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  11  21  12   0   0   0   0   0   0   0   0  92  20   0   0   0   0   0   0   0   0   0   0   0   0   0  91 213 253 255 255 222  95   3   0   0   0   0   7 255 222   0   0   0   0   0   0   0   0   0   0   0  24 190 255 196 118 100 109 196 255 121   0   0   0   0   0 141  35   0   0   0   0   0   0   0   0   0   0   1 185 241  94   1   0   0   0   0  63  25   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  89 255 115 133 150  37   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0 207 241 252 255 250 199   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  30 200 255 242 149 252 232 195   3   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  39 225 238 255  85   0 119 255  83   0   0   0   0   0   0   0   0   0   0  0   0   0   0   0   0   0   0  43 229 231 106 255  49   0   1 201 222   7   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  33 237 220  33  79 255  75   0   0  61 255  94   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   4 197 235  28   0   4 210 166   0   0   1 250 127   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0 128 255  85   0   0   0  17  16   0   0   0 231 146   0   0   0   0   0   0   0   0   0   0   0   0   0   0  56 251 153   0   0   0   0   0   0   0   0   0 228 148   0   0   0   0   0   0   0   0   0   0   0   0   0   0 162 229  11   0   0   0   0   0   0   0   0   0 246 131   0   0   0   0   0   0   0   0   0   0   0   0   0   0 219 165   0   0   0   0   0   0   0   0   0  13 255 111   0   0   0   0   0   0   0   0   0   0   0   0   0  21 254 109   0   0   0   0   0   0   0   0   0  78 255  58   0   0   0   0   0   0   0   0   0   0   0   0   0  78 255  51   0   0   0   0   0   0   0   0   0 152 237   3   0   0   0   0   0   0    0   0   0   0   0   0   0 120 254   5   0   0   0   0   0   0   0   0   3 228 165   0   0   0   0   0   0   0   0   0   0   0   0   0   0 123 254   0   0   0   0   0   0   0   0   0  72 255  74   0   0   0   0   0   0   0   0   0   0   0   0   0   0 114 255  13   0   0   0   0   0   0   0   0 169 229   3   0   0   0   0   0   0   0   0   0   0   0   0   0   0  60 255  70   0   0   0   0   0   0   0  53 252 129   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   7 239 174   0   0   0   0   0   0   6 208 222  11   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0 110 255 100   0   0   0   0   3 170 253  70   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   3 180 255 178  99  68  91 200 254 104   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   2 116 222 255 255 255 213  87   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  32  51  44   1   0   0   0   0   0   0   0   0   0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0"
        
        sep = ' '

        img = np.fromstring(imgStr, dtype=float, sep=sep).reshape(28,28,1) / 255

        print(img.shape)

        model = classifierManager.get('DoodleClassifier')

        prediction = model.predictClassIndex(img)

        print(prediction.shape)

        print(prediction)
        print(classes[prediction])