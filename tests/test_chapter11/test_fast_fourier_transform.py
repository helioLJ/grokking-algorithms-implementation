import pytest
import numpy as np
from src.chapter11.fast_fourier_transform import (
    fast_fourier_transform,
    inverse_fast_fourier_transform,
)


def test_fast_fourier_transform() -> None:
    # Test with a simple sequence
    x = [1, 2, 3, 4]
    expected = np.fft.fft(x)
    result = fast_fourier_transform(x)
    np.testing.assert_allclose(result, expected, rtol=1e-10, atol=1e-10)

    # Test with a longer sequence
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    expected = np.fft.fft(x)
    result = fast_fourier_transform(x)
    np.testing.assert_allclose(result, expected, rtol=1e-10, atol=1e-10)


def test_fast_fourier_transform_invalid_input() -> None:
    # Test with input length not a power of 2
    with pytest.raises(ValueError):
        fast_fourier_transform([1, 2, 3])


def test_inverse_fast_fourier_transform() -> None:
    # Test IFFT with a simple sequence
    x = [1, 2, 3, 4]
    fft_result = fast_fourier_transform(x)
    ifft_result = inverse_fast_fourier_transform(fft_result)
    np.testing.assert_allclose(ifft_result, x, rtol=1e-10, atol=1e-10)

    # Test IFFT with a longer sequence
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    fft_result = fast_fourier_transform(x)
    ifft_result = inverse_fast_fourier_transform(fft_result)
    np.testing.assert_allclose(ifft_result, x, rtol=1e-10, atol=1e-10)


def test_fft_ifft_roundtrip() -> None:
    # Test FFT followed by IFFT to ensure we get back the original sequence
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    fft_result = fast_fourier_transform(x)
    ifft_result = inverse_fast_fourier_transform(fft_result)
    np.testing.assert_allclose(ifft_result, x, rtol=1e-10, atol=1e-10)
