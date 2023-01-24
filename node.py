class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None, depth=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value
        self.depth = depth

    def is_leaf(self):
        return self.value is not None
