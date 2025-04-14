"""Example usage of the code error detector."""

from pybughunt import CodeErrorDetector

def main():
    """Run examples of code error detection."""
    
    # Initialize the detector
    detector = CodeErrorDetector()
    
    # Example 1: Code with syntax error
    print("Example 1: Code with syntax error")
    code1 = '''
def hello():
    print("Hello, world!"
'''
    results1 = detector.analyze(code1)
    print(f"Syntax errors: {len(results1['syntax_errors'])}")
    print(f"Logic errors: {len(results1['logic_errors'])}")
    for error in results1["syntax_errors"]:
        print(f"  Line {error['line']}: {error['message']}")
    
    print("\n" + "-" * 40 + "\n")
    
    # Example 2: Code with logical error
    print("Example 2: Code with logical error")
    code2 = '''
def process_data():
    while True:
        print("Processing...")
        # No break statement - infinite loop
'''
    results2 = detector.analyze(code2)
    print(f"Syntax errors: {len(results2['syntax_errors'])}")
    print(f"Logic errors: {len(results2['logic_errors'])}")
    for error in results2["logic_errors"]:
        print(f"  Line {error['line']}: {error['message']}")
    
    print("\n" + "-" * 40 + "\n")
    
    # Example 3: Code with unused variable
    print("Example 3: Code with unused variable")
    code3 = '''
def calculate():
    x = 10  # This variable is unused
    return 42
'''
    results3 = detector.analyze(code3)
    print(f"Syntax errors: {len(results3['syntax_errors'])}")
    print(f"Logic errors: {len(results3['logic_errors'])}")
    for error in results3["logic_errors"]:
        print(f"  Line {error['line']}: {error['message']}")
        
    # Get fix suggestions
    suggestions = detector.fix_suggestions(code3, results3)
    print("\nSuggested fixes:")
    for error_key, suggestion in suggestions.items():
        print(f"  {error_key}: {suggestion}")

if __name__ == "__main__":
    main()