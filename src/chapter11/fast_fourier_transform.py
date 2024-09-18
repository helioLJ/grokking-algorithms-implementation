import cmath
import numpy as np
from typing import Sequence, Union


def fast_fourier_transform(x: Sequence[Union[int, float]]) -> Sequence[complex]:
    """
    Compute the Fast Fourier Transform (FFT) of the input sequence.

    This function implements the Cooley-Tukey FFT algorithm, which has a time complexity of O(n log n).

    Args:
        x (Sequence[Union[int, float]]): The input sequence of real numbers.

    Returns:
        Sequence[complex]: The FFT of the input sequence.

    Raises:
        ValueError: If the input length is not a power of 2.
    """
    n = len(x)
    if n <= 1:
        return [complex(val) for val in x]  # Convert to complex for the base case
    if n & (n - 1) != 0:
        raise ValueError("Input length must be a power of 2")

    # Divide
    even = fast_fourier_transform(x[0::2])
    odd = fast_fourier_transform(x[1::2])

    # Combine
    T = [cmath.exp(-2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + T[k] for k in range(n // 2)] + [
        even[k] - T[k] for k in range(n // 2)
    ]


def inverse_fast_fourier_transform(x: Sequence[complex]) -> Sequence[complex]:
    """
    Compute the Inverse Fast Fourier Transform (IFFT) of the input sequence.

    This function uses the FFT algorithm to compute the IFFT by conjugating the input,
    applying FFT, and then conjugating and scaling the result.

    Args:
        x (Sequence[complex]): The input sequence of complex numbers.

    Returns:
        Sequence[complex]: The IFFT of the input sequence.
    """
    n = len(x)
    conjugated = [np.conj(val) for val in x]
    fft_result = fast_fourier_transform(conjugated)
    return [np.conj(val) / n for val in fft_result]
