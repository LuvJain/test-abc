"""
Tuples and Sets in Python

This module demonstrates the usage of tuples and sets in Python.

Tuples are immutable sequences, similar to lists but cannot be changed after creation.
Sets are unordered collections of unique elements, useful for membership testing and
eliminating duplicate entries.
"""


# ==========================
# TUPLES
# ==========================

def tuple_examples():
    """
    Demonstrate creation and basic properties of tuples.

    Returns:
        dict: A dictionary of tuple examples
    """
    examples = {}

    # Creating tuples
    examples["empty_tuple"] = ()
    examples["single_item_tuple"] = (1,)  # Note the comma is needed
    examples["numbers_tuple"] = (1, 2, 3, 4, 5)
    examples["mixed_tuple"] = (1, "hello", 3.14, True)
    examples["nested_tuple"] = (1, (2, 3), (4, 5, 6))
    examples["from_constructor"] = tuple([1, 2, 3])  # Convert list to tuple
    examples["from_string"] = tuple("Python")  # ('P', 'y', 't', 'h', 'o', 'n')

    # Tuple packing and unpacking
    coordinates = (10, 20)  # Packing
    x, y = coordinates  # Unpacking
    examples["tuple_packing"] = coordinates
    examples["tuple_unpacking"] = {"x": x, "y": y}

    # Extended unpacking (Python 3+)
    numbers = (1, 2, 3, 4, 5)
    first, *middle, last = numbers
    examples["extended_unpacking"] = {"first": first, "middle": middle, "last": last}

    return examples


def tuple_operations():
    """
    Demonstrate operations that can be performed on tuples.

    Returns:
        dict: Dictionary of tuple operation examples
    """
    examples = {}

    # Sample tuple for examples
    t = (1, 2, 3, 4, 5, 3)

    # Accessing elements (similar to lists)
    examples["indexing"] = t[2]  # 3
    examples["negative_index"] = t[-1]  # 3
    examples["slicing"] = t[1:4]  # (2, 3, 4)

    # Immutability demonstration
    examples["immutable"] = "Cannot modify tuples after creation (t[0] = 10 would raise TypeError)"

    # Common operations
    examples["length"] = len(t)  # 6
    examples["count"] = t.count(3)  # 2 (number of occurrences of 3)
    examples["index"] = t.index(3)  # 2 (index of first occurrence of 3)
    examples["min"] = min(t)  # 1
    examples["max"] = max(t)  # 5
    examples["sum"] = sum(t)  # 18

    # Concatenation
    examples["concatenation"] = t + (6, 7, 8)  # (1, 2, 3, 4, 5, 3, 6, 7, 8)
    examples["repetition"] = (1, 2) * 3  # (1, 2, 1, 2, 1, 2)

    # Membership testing
    examples["membership"] = 3 in t  # True
    examples["non_membership"] = 6 not in t  # True

    # Iteration
    square_tuple = tuple(x**2 for x in t)
    examples["iteration"] = square_tuple

    # Sorting (returns a list, not a tuple)
    unsorted_tuple = (3, 1, 4, 1, 5, 9, 2)
    examples["sorted"] = sorted(unsorted_tuple)  # Returns [1, 1, 2, 3, 4, 5, 9]

    # Conversion
    examples["to_list"] = list(t)  # [1, 2, 3, 4, 5, 3]

    return examples


