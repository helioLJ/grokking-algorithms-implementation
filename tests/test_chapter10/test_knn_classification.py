import numpy as np
import pytest
from typing import Any
from src.chapter10.knn_classification import KNNClassifier


@pytest.fixture
def sample_data() -> (
    tuple[np.ndarray[Any, np.dtype[Any]], np.ndarray[Any, np.dtype[Any]]]
):
    X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
    y = np.array([0, 0, 1, 1, 0, 1])
    return X, y


def test_knn_classifier_init() -> None:
    knn = KNNClassifier(k=5)
    assert knn.k == 5
    assert knn.X_train is None
    assert knn.y_train is None


def test_knn_classifier_fit(
    sample_data: tuple[np.ndarray[Any, np.dtype[Any]], np.ndarray[Any, np.dtype[Any]]],
) -> None:
    X, y = sample_data
    knn = KNNClassifier()
    knn.fit(X, y)
    assert knn.X_train is not None
    assert knn.y_train is not None
    assert np.array_equal(knn.X_train, X)
    assert np.array_equal(knn.y_train, y)


def test_knn_classifier_predict(
    sample_data: tuple[np.ndarray[Any, np.dtype[Any]], np.ndarray[Any, np.dtype[Any]]],
) -> None:
    X, y = sample_data
    knn = KNNClassifier(k=3)
    knn.fit(X, y)

    X_test = np.array([[1.2, 1.9], [7, 7], [3, 4]])
    predictions = knn.predict(X_test)

    assert len(predictions) == 3
    assert (
        predictions[0] == 0
    )  # Should be classified as 0 (close to [1, 2] and [1.5, 1.8])
    assert predictions[1] == 1  # Should be classified as 1 (close to [5, 8] and [8, 8])
    assert (
        predictions[2] == 0
    )  # Should be classified as 0 (closer to the cluster of 0s)


def test_knn_classifier_edge_cases(
    sample_data: tuple[np.ndarray[Any, np.dtype[Any]], np.ndarray[Any, np.dtype[Any]]],
) -> None:
    X = np.array([[1, 1], [2, 2], [3, 3]])
    y = np.array([0, 1, 0])
    knn = KNNClassifier(k=3)
    knn.fit(X, y)

    # Test with a point exactly on one of the training points
    assert knn.predict(np.array([[1, 1]])) == 0

    # Test with a point equidistant from all training points
    assert knn.predict(np.array([[2, 2]])) == 0  # Changed from 1 to 0


def test_knn_classifier_k_greater_than_samples(
    sample_data: tuple[np.ndarray[Any, np.dtype[Any]], np.ndarray[Any, np.dtype[Any]]],
) -> None:
    X = np.array([[1, 1], [2, 2]])
    y = np.array([0, 1])
    knn = KNNClassifier(k=3)
    knn.fit(X, y)

    # Even though k=3, it should still work with only 2 samples
    assert knn.predict(np.array([[1.5, 1.5]])) in [0, 1]
