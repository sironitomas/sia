import graphviz
import ipdb
import numpy as np
import pandas as pd
from sklearn import tree

def get_dataframe(filename):
    return pd.read_csv(filename, dtype='category')

def train_model():
    df = get_dataframe('mushrooms.csv')
    target_names = df.type.cat.categories

    for column in df.columns:
        df[column] = df[column].cat.codes

    Y = df['type'].to_numpy()
    del df['type']
    X = df.to_numpy()

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)

    return clf

def analysis(content):
    df = get_dataframe('mushrooms.csv')
    del df['type']
    clf = train_model()
    decoder = {}
    for column in df.columns:
        decoder[column] = {}
        for i, name in enumerate(df[column].cat.categories):
            decoder[column][name] = i
    query_list = []
    # ipdb.set_trace()
    for column in df.columns:
        query_list.append(decoder[column][content[column]])
    print(query_list)
    query_array = np.array(query_list)
    print(query_array)
    prediction = clf.predict([query_array])
    # ipdb.set_trace()
    if prediction[0] == 0:
        return 'e'
    else:
        return 'p'

if __name__ == '__main__':
    test = {
        'cap_shape': 'f',
        'cap_surface': 'g',
        'cap_color': 'n',
        'bruises': 'f',
        'odor': 'a',
        'gill_attachment': 'f',
        'gill_spacing': 'c',
        'gill_size': 'n',
        'gill_color': 'k',
        'stalk_shape': 't',
        'stalk_root': 'b',
        'stalk_surface_above_ring': 'y',
        'stalk_surface_below_ring': 's',
        'stalk_color_above_ring': 'c',
        'stalk_color_below_ring': 'w',
        'veil_type': 'p',
        'veil_color': 'o',
        'ring_number': 't',
        'ring_type': 'e',
        'spore_print_color': 'y',
        'population': 'a',
        'habitat': 'd'
    }
    analysis(test)