def tuple_use_cases():
    """
    Demonstrate common use cases for tuples in Python.

    Returns:
        dict: Dictionary of tuple use case examples
    """
    examples = {}

    # 1. Returning multiple values from a function
    def min_max(numbers):
        return min(numbers), max(numbers)

    result = min_max([3, 1, 4, 1, 5, 9, 2])
    examples["return_multiple_values"] = result  # (1, 9)

    # 2. Dictionary keys (tuples can be used as dictionary keys because they're immutable)
    locations = {
        (40.7128, -74.0060): "New York",
        (34.0522, -118.2437): "Los Angeles",
        (41.8781, -87.6298): "Chicago"
    }
    examples["as_dictionary_keys"] = list(locations.keys())

    # 3. Function arguments with *args
    def add_all(*args):
        return sum(args)

    examples["args_unpacking"] = add_all(1, 2, 3, 4, 5)  # 15

    # 4. Immutable records/data structures
    Person = tuple
    john = Person(name="John", age=30, city="New York")
    examples["named_records"] = {
        "name": john[0],
        "age": john[1],
        "city": john[2]
    }

    # 5. More structured data using collections.namedtuple
    from collections import namedtuple

    # Define a new type
    Point = namedtuple('Point', ['x', 'y', 'z'])

    # Create an instance
    p = Point(1, 2, 3)
    examples["named_tuple"] = {
        "x": p.x,
        "y": p.y,
        "z": p.z,
        "as_tuple": tuple(p),
        "by_index": p[0]  # Still supports indexing
    }

    # 6. Sequence unpacking in for loops
    points = [(1, 2), (3, 4), (5, 6)]
    coordinates = []
    for x, y in points:
        coordinates.append(f"({x}, {y})")
    examples["unpacking_in_loops"] = coordinates

    return examples


