"""
Dictionaries in Python

This module demonstrates the usage of dictionaries, one of Python's most powerful
and flexible data structures. Dictionaries are mutable, unordered collections of
key-value pairs, where each key must be unique and immutable.
"""


def create_dict_examples():
    """
    Create and return examples of different dictionary creation methods.

    Returns:
        dict: A dictionary mapping example names to the created dictionaries
    """
    examples = {}

    # Empty dictionary
    examples["empty_dict"] = {}

    # Dictionary with initial values
    examples["person"] = {"name": "John", "age": 30, "city": "New York"}

    # Dictionary with the dict() constructor
    examples["constructor"] = dict(name="Alice", age=25, city="Boston")

    # Dictionary from a list of tuples
    examples["from_tuples"] = dict([("a", 1), ("b", 2), ("c", 3)])

    # Dictionary created with fromkeys() - same value for all keys
    examples["fromkeys"] = dict.fromkeys(["apple", "banana", "cherry"], 0)

    # Dictionary comprehension
    examples["comprehension"] = {x: x**2 for x in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    # Nested dictionaries
    examples["nested"] = {
        "person1": {"name": "John", "age": 30},
        "person2": {"name": "Alice", "age": 25}
    }

    return examples


def dict_access_examples():
    """
    Demonstrate different ways to access elements in a dictionary.

    Returns:
        dict: A dictionary of examples showing different access patterns
    """
    # Sample dictionary for examples
    person = {
        "name": "Jane",
        "age": 28,
        "job": "Engineer",
        "skills": ["Python", "SQL", "JavaScript"],
        "address": {
            "city": "San Francisco",
            "state": "CA"
        }
    }

    examples = {}

    # Basic key access
    examples["name_access"] = person["name"]  # Jane

    # Access with get() method - safer, returns None or default if key doesn't exist
    examples["get_age"] = person.get("age")  # 28
    examples["get_salary"] = person.get("salary")  # None
    examples["get_with_default"] = person.get("height", 170)  # 170 (default value)

    # Accessing nested values
    examples["nested_access"] = person["address"]["city"]  # San Francisco
    examples["list_in_dict"] = person["skills"][1]  # SQL

    # Checking if a key exists
    examples["has_job"] = "job" in person  # True
    examples["has_salary"] = "salary" in person  # False

    # View objects (keys, values, items)
    examples["keys"] = list(person.keys())  # ['name', 'age', 'job', 'skills', 'address']
    examples["values"] = list(person.values())  # [values corresponding to keys]
    examples["items"] = list(person.items())  # list of (key, value) tuples

    return examples


def dict_modification_examples():
    """
    Demonstrate various ways to modify dictionaries.

    Returns:
        dict: Examples of dictionary modifications
    """
    examples = {}

    # Starting dictionary
    person = {"name": "Tom", "age": 35}

    # Adding a new key-value pair
    person_add = person.copy()
    person_add["job"] = "Developer"
    examples["adding_pair"] = person_add  # {'name': 'Tom', 'age': 35, 'job': 'Developer'}

    # Updating a value
    person_update = person.copy()
    person_update["age"] = 36
    examples["updating_value"] = person_update  # {'name': 'Tom', 'age': 36}

    # Updating multiple values at once with update()
    person_update_multiple = person.copy()
    person_update_multiple.update({"age": 36, "job": "Developer", "city": "Seattle"})
    examples["updating_multiple"] = person_update_multiple  # Updated with multiple values

    # Removing a key-value pair with pop()
    person_pop = {"name": "Tom", "age": 35, "job": "Developer"}
    popped_value = person_pop.pop("job")
    examples["pop"] = {"dict": person_pop, "popped_value": popped_value}  # Dict without 'job', value 'Developer'

    # Removing the last inserted item with popitem() (Python 3.7+ maintains insertion order)
    person_popitem = {"name": "Tom", "age": 35, "job": "Developer"}
    popped_item = person_popitem.popitem()  # Removes and returns ('job', 'Developer')
    examples["popitem"] = {"dict": person_popitem, "popped_item": popped_item}

    # Removing a key with del
    person_del = {"name": "Tom", "age": 35, "job": "Developer"}
    del person_del["age"]
    examples["del"] = person_del  # {'name': 'Tom', 'job': 'Developer'}

    # Clearing all items
    person_clear = {"name": "Tom", "age": 35}
    person_clear.clear()
    examples["clear"] = person_clear  # {}

    # Dictionary merging (Python 3.9+)
    # Using | and |= operators for merging dictionaries (uncomment for Python 3.9+)
    # examples["merge_new"] = {"a": 1, "b": 2} | {"b": 3, "c": 4}  # {'a': 1, 'b': 3, 'c': 4}

    # Merging dictionaries with {**d1, **d2} unpacking (works in Python 3.5+)
    examples["merge_unpacking"] = {**{"a": 1, "b": 2}, **{"b": 3, "c": 4}}  # {'a': 1, 'b': 3, 'c': 4}

    return examples


def dict_operations_examples():
    """
    Demonstrate common dictionary operations and methods.

    Returns:
        dict: Examples of dictionary operations
    """
    examples = {}

    # Sample dictionary for examples
    student = {
        "name": "Emma",
        "id": 12345,
        "courses": ["Math", "Science", "History"],
        "grades": {"Math": 90, "Science": 95, "History": 88}
    }

    # Length (number of key-value pairs)
    examples["length"] = len(student)  # 4

    # Dictionary views
    examples["dict_keys"] = list(student.keys())
    examples["dict_values"] = list(student.values())
    examples["dict_items"] = list(student.items())

    # Copy a dictionary
    # Shallow copy - nested mutable objects are shared
    examples["shallow_copy"] = student.copy()
    examples["shallow_copy2"] = dict(student)

    # Deep copy - creates independent copies of nested objects
    import copy
    examples["deep_copy"] = copy.deepcopy(student)

    # Dictionary comprehension with filtering
    numbers = [1, 2, 3, 4, 5, 6]
    examples["dict_comprehension"] = {x: x**3 for x in numbers if x % 2 == 0}  # {2: 8, 4: 64, 6: 216}

    # Iterating through a dictionary
    keys_string = ", ".join(student.keys())
    examples["keys_iteration"] = f"Keys: {keys_string}"

    # Convert dictionary to list of tuples
    examples["dict_to_tuples"] = list(student.items())

    # Convert lists to dictionary
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    examples["lists_to_dict"] = dict(zip(keys, values))  # {'a': 1, 'b': 2, 'c': 3}

    return examples


def dict_advanced_examples():
    """
    Demonstrate more advanced dictionary concepts and techniques.

    Returns:
        dict: Advanced dictionary examples
    """
    examples = {}

    # Default dictionaries - never raise KeyError
    from collections import defaultdict

    # defaultdict with int - default value is 0
    word_counts = defaultdict(int)
    for word in ["apple", "banana", "apple", "cherry", "banana", "apple"]:
        word_counts[word] += 1
    examples["defaultdict_int"] = dict(word_counts)  # {'apple': 3, 'banana': 2, 'cherry': 1}

    # defaultdict with list - default value is empty list
    fruit_colors = defaultdict(list)
    fruit_colors["red"].append("apple")
    fruit_colors["yellow"].append("banana")
    fruit_colors["red"].append("cherry")
    examples["defaultdict_list"] = dict(fruit_colors)  # {'red': ['apple', 'cherry'], 'yellow': ['banana']}

    # OrderedDict - maintains insertion order (less important since Python 3.7+ dicts preserve order)
    from collections import OrderedDict
    ordered = OrderedDict([("first", 1), ("second", 2), ("third", 3)])
    examples["ordered_dict"] = list(ordered.items())  # [('first', 1), ('second', 2), ('third', 3)]

    # Counter - specialized dictionary for counting hashable objects
    from collections import Counter
    count = Counter(["apple", "orange", "apple", "banana", "orange", "apple"])
    examples["counter"] = dict(count)  # {'apple': 3, 'orange': 2, 'banana': 1}
    examples["counter_most_common"] = count.most_common(2)  # [('apple', 3), ('orange', 2)]

    # Nested dictionary access with get() to avoid KeyError
    nested = {"users": {"john": {"email": "john@example.com"}}}

    # Safe access with multiple get() calls
    email = nested.get("users", {}).get("john", {}).get("email", "No email")
    examples["safe_nested_access"] = email  # "john@example.com"

    # Try to access a non-existent nested path
    missing = nested.get("users", {}).get("jane", {}).get("email", "No email")
    examples["missing_nested_access"] = missing  # "No email"

    # Dictionary of functions
    def add(x, y): return x + y
    def subtract(x, y): return x - y
    def multiply(x, y): return x * y

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply
    }

    examples["function_dict_result"] = operations["add"](5, 3)  # 8

    return examples


