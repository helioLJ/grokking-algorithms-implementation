import numpy as np
from numpy.typing import NDArray
from sklearn.neighbors import NearestNeighbors


def knn_regression(
    X_train: NDArray[np.float64],
    y_train: NDArray[np.float64],
    X_test: NDArray[np.float64],
    k: int,
) -> NDArray[np.float64]:
    """
    Perform K-Nearest Neighbors regression.
    """
    if k <= 0:
        raise ValueError("k must be greater than 0")
    if X_train.shape[0] != y_train.shape[0]:
        raise ValueError("X_train and y_train must have the same number of samples")
    if X_train.shape[1] != X_test.shape[1]:
        raise ValueError("X_train and X_test must have the same number of features")

    nn = NearestNeighbors(n_neighbors=k, metric="euclidean")
    nn.fit(X_train)

    distances, indices = nn.kneighbors(X_test)

    y_pred: NDArray[np.float64] = np.mean(y_train[indices], axis=1)

    return y_pred


def mean_squared_error(
    y_true: NDArray[np.float64], y_pred: NDArray[np.float64]
) -> np.float64:
    """
    Calculate the mean squared error between true and predicted values.

    Args:
        y_true (np.ndarray): True target values.
        y_pred (np.ndarray): Predicted target values.

    Returns:
        float: Mean squared error.
    """
    return np.float64(np.mean((y_true - y_pred) ** 2))


def r2_score(y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> np.float64:
    """
    Calculate the R-squared score between true and predicted values.
    """
    ss_total = np.sum((y_true - np.mean(y_true)) ** 2)
    ss_residual = np.sum((y_true - y_pred) ** 2)
    return np.float64(1 - (ss_residual / ss_total))