def interactive_tuple_demo():
    """
    Interactive demonstration of tuple operations.
    """
    print("\n=== Python Tuples Interactive Demo ===\n")

    # Explain what tuples are
    print("Tuples are immutable sequences in Python, similar to lists but cannot be changed after creation.")
    print("They're commonly used for fixed collections of items and can be used as dictionary keys.")

    # Create a tuple
    print("\nLet's create a tuple:")
    items = []
    while True:
        item = input("Enter an item (or 'done' to finish): ")
        if item.lower() == 'done':
            break

        # Try to convert to number if applicable
        try:
            if '.' in item:
                item = float(item)
            elif item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
                item = int(item)
        except ValueError:
            pass

        items.append(item)

    # If no items were entered, use a default tuple
    if not items:
        my_tuple = (1, 2, 3, 'apple', 'banana')
        print(f"Using default tuple: {my_tuple}")
    else:
        my_tuple = tuple(items)
        print(f"Created tuple: {my_tuple}")

    # Demonstrate tuple operations
    while True:
        print("\nChoose an operation to explore:")
        print("1. Access elements (indexing and slicing)")
        print("2. Count and find elements")
        print("3. Concatenate with another tuple")
        print("4. Unpack tuple values")
        print("5. Create a named tuple")
        print("6. Convert to other data types")
        print("7. Check membership (in operator)")
        print("8. Exit tuple demo")

        choice = input("\nEnter your choice (1-8): ")

        if choice == '1':
            # Access elements
            try:
                index_input = input("Enter an index or slice (e.g., 1, -1, 1:3, ::2): ")
                if ':' in index_input:
                    # It's a slice
                    parts = [p.strip() for p in index_input.split(':')]
                    start = int(parts[0]) if parts[0] else None
                    end = int(parts[1]) if len(parts) > 1 and parts[1] else None
                    step = int(parts[2]) if len(parts) > 2 and parts[2] else None

                    # Create the appropriate slice object
                    if len(parts) == 2:
                        result = my_tuple[start:end]
                    else:
                        result = my_tuple[start:end:step]
                else:
                    # It's an index
                    result = my_tuple[int(index_input)]
                print(f"Result: {result}")
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")

        elif choice == '2':
            # Count and find
            value = input("Enter a value to count/find: ")

            # Convert to appropriate type if the input looks like a number
            try:
                if '.' in value:
                    value = float(value)
                elif value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
                    value = int(value)
            except ValueError:
                pass

            # Count occurrences
            count = my_tuple.count(value)
            print(f"'{value}' appears {count} time(s) in the tuple")

            # Find index
            if count > 0:
                try:
                    index = my_tuple.index(value)
                    print(f"First occurrence of '{value}' is at index {index}")
                except ValueError:
                    print(f"'{value}' not found in the tuple")
            else:
                print(f"'{value}' not found in the tuple")

        elif choice == '3':
            # Concatenate tuples
            print("Let's create another tuple to concatenate with yours")
            items2 = []
            while True:
                item = input("Enter an item for the second tuple (or 'done' to finish): ")
                if item.lower() == 'done':
                    break

                # Try to convert to number if applicable
                try:
                    if '.' in item:
                        item = float(item)
                    elif item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
                        item = int(item)
                except ValueError:
                    pass

                items2.append(item)

            second_tuple = tuple(items2) if items2 else (4, 5, 6)
            if not items2:
                print(f"Using default second tuple: {second_tuple}")

            concatenated = my_tuple + second_tuple
            print(f"Concatenated tuple: {concatenated}")

            # Optional - replace current tuple with concatenated one
            if input("Use this concatenated tuple for further operations? (y/n): ").lower().startswith('y'):
                my_tuple = concatenated

        elif choice == '4':
            # Tuple unpacking
            if not my_tuple:
                print("Cannot unpack an empty tuple")
                continue

            if len(my_tuple) <= 3:
                # Basic unpacking for small tuples
                try:
                    if len(my_tuple) == 1:
                        (a,) = my_tuple
                        print(f"Unpacked value: a = {a}")
                    elif len(my_tuple) == 2:
                        a, b = my_tuple
                        print(f"Unpacked values: a = {a}, b = {b}")
                    elif len(my_tuple) == 3:
                        a, b, c = my_tuple
                        print(f"Unpacked values: a = {a}, b = {b}, c = {c}")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                # Extended unpacking for larger tuples
                try:
                    first, *middle, last = my_tuple
                    print(f"First: {first}")
                    print(f"Middle: {middle}")
                    print(f"Last: {last}")
                    print("Note: The middle part is a list, not a tuple")
                except ValueError as e:
                    print(f"Error: {e}")

        elif choice == '5':
            # Named tuple
            from collections import namedtuple

            print("\nLet's create a named tuple type:")
            type_name = input("Enter a name for your named tuple type (e.g., 'Person'): ") or "Record"
            field_names = input("Enter field names separated by spaces (e.g., 'name age city'): ") or "field1 field2 field3"

            # Create the named tuple class
            try:
                RecordType = namedtuple(type_name, field_names.split())
                print(f"Created a new named tuple type: {type_name} with fields: {field_names}")

                # Create an instance
                values = []
                for field in field_names.split():
                    value = input(f"Enter a value for {field}: ")
                    # Try to convert to appropriate type
                    try:
                        if '.' in value:
                            value = float(value)
                        elif value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
                            value = int(value)
                    except ValueError:
                        pass
                    values.append(value)

                record = RecordType(*values)
                print(f"Created named tuple instance: {record}")

                # Demonstrate access methods
                print("\nAccessing fields:")
                for field in field_names.split():
                    print(f"{field}: {getattr(record, field)}")

                print("\nYou can also access by index:")
                for i, field in enumerate(field_names.split()):
                    print(f"{field} (index {i}): {record[i]}")

            except (ValueError, TypeError) as e:
                print(f"Error creating named tuple: {e}")

        elif choice == '6':
            # Convert to other data types
            print("\nConverting tuple to other data types:")
            print(f"As list: {list(my_tuple)}")

            try:
                # Only works if all elements are strings or all elements are numbers
                if all(isinstance(x, str) for x in my_tuple):
                    print(f"Joined as string: {''.join(my_tuple)}")
                elif all(isinstance(x, (int, float)) for x in my_tuple):
                    print(f"Sum: {sum(my_tuple)}")
                    print(f"Average: {sum(my_tuple)/len(my_tuple) if my_tuple else 0}")
            except TypeError:
                print("Note: Some operations are only available for tuples of compatible types")

        elif choice == '7':
            # Check membership
            value = input("Enter a value to check for membership: ")

            # Convert to appropriate type if the input looks like a number
            try:
                if '.' in value:
                    value = float(value)
                elif value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
                    value = int(value)
            except ValueError:
                pass

            if value in my_tuple:
                print(f"'{value}' is in the tuple")
            else:
                print(f"'{value}' is not in the tuple")

        elif choice == '8':
            print("\nExiting tuple demo...")
            break

        else:
            print("Invalid choice, please try again.")

    return "Tuple demo completed"


