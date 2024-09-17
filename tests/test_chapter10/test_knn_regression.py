import numpy as np
import pytest
from src.chapter10.knn_regression import knn_regression, mean_squared_error, r2_score


def test_knn_regression() -> None:
    # Create a simple dataset
    X_train = np.array([[1], [2], [3], [4], [5]])
    y_train = np.array([2, 4, 5, 4, 5])
    X_test = np.array([[1.5], [3.5]])
    k = 2

    # Perform KNN regression
    y_pred = knn_regression(X_train, y_train, X_test, k)

    # Check if the output shape is correct
    assert y_pred.shape == (2,)

    # Check if the predictions are reasonable
    assert 2 < y_pred[0] < 4
    assert 4 < y_pred[1] < 5


def test_mean_squared_error() -> None:
    y_true = np.array([3, 5, 2, 7])
    y_pred = np.array([2.5, 5.0, 1.8, 7.2])

    mse = mean_squared_error(y_true, y_pred)

    # Check if the MSE is close to the expected value
    assert np.isclose(mse, 0.0825, atol=1e-4)


def test_r2_score() -> None:
    y_true = np.array([3, 5, 2, 7])
    y_pred = np.array([2.5, 5.0, 1.8, 7.2])

    r2 = r2_score(y_true, y_pred)

    # Check if the R2 score is close to the expected value
    assert np.isclose(r2, 0.9776, atol=1e-4)


def test_knn_regression_edge_cases() -> None:
    # Test with k=1
    X_train = np.array([[1], [2], [3]])
    y_train = np.array([1, 2, 3])
    X_test = np.array([[1.5], [2.5]])
    k = 1

    y_pred = knn_regression(X_train, y_train, X_test, k)
    assert np.allclose(y_pred, [1, 2])

    # Test with k equal to the number of training samples
    k = 3
    y_pred = knn_regression(X_train, y_train, X_test, k)
    assert np.allclose(y_pred, [2, 2])


def test_knn_regression_input_validation() -> None:
    X_train = np.array([[1], [2], [3]])
    y_train = np.array([1, 2, 3])
    X_test = np.array([[1.5], [2.5]])

    # Test with invalid k (k <= 0)
    with pytest.raises(ValueError):
        knn_regression(X_train, y_train, X_test, 0)

    # Test with mismatched X_train and y_train shapes
    with pytest.raises(ValueError):
        knn_regression(X_train, y_train[:-1], X_test, 2)

    # Test with different number of features in X_train and X_test
    with pytest.raises(ValueError):
        knn_regression(X_train, y_train, np.array([[1, 2], [3, 4]]), 2)