def dict_use_cases():
    """
    Demonstrate common use cases for dictionaries in Python programs.

    Returns:
        dict: Dictionary use case examples
    """
    examples = {}

    # 1. Counting elements
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    examples["counting"] = word_count  # {'apple': 3, 'banana': 2, 'orange': 1}

    # 2. Grouping data
    students = [
        {"name": "Alice", "grade": "A"},
        {"name": "Bob", "grade": "B"},
        {"name": "Charlie", "grade": "A"},
        {"name": "David", "grade": "C"}
    ]

    by_grade = {}
    for student in students:
        grade = student["grade"]
        if grade not in by_grade:
            by_grade[grade] = []
        by_grade[grade].append(student["name"])
    examples["grouping"] = by_grade  # {'A': ['Alice', 'Charlie'], 'B': ['Bob'], 'C': ['David']}

    # 3. Caching/memoization
    def fibonacci(n, cache={}):
        """Calculate Fibonacci numbers with memoization."""
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]

    # Calculate first 10 Fibonacci numbers
    fib_results = {}
    for i in range(10):
        fib_results[i] = fibonacci(i)
    examples["memoization"] = fib_results

    # 4. Lookup tables
    day_names = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    examples["lookup_table"] = day_names

    # 5. Configuration settings
    config = {
        "app_name": "MyApp",
        "version": "1.0.0",
        "debug": True,
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "mydb"
        },
        "cache_time": 3600
    }
    examples["configuration"] = config

    # 6. Json-like data structure
    person = {
        "name": "John Smith",
        "age": 35,
        "contact": {
            "email": "john@example.com",
            "phone": "555-1234"
        },
        "interests": ["programming", "hiking", "reading"],
        "is_active": True
    }
    examples["json_like"] = person

    return examples