# ==========================
# SETS
# ==========================

def set_examples():
    """
    Demonstrate creation and basic properties of sets.

    Returns:
        dict: A dictionary of set examples
    """
    examples = {}

    # Creating sets
    examples["empty_set"] = set()  # Empty set (NOT {}, which is an empty dict)
    examples["from_literals"] = {1, 2, 3, 4, 5}
    examples["from_constructor"] = set([1, 2, 3, 3, 2, 1])  # Removes duplicates: {1, 2, 3}
    examples["from_string"] = set("hello")  # {'h', 'e', 'l', 'o'}
    examples["from_tuple"] = set((1, 2, 3, 2))  # {1, 2, 3}

    # Uniqueness demonstration
    examples["uniqueness"] = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])  # {1, 2, 3, 4}

    # Immutable elements only
    examples["immutable_elements"] = "Sets can only contain hashable (immutable) elements"
    # This would raise TypeError: examples["invalid"] = {[1, 2], [3, 4]}

    # Frozen sets (immutable sets)
    examples["frozen_set"] = frozenset([1, 2, 3])

    return examples


def set_operations():
    """
    Demonstrate operations that can be performed on sets.

    Returns:
        dict: Dictionary of set operation examples
    """
    examples = {}

    # Sample sets
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}

    # Basic set operations
    examples["union"] = a | b  # {1, 2, 3, 4, 5, 6, 7, 8}
    examples["union_method"] = a.union(b)  # Same as a | b

    examples["intersection"] = a & b  # {4, 5}
    examples["intersection_method"] = a.intersection(b)  # Same as a & b

    examples["difference"] = a - b  # {1, 2, 3}
    examples["difference_method"] = a.difference(b)  # Same as a - b

    examples["symmetric_difference"] = a ^ b  # {1, 2, 3, 6, 7, 8}
    examples["symmetric_difference_method"] = a.symmetric_difference(b)  # Same as a ^ b

    # Subset, superset, disjoint
    c = {1, 2}
    d = {1, 2, 3, 4, 5}
    examples["subset"] = c.issubset(d)  # True (c is a subset of d)
    examples["subset_operator"] = c <= d  # True

    examples["proper_subset"] = c < d  # True (c is a proper subset of d)

    examples["superset"] = d.issuperset(c)  # True (d is a superset of c)
    examples["superset_operator"] = d >= c  # True

    examples["proper_superset"] = d > c  # True (d is a proper superset of c)

    e = {10, 11, 12}
    examples["disjoint"] = a.isdisjoint(e)  # True (a and e have no elements in common)

    return examples


def set_modifications():
    """
    Demonstrate ways to modify sets.

    Returns:
        dict: Dictionary of set modification examples
    """
    examples = {}

    # Add elements
    s = {1, 2, 3}
    s.add(4)
    examples["add"] = set(s)  # {1, 2, 3, 4}

    # Add multiple elements
    s = {1, 2, 3}
    s.update([3, 4, 5])
    examples["update"] = set(s)  # {1, 2, 3, 4, 5}

    # Remove elements (raises KeyError if not present)
    s = {1, 2, 3, 4, 5}
    s.remove(3)
    examples["remove"] = set(s)  # {1, 2, 4, 5}

    # Discard elements (no error if not present)
    s = {1, 2, 3, 4, 5}
    s.discard(3)
    s.discard(10)  # No error
    examples["discard"] = set(s)  # {1, 2, 4, 5}

    # Pop a random element
    s = {1, 2, 3}
    popped = s.pop()
    examples["pop"] = {"set_after_pop": set(s), "popped_value": popped}

    # Clear a set
    s = {1, 2, 3}
    s.clear()
    examples["clear"] = set(s)  # set()

    # In-place operations
    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}

    # Union update
    s = s1.copy()
    s |= s2
    examples["union_update"] = set(s)  # {1, 2, 3, 4, 5, 6}

    # Intersection update
    s = s1.copy()
    s &= s2
    examples["intersection_update"] = set(s)  # {3, 4}

    # Difference update
    s = s1.copy()
    s -= s2
    examples["difference_update"] = set(s)  # {1, 2}

    # Symmetric difference update
    s = s1.copy()
    s ^= s2
    examples["symmetric_difference_update"] = set(s)  # {1, 2, 5, 6}

    return examples


