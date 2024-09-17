import numpy as np
from collections import Counter
from typing import Any


class KNNClassifier:
    def __init__(self, k: int = 3) -> None:
        """
        Initialize the KNN classifier with a specified number of neighbors.

        Parameters:
        k (int): Number of neighbors to use for classification.
        """
        self.k = k
        self.X_train: np.ndarray[Any, np.dtype[Any]] | None = None
        self.y_train: np.ndarray[Any, np.dtype[Any]] | None = None

    def fit(
        self, X: np.ndarray[Any, np.dtype[Any]], y: np.ndarray[Any, np.dtype[Any]]
    ) -> None:
        """
        Fit the KNN classifier with the training data.

        Parameters:
        X (np.ndarray): Training data features.
        y (np.ndarray): Training data labels.
        """
        self.X_train = X
        self.y_train = y

    def predict(
        self, X: np.ndarray[Any, np.dtype[Any]]
    ) -> np.ndarray[Any, np.dtype[Any]]:
        """
        Predict the labels for the given test data.

        Parameters:
        X (np.ndarray): Test data features.

        Returns:
        np.ndarray: Predicted labels for the test data.
        """
        return np.array([self._predict(x) for x in X])

    def _predict(self, x: np.ndarray[Any, np.dtype[Any]]) -> Any:
        """
        Predict the label for a single test data point.

        Parameters:
        x (np.ndarray): A single test data point.

        Returns:
        Any: Predicted label for the test data point.
        """
        if self.X_train is None or self.y_train is None:
            raise ValueError("Model not fitted. Call 'fit' before using 'predict'.")

        distances = np.sqrt(np.sum((self.X_train - x) ** 2, axis=1))
        k_indices = np.argsort(distances)[: self.k]
        k_nearest_labels = self.y_train[k_indices]

        # Handle ties by selecting the most frequent class
        # If there's still a tie, choose the class that appears first in the training set
        class_counts = Counter(k_nearest_labels)
        max_count = max(class_counts.values())
        most_common_classes = [
            cls for cls, count in class_counts.items() if count == max_count
        ]

        if len(most_common_classes) == 1:
            return most_common_classes[0]
        else:
            # If there's a tie, choose the class that appears first in the original training set
            for label in self.y_train:
                if label in most_common_classes:
                    return label
