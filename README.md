# Grokking Algorithms Implementation

This repository contains implementations of algorithms from the book "Grokking Algorithms" by Aditya Bhargava, along with corresponding unit tests.


## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/grokking_algorithms.git
   cd grokking_algorithms
   ```

2. Set up a virtual environment using [uv](https://docs.astral.sh/uv/getting-started/installation/) (optional but recommended):

3. Install dependencies:
   ```
   uv sync
   ```

## Implementing Algorithms

1. Navigate to the appropriate chapter directory in `src/`.
2. Implement the algorithm in the corresponding Python file.
3. Run the tests to verify your implementation.

## Running Tests

To run all tests:
```python
pytest
```

To run tests for a specific chapter, navigate to the chapter directory and run:
```python
pytest tests/test_chapterX
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Implement your changes and add tests if necessary
4. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Aditya Bhargava for the book "Grokking Algorithms"
- All contributors to this project