def set_use_cases():
    """
    Demonstrate common use cases for sets in Python.

    Returns:
        dict: Dictionary of set use case examples
    """
    examples = {}

    # 1. Remove duplicates from a list
    duplicates = [1, 2, 2, 3, 4, 3, 5, 1, 6]
    examples["remove_duplicates"] = list(set(duplicates))  # Note: order not preserved

    # 2. Membership testing (faster than lists for large datasets)
    numbers = set(range(1000))
    examples["membership_test"] = 500 in numbers  # True, fast lookup

    # 3. Finding unique elements
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    examples["unique_to_first"] = list(set(list1) - set(list2))  # Elements in list1 but not in list2
    examples["unique_to_second"] = list(set(list2) - set(list1))  # Elements in list2 but not in list1
    examples["in_either"] = list(set(list1) | set(list2))  # Elements in either list
    examples["in_both"] = list(set(list1) & set(list2))  # Elements in both lists
    examples["in_one_but_not_both"] = list(set(list1) ^ set(list2))  # Elements in either but not both

    # 4. Finding all unique characters in a string
    text = "hello world"
    examples["unique_chars"] = set(text)  # {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}

    # 5. Set operations in practice
    students_course_a = {"Alice", "Bob", "Charlie", "David"}
    students_course_b = {"Bob", "David", "Edward", "Frank"}

    # Students in either course
    examples["students_either_course"] = students_course_a | students_course_b

    # Students in both courses
    examples["students_both_courses"] = students_course_a & students_course_b

    # Students in course A but not B
    examples["students_only_course_a"] = students_course_a - students_course_b

    # Students in exactly one course
    examples["students_exactly_one_course"] = students_course_a ^ students_course_b

    return examples


