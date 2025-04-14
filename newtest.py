from pybughunt import CodeErrorDetector

detector = CodeErrorDetector()
code = '''
def example():
    print("Hello, world!"
'''
results = detector.analyze(code)
print(results)
