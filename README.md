# Code Error Detector

A Python library for detecting logical and syntactical errors in Python code.

## Features

- Syntax error detection and analysis
- Logical error detection using pattern-based and machine learning approaches
- Command-line interface for analyzing Python files
- Training capabilities for custom error detection models

## Installation

```bash
# Install from source
git clone https://github.com/Preksha-7/python-library.git
cd python-library
pip install -e .
```

## Usage

### Command Line

```bash
# Analyze Python files
code_error_detector analyze file1.py file2.py

# Analyze with custom model
code_error_detector analyze file1.py --model path/to/model.pkl

# Output in JSON format
code_error_detector analyze file1.py --format json --output results.json

# Train a new model
code_error_detector train --dataset path/to/dataset --output path/to/model.pkl
```

### Python API

```python
from code_error_detector import CodeErrorDetector

# Initialize the detector
detector = CodeErrorDetector()

# Analyze code
code = '''
def example():
    print("Hello, world!"
'''
results = detector.analyze(code)

# Get fix suggestions
if results["syntax_errors"] or results["logic_errors"]:
    errors = results["syntax_errors"] + results["logic_errors"]
    suggestions = detector.fix_suggestions(code, results)
    for error_key, suggestion in suggestions.items():
        print(f"Suggestion for {error_key}: {suggestion}")
```

## Supported Error Types

### Syntax Errors

- Missing parentheses, brackets, or braces
- Indentation errors
- Invalid syntax
- Unterminated string literals

### Logical Errors

- Infinite loops (while True without break)
- Unused variables
- Potential off-by-one errors
- Division by zero
- Unreachable code

## License

MIT
