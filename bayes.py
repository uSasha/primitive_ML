import numpy as np


class NaiveBayes(object):
    def __init__(self):
        self.probabilities = []
        self.x = None
        self.y = None

    def fit(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)

    def _get_proba_multinom(self, feature, point, category):
        p_a = (self.y == category).sum() / len(self.y)
        p_ba = ((self.x[self.y == category][:, feature] == point[feature]).sum()
                / len(self.x[self.y == category]))
        p_b = (self.x[:, feature] == point[feature]).sum() / len(self.x) + 1e-100
        return p_a * p_ba / p_b

    def predict(self, x):
        result = []
        for point in x:
            probabilities = []
            for category in np.unique(self.y):
                category_prob = 1
                for feature in range(len(point)):
                    # category_prob *= self._get_proba_multinom(feature, point, category)
                    lol = self._get_proba_multinom(feature, point, category)
                    category_prob *= lol

                probabilities.append(category_prob)
            result.append(np.unique(self.y)[np.argmax(probabilities)])
        return result
