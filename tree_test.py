import graphviz
import numpy as np
import pandas as pd
from sklearn import tree

df = pd.read_csv('mushrooms.csv', dtype='category')
target_names = df.type.cat.categories

for column in df.columns:
    df[column] = df[column].cat.codes

Y = df['type'].to_numpy()
del df['type']
X = df.to_numpy()

clf = tree.DecisionTreeClassifier(max_features=int)
clf = clf.fit(X, Y)

clf.predict([X[0]])
# import ipdb
# ipdb.set_trace()

dot_data = tree.export_graphviz(
    clf, out_file=None,
    feature_names=df.columns,
    class_names=target_names,
    filled=True, rounded=True,
    special_characters=True
)
graph = graphviz.Source(dot_data)
graph
graph.render("mushrooms")