def interactive_dict_demo():
    """
    Function for interactive dictionary operation demonstration.

    This function can be called from a main script to allow users to
    interactively try dictionary operations.
    """
    print("\n=== Python Dictionaries Interactive Demo ===\n")

    # Create a dictionary
    my_dict = {}
    print(f"Created empty dictionary: {my_dict}")

    # Add some initial items
    while True:
        key = input("\nEnter a key (or 'done' to continue): ")
        if key.lower() == 'done':
            break

        value = input(f"Enter a value for '{key}': ")

        # Try to convert to int or float if it looks like a number
        try:
            if '.' in value:
                value = float(value)
            elif value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
                value = int(value)
        except ValueError:
            # Keep as string if not convertible
            pass

        my_dict[key] = value
        print(f"Dictionary now contains: {my_dict}")

    if not my_dict:
        # Use a default dictionary if the user didn't add any items
        my_dict = {"name": "John", "age": 30, "city": "New York"}
        print(f"\nUsing default dictionary: {my_dict}")

    print("\n=== Dictionary Operations ===")

    while True:
        print("\nCurrent dictionary:", my_dict)
        print("\nChoose an operation:")
        print("1. Access value (by key)")
        print("2. Add or update key-value pair")
        print("3. Remove key-value pair")
        print("4. View keys, values, or items")
        print("5. Check if key exists")
        print("6. Dictionary information")
        print("7. Advanced operations")
        print("8. Exit demo")

        choice = input("\nEnter your choice (1-8): ")

        if choice == '1':
            # Access value
            key = input("Enter a key to access: ")

            # Method selection
            method = input("Use (d)irect access [key] or (g)et method? ").lower()

            try:
                if method.startswith('g'):
                    default = input("Enter a default value if key doesn't exist (optional): ")
                    if default:
                        # Try to convert default to number if it looks like one
                        try:
                            if '.' in default:
                                default = float(default)
                            else:
                                default = int(default)
                        except ValueError:
                            # Keep as string
                            pass
                        result = my_dict.get(key, default)
                    else:
                        result = my_dict.get(key)
                    print(f"Result using get(): {result}")
                else:
                    result = my_dict[key]
                    print(f"Result using direct access: {result}")
            except KeyError as e:
                print(f"Error: {e} - Key doesn't exist in the dictionary")

        elif choice == '2':
            # Add or update
            key = input("Enter a key to add/update: ")
            value = input(f"Enter a value for '{key}': ")

            # Try to convert to number if it looks like one
            try:
                if '.' in value:
                    value = float(value)
                elif value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
                    value = int(value)
            except ValueError:
                # Keep as string
                pass

            # Update method selection
            method = input("Use (d)irect assignment or (u)pdate method? ").lower()

            if method.startswith('u'):
                my_dict.update({key: value})
                print(f"Updated using update() method: {my_dict}")
            else:
                my_dict[key] = value
                print(f"Updated using direct assignment: {my_dict}")

        elif choice == '3':
            # Remove key-value pair
            if not my_dict:
                print("Dictionary is already empty!")
                continue

            key = input("Enter a key to remove: ")

            if key not in my_dict:
                print(f"Key '{key}' doesn't exist in the dictionary.")
                continue

            method = input("Use (d)el, (p)op, or (c)lear all? ").lower()

            try:
                if method.startswith('d'):
                    del my_dict[key]
                    print(f"Removed '{key}' using del: {my_dict}")
                elif method.startswith('p'):
                    value = my_dict.pop(key)
                    print(f"Popped '{key}': {value}")
                    print(f"Dictionary now: {my_dict}")
                else:
                    confirm = input("Are you sure you want to clear all items? (y/n): ").lower()
                    if confirm.startswith('y'):
                        my_dict.clear()
                        print("Dictionary cleared:", my_dict)
            except KeyError as e:
                print(f"Error: {e}")

        elif choice == '4':
            # View keys, values, items
            view_type = input("View (k)eys, (v)alues, or (i)tems? ").lower()

            if view_type.startswith('k'):
                print("Keys:", list(my_dict.keys()))
            elif view_type.startswith('v'):
                print("Values:", list(my_dict.values()))
            else:
                print("Items:", list(my_dict.items()))

        elif choice == '5':
            # Check if key exists
            key = input("Enter a key to check: ")

            if key in my_dict:
                print(f"'{key}' exists in the dictionary with value: {my_dict[key]}")
            else:
                print(f"'{key}' does NOT exist in the dictionary")

        elif choice == '6':
            # Dictionary information
            print(f"Number of key-value pairs: {len(my_dict)}")

            # Count data types
            types_count = {}
            for value in my_dict.values():
                type_name = type(value).__name__
                types_count[type_name] = types_count.get(type_name, 0) + 1
            print(f"Value types: {types_count}")

            # Memory info (approximate)
            import sys
            mem_size = sys.getsizeof(my_dict)
            print(f"Approximate memory size: {mem_size} bytes")

        elif choice == '7':
            # Advanced operations
            print("\nAdvanced Operations:")
            print("1. Copy dictionary (shallow)")
            print("2. Merge with another dictionary")
            print("3. Invert dictionary (values become keys)")
            print("4. Create filtered dictionary")
            print("5. Transform values")

            advanced_choice = input("\nChoose operation (1-5): ")

            if advanced_choice == '1':
                # Copy
                dict_copy = my_dict.copy()
                print(f"Original: {my_dict}")
                print(f"Copy: {dict_copy}")
                print("Note: This is a shallow copy. Nested mutable objects would still be shared.")

            elif advanced_choice == '2':
                # Merge
                print("Let's create another dictionary to merge with yours")
                other_dict = {}
                for _ in range(2):  # Just get 2 key-values for simplicity
                    key = input("Enter a key for the second dictionary: ")
                    value = input(f"Enter a value for '{key}': ")
                    other_dict[key] = value

                print(f"First dictionary: {my_dict}")
                print(f"Second dictionary: {other_dict}")

                # Merge options
                merge_method = input("Merge using (u)pdate or (**) unpacking? ").lower()

                if merge_method.startswith('u'):
                    result = my_dict.copy()
                    result.update(other_dict)
                    print(f"Merged (update): {result}")
                else:
                    result = {**my_dict, **other_dict}
                    print(f"Merged (unpacking): {result}")

                if input("Replace your dictionary with the merged one? (y/n): ").lower().startswith('y'):
                    my_dict = result

            elif advanced_choice == '3':
                # Invert (assuming values are immutable and unique)
                try:
                    inverted = {v: k for k, v in my_dict.items()}
                    print(f"Inverted dictionary: {inverted}")

                    if input("Replace your dictionary with the inverted one? (y/n): ").lower().startswith('y'):
                        my_dict = inverted
                except TypeError:
                    print("Error: Dictionary values must be immutable (hashable) to use as keys")

            elif advanced_choice == '4':
                # Filtered dictionary
                filter_type = input("Filter based on (k)eys or (v)alues? ").lower()

                if filter_type.startswith('k'):
                    prefix = input("Enter key prefix to filter by (or leave blank): ")
                    result = {k: v for k, v in my_dict.items() if str(k).startswith(prefix)}
                else:
                    value_type = input("Filter for values of type (s)tring, (i)nt, (f)loat, or (a)ll non-strings? ").lower()

                    if value_type.startswith('s'):
                        result = {k: v for k, v in my_dict.items() if isinstance(v, str)}
                    elif value_type.startswith('i'):
                        result = {k: v for k, v in my_dict.items() if isinstance(v, int)}
                    elif value_type.startswith('f'):
                        result = {k: v for k, v in my_dict.items() if isinstance(v, float)}
                    else:
                        result = {k: v for k, v in my_dict.items() if not isinstance(v, str)}

                print(f"Filtered dictionary: {result}")

                if input("Replace your dictionary with the filtered one? (y/n): ").lower().startswith('y'):
                    my_dict = result

            elif advanced_choice == '5':
                # Transform values
                transform_type = input("Transform (n)umeric values or (s)tring values? ").lower()

                if transform_type.startswith('n'):
                    operation = input("(d)ouble, (s)quare, or (h)alve numeric values? ").lower()

                    if operation.startswith('d'):
                        result = {k: v * 2 if isinstance(v, (int, float)) else v for k, v in my_dict.items()}
                    elif operation.startswith('s'):
                        result = {k: v ** 2 if isinstance(v, (int, float)) else v for k, v in my_dict.items()}
                    else:
                        result = {k: v / 2 if isinstance(v, (int, float)) else v for k, v in my_dict.items()}

                else:
                    operation = input("(u)ppercase, (l)owercase, or (r)everse string values? ").lower()

                    if operation.startswith('u'):
                        result = {k: v.upper() if isinstance(v, str) else v for k, v in my_dict.items()}
                    elif operation.startswith('l'):
                        result = {k: v.lower() if isinstance(v, str) else v for k, v in my_dict.items()}
                    else:
                        result = {k: v[::-1] if isinstance(v, str) else v for k, v in my_dict.items()}

                print(f"Transformed dictionary: {result}")

                if input("Replace your dictionary with the transformed one? (y/n): ").lower().startswith('y'):
                    my_dict = result

        elif choice == '8':
            break

        else:
            print("Invalid choice, please try again.")

    print("\nThanks for exploring Python dictionaries!")