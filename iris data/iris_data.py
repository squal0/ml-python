from matplotlib import pyplot as plt
import numpy as np

#load the data with load_iris from sklearn
from sklearn.datasets import load_iris

data = load_iris()

#load_iris returns an object with several fields
features = data.data
feature_names = data.feature_names
target = data.target
target_names = data.target_names

for t in range(3):
    if t == 0:
        c = 'r'
        marker = '>'

    elif t == 1:
        c = 'g'
        marker = 'o'

    elif t == 2:
        c = 'b'
        marker = 'x'

    plt.scatter(features[target == t, 0],
                features[target == t, 1],
                marker = marker,
                c = c)

#use numpy indexing to get an array of strings
labels = target_names[target]

#The petal length is the feature at position 2
plength = features[:, 2]

#Build an array of booleans
is_setosa = (labels == 'setosa')

#important step take note
max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()
print ('Maximum of setosa: {0}.'.format(max_setosa))
print ('Minimum of others: {0}.'.format(min_non_setosa))

#first select only the non-setosa features and labels
# ~ is the boolean negation operator
features = features[~is_setosa]
labels = labels[~is_setosa]

#build a new target variable, is_virginica
is_virginica = (labels == 'virginica')

#initialize best accuracy to impossibly low value
best_acc = -1.0
for f1 in range(features.shape[1]):
    #testing all possible thresholds
    thresh = features[:, f1]
    for t in thresh:
        #get the vector features for f1
        feature_1 = features[:, f1]
        #apply threshold 't'
        pred  = (feature_1 > t)
        acc = (pred == is_virginica).mean()
        rev_acc = (pred == ~is_virginica).mean()

        if rev_acc > acc:
            reverse = True
            acc = rev_acc
        else:
            reverse = False

        if acc > best_acc:
            best_acc = acc
            best_f1 = f1
            best_t = t
            best_reverse = reverse

def is_virginica_test(f1, t, reverse, example):
    'apply threshold model to new example'
    test = example[f1] > t
    if reverse:
        test = not test
    return test

from threshold import fit_model, predict

# training accuracy was 96.0%.
# testing accuracy was 90.0% (N = 50).

correct = 0.0
for ei in range(len(features)):
    #select all but one at position 'ei':
    training = np.ones(len(features), bool)
    training[ei] = False
    testing = ~training
    model = fit_model(features[training], is_virginica[training])
    predictions = predict(model, features[testing])
    correct += np.sum(predictions == is_virginica[testing])
    
acc = correct / float(len(features))
print ('Accuracy: {0:.1%}'.format(acc))
