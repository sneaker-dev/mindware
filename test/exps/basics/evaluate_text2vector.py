import numpy as np
import os
import sys

sys.path.append(os.getcwd())

from solnml.components.feature_engineering.transformations.preprocessor.text2vector import \
    Text2VectorTransformation
from solnml.components.feature_engineering.transformation_graph import DataNode
from solnml.components.utils.constants import *
from solnml.estimators import Classifier

x = np.array([[1, 'I am good', 'I am right', 3], [2, 'He is good', 'He is ok', 4],
              [2.5, 'Everyone is good', 'Everyone is ok', 7], [1.3333, 'well', 'what', 5]])
y = np.array([0, 1, 0, 1])

t2v = Text2VectorTransformation()
data = (x, y)
feature_type = [NUMERICAL, TEXT, TEXT, DISCRETE]
datanode = DataNode(data, feature_type)

clf = Classifier(time_limit=20,
                 enable_meta_algorithm_selection=False,
                 include_algorithms=['random_forest'])

clf.fit(datanode)
