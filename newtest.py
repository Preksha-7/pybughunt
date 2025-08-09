from pybughunt import CodeErrorDetector

detector = CodeErrorDetector()
code = '''
# sample_intense_bug.py

def append_to_list(value, my_list=[]):
    """
    Appends a value to a list.
    This function has a subtle logical error related to mutable default arguments.
    """
    my_list.append(value)
    return my_list

def calculate_average(data_points):
    """
    Calculates the average of a list of data points.
    Contains a potential division-by-zero if not handled carefully,
    but the main bug is in 'append_to_list' interactions.
    """
    if not data_points:
        return 0.0 # Handles empty list explicitly
    return sum(data_points) / len(data_points)

def main():
    print("Demonstrating the subtle bug with mutable default arguments:")

    list1 = append_to_list(10)
    print(f"List 1 after first call (expected [10]): {list1}")

    list2 = append_to_list(20) # Unexpectedly appends to the *same* list as list1
    print(f"List 2 after second call (expected [20], but will be [10, 20]): {list2}")

    list3 = append_to_list(30, []) # Correct usage, provides a new list
    print(f"List 3 with explicit list (expected [30]): {list3}")

    print("\nObserve that list1 and list2 are the same object due to the default argument's mutability.")
    print(f"Is list1 the same object as list2? {list1 is list2}")

    # A more complex scenario where the mutable default might lead to unexpected state
    results_store = {}
    def process_data(data, cache={}):
        if data not in cache:
            # Simulate some complex computation
            processed = [x * 2 for x in data]
            cache[data] = processed
        return cache[data]

    data1 = tuple([1, 2, 3]) # Use tuple for dict key
    data2 = tuple([4, 5, 6])

    res1 = process_data(data1)
    print(f"\nProcessed data1: {res1}")

    res2 = process_data(data2)
    print(f"Processed data2: {res2}")

    res3 = process_data(data1) # This will retrieve from cache, but what if cache was cleared externally?
    print(f"Processed data1 again: {res3}")

    # The bug: if `cache` were intended to be unique for each call or specific context,
    # its persistence across calls can lead to stale data or unexpected side effects.
    # While this 'cache' example might sometimes be intentional, it's often a source of bugs
    # when developers don't realize the default dict is shared.

    # Example of a division by zero that could be caught by static analysis
    # This part is straightforward for static analysis, unlike the mutable default arg.
    numerator = 10
    denominator = 0
    # result = numerator / denominator # This would be a clear static error if uncommented

if __name__ == "__main__":
    main()
'''
results = detector.analyze(code)
print(results)
