import numpy as np
from node import Node
from collections import Counter


class DecisionTreeClassifier:
    def __init__(self, max_depth=100, n_features=None, min_samples_split=2, criterion="gini"):
        self.n_features = n_features
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.criterion = criterion
        self.root = None
        self.__tree = None

    def fit(self, features, labels):
        self.n_features = features.shape[1] if not self.n_features else min(
            self.n_features, features.shape[1])

        self.root = self.__build_tree(features, labels)

    def __build_tree(self, features, labels, depth=0):
        row_size, column_size = features.shape
        n_labels = len(np.unique(labels))

        if (depth >= self.max_depth) or (n_labels == 1) or (row_size < self.min_samples_split):
            value = self._most_common_label(labels)
            return Node(value=value, depth=depth)

        feature_indexes = np.random.choice(
            column_size, self.n_features, replace=False)

        best_feature, best_threshold = self.__best_split(
            features, labels, feature_indexes)

        left_indexes, right_indexes = self.__split(
            features[:, best_feature], best_threshold)

        left = self.__build_tree(
            features[left_indexes], labels[left_indexes], depth + 1)

        right = self.__build_tree(
            features[right_indexes], labels[right_indexes], depth + 1)

        return Node(best_feature, best_threshold, left, right, depth=depth)

    def _most_common_label(self, features):
        counter = Counter(features)
        return counter.most_common(1)[0][0]

    def __best_split(self, features, labels, feature_indexes):
        best_gain = -1
        split_index = None
        split_threshold = None

        for feature_index in feature_indexes:
            column = features[:, feature_index]
            thresholds = np.unique(column)

            for threshold in thresholds:
                gain = self.__calculate_information_gain(
                    labels, column, threshold)

                if gain > best_gain:
                    best_gain = gain
                    split_index = feature_index
                    split_threshold = threshold

        return split_index, split_threshold

    def __split(self, column, threshold):
        left_indexes = np.argwhere(column <= threshold).flatten()
        right_indexes = np.argwhere(column > threshold).flatten()
        return left_indexes, right_indexes

    def __calculate_information_gain(self, labels, column, threshold):

        if self.criterion == "entropy":
            criterion_function = self.__calculate_entropy
        if self.criterion == "gini":
            criterion_function = self.__calculate_gini

        impurity = criterion_function(labels)

        left_indexes, right_indexes = self.__split(column, threshold)

        if (len(left_indexes) == 0) or (len(right_indexes) == 0):
            return 0

        n_samples = len(labels)
        n_left_samples, n_right_samples = len(left_indexes), len(right_indexes)
        left_criterion = criterion_function(labels[left_indexes])
        right_criterion = criterion_function(labels[right_indexes])
        features_impurity = ((n_left_samples / n_samples) * left_criterion) + \
            ((n_right_samples / n_samples) * right_criterion)

        return impurity - features_impurity

    def __calculate_entropy(self, labels):
        _, counts = np.unique(labels, return_counts=True)
        ps = counts / len(labels)
        return -np.sum([p * np.log(p) for p in ps if p > 0])

    def __calculate_gini(self, labels):
        _, counts = np.unique(labels, return_counts=True)
        probabilities = counts / len(labels)
        return (probabilities * (1 - probabilities)).sum()

    def predict(self, features):
        return np.array([self.__traverse_tree(feature, self.root) for feature in features])

    def __traverse_tree(self, feature, node):
        if node.is_leaf():
            return node.value

        if feature[node.feature] <= node.threshold:
            return self.__traverse_tree(feature, node.left)

        return self.__traverse_tree(feature, node.right)

    def print_tree(self):
        self.__print_all_node(self.root)

    def __print_all_node(self, node):
        queue = [node]
        while len(queue) > 0:
            current = queue.pop(0)
            self.__print_node(current)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

    def __print_node(self, node):
        if node.is_leaf():
            print(f"depth: {node.depth}")
            print(f"value: {node.value}")
            print()
        else:
            print(f"depth: {node.depth}")
            print(f"feature: {node.feature}")
            print(f"threshold: {node.threshold}")
            print()