def interactive_set_demo():
    """
    Interactive demonstration of set operations.
    """
    print("\n=== Python Sets Interactive Demo ===\n")

    # Explain what sets are
    print("Sets are unordered collections of unique elements in Python.")
    print("They're particularly useful for membership testing, removing duplicates,")
    print("and mathematical set operations like unions and intersections.")

    # Create a set
    print("\nLet's create a set:")
    items = []
    while True:
        item = input("Enter an item (or 'done' to finish): ")
        if item.lower() == 'done':
            break

        # Try to convert to number if applicable
        try:
            if '.' in item:
                item = float(item)
            elif item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
                item = int(item)
        except ValueError:
            pass

        items.append(item)

    # If no items were entered, use a default set
    if not items:
        my_set = {1, 2, 3, 4, 5}
        print(f"Using default set: {my_set}")
    else:
        my_set = set(items)
        print(f"Created set: {my_set}")
        if len(my_set) < len(items):
            print("Note: Duplicate elements were automatically removed")

    # Demonstrate set operations
    while True:
        print("\nChoose an operation to explore:")
        print("1. Add or remove elements")
        print("2. Set operations with another set (union, intersection, etc.)")
        print("3. Check membership and subset relationships")
        print("4. Convert to other data types")
        print("5. Find unique elements between collections")
        print("6. Exit set demo")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            # Add or remove elements
            modification = input("(a)dd, (r)emove, (d)iscard, (p)op, or (c)lear? ").lower()

            if modification.startswith('a'):
                value = input("Enter a value to add: ")
                # Convert to appropriate type if it looks like a number
                try:
                    if '.' in value:
                        value = float(value)
                    elif value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
                        value = int(value)
                except ValueError:
                    pass

                my_set.add(value)
                print(f"Set after adding {value}: {my_set}")

            elif modification.startswith('r'):
                value = input("Enter a value to remove: ")
                # Convert to appropriate type if it looks like a number
                try:
                    if '.' in value:
                        value = float(value)
                    elif value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
                        value = int(value)
                except ValueError:
                    pass

                try:
                    my_set.remove(value)
                    print(f"Set after removing {value}: {my_set}")
                except KeyError:
                    print(f"Error: {value} is not in the set")

            elif modification.startswith('d'):
                value = input("Enter a value to discard: ")
                # Convert to appropriate type if it looks like a number
                try:
                    if '.' in value:
                        value = float(value)
                    elif value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
                        value = int(value)
                except ValueError:
                    pass

                my_set.discard(value)
                print(f"Set after discarding {value} (no error if not present): {my_set}")

            elif modification.startswith('p'):
                if not my_set:
                    print("Cannot pop from an empty set")
                else:
                    popped = my_set.pop()
                    print(f"Popped random element: {popped}")
                    print(f"Set after pop: {my_set}")

            elif modification.startswith('c'):
                confirm = input("Are you sure you want to clear the set? (y/n): ").lower()
                if confirm.startswith('y'):
                    my_set.clear()
                    print("Set cleared:", my_set)

        elif choice == '2':
            # Set operations with another set
            print("Let's create another set to perform operations with yours")
            items2 = []
            while True:
                item = input("Enter an item for the second set (or 'done' to finish): ")
                if item.lower() == 'done':
                    break

                # Try to convert to number if applicable
                try:
                    if '.' in item:
                        item = float(item)
                    elif item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
                        item = int(item)
                except ValueError:
                    pass

                items2.append(item)

            other_set = set(items2) if items2 else {4, 5, 6, 7, 8}
            if not items2:
                print(f"Using default second set: {other_set}")

            print(f"\nYour set: {my_set}")
            print(f"Other set: {other_set}")

            print("\nSet Operations:")
            union = my_set | other_set
            print(f"Union (elements in either set): {union}")

            intersection = my_set & other_set
            print(f"Intersection (elements in both sets): {intersection}")

            diff1 = my_set - other_set
            print(f"Difference (elements in your set but not in other): {diff1}")

            diff2 = other_set - my_set
            print(f"Difference (elements in other set but not in yours): {diff2}")

            sym_diff = my_set ^ other_set
            print(f"Symmetric Difference (elements in either set, but not both): {sym_diff}")

            # Ask if they want to update their set
            op_choice = input("\nWould you like to update your set with one of these results? (y/n): ").lower()
            if op_choice.startswith('y'):
                update_choice = input("Which result? (u)nion, (i)ntersection, your (d)ifference, (s)ymmetric difference: ").lower()

                if update_choice.startswith('u'):
                    my_set = union
                elif update_choice.startswith('i'):
                    my_set = intersection
                elif update_choice.startswith('d'):
                    my_set = diff1
                elif update_choice.startswith('s'):
                    my_set = sym_diff
                else:
                    print("Invalid choice, set not updated")

                print(f"Your set is now: {my_set}")

        elif choice == '3':
            # Membership and subset relationships
            print("Let's create another set to check relationships")
            items2 = []
            while True:
                item = input("Enter an item for the comparison set (or 'done' to finish): ")
                if item.lower() == 'done':
                    break

                # Try to convert to number if applicable
                try:
                    if '.' in item:
                        item = float(item)
                    elif item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
                        item = int(item)
                except ValueError:
                    pass

                items2.append(item)

            other_set = set(items2) if items2 else {1, 2, 3}
            if not items2:
                print(f"Using default comparison set: {other_set}")

            print(f"\nYour set: {my_set}")
            print(f"Comparison set: {other_set}")

            # Check membership for a specific element
            check_element = input("\nEnter an element to check membership in both sets: ")
            # Convert to appropriate type if it looks like a number
            try:
                if '.' in check_element:
                    check_element = float(check_element)
                elif check_element.isdigit() or (check_element.startswith('-') and check_element[1:].isdigit()):
                    check_element = int(check_element)
            except ValueError:
                pass

            print(f"'{check_element}' in your set: {check_element in my_set}")
            print(f"'{check_element}' in comparison set: {check_element in other_set}")

            # Check subset/superset relationships
            print(f"\nSubset/Superset Relationships:")
            print(f"Your set is subset of comparison: {my_set.issubset(other_set)}")
            print(f"Your set is proper subset of comparison: {my_set < other_set}")
            print(f"Your set is superset of comparison: {my_set.issuperset(other_set)}")
            print(f"Your set is proper superset of comparison: {my_set > other_set}")
            print(f"Sets are disjoint (no common elements): {my_set.isdisjoint(other_set)}")
            print(f"Sets are equal: {my_set == other_set}")

        elif choice == '4':
            # Convert to other data types
            print("\nConverting set to other data types:")
            print(f"As list: {list(my_set)}")
            print(f"As tuple: {tuple(my_set)}")

            if all(isinstance(x, str) for x in my_set):
                print(f"Join as string: {''.join(my_set)}")
            elif all(isinstance(x, (int, float)) for x in my_set):
                print(f"Sum: {sum(my_set)}")
                print(f"Average: {sum(my_set)/len(my_set) if my_set else 0}")

            # Convert to frozen set
            frozen = frozenset(my_set)
            print(f"As frozen set: {frozen}")
            print("Note: Frozen sets are immutable and can be used as dictionary keys or elements of another set")

        elif choice == '5':
            # Find unique elements between collections
            print("Let's compare your set with another collection to find unique elements")

            collection_type = input("Compare with a (l)ist, (s)tring, or another (s)et? ").lower()
            other_collection = []

            if collection_type.startswith('l'):
                # Get a list
                while True:
                    item = input("Enter a list item (or 'done' to finish): ")
                    if item.lower() == 'done':
                        break

                    # Try to convert to number if applicable
                    try:
                        if '.' in item:
                            item = float(item)
                        elif item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
                            item = int(item)
                    except ValueError:
                        pass

                    other_collection.append(item)

                if not other_collection:
                    other_collection = [1, 2, 3, 4, 10, 11]
                    print(f"Using default list: {other_collection}")

                other_set = set(other_collection)

            elif collection_type.startswith('s') and len(collection_type) > 1 and collection_type[1] == 't':
                # Get a string
                text = input("Enter a string: ") or "hello world"
                if not text:
                    text = "hello world"
                    print(f"Using default string: {text}")

                other_collection = text
                other_set = set(text)

            else:
                # Get another set
                while True:
                    item = input("Enter a set item (or 'done' to finish): ")
                    if item.lower() == 'done':
                        break

                    # Try to convert to number if applicable
                    try:
                        if '.' in item:
                            item = float(item)
                        elif item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
                            item = int(item)
                    except ValueError:
                        pass

                    other_collection.append(item)

                if not other_collection:
                    other_collection = [3, 4, 5, 6, 7]
                    print(f"Using default set: {set(other_collection)}")

                other_set = set(other_collection)

            print(f"\nYour set: {my_set}")
            print(f"Other collection as set: {other_set}")

            print("\nUnique Elements Analysis:")
            print(f"Elements unique to your set: {my_set - other_set}")
            print(f"Elements unique to other collection: {other_set - my_set}")
            print(f"Elements in either collection: {my_set | other_set}")
            print(f"Elements in both collections: {my_set & other_set}")
            print(f"Elements in exactly one collection: {my_set ^ other_set}")

        elif choice == '6':
            print("\nExiting set demo...")
            break

        else:
            print("Invalid choice, please try again.")

    return "Set demo completed"