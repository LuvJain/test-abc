"""
Lists in Python

This module demonstrates the usage of lists, one of Python's most versatile
and commonly used data structures. Lists are ordered, mutable sequences
that can hold elements of different types.
"""


def create_list_examples():
    """
    Create and return examples of different list creation methods.

    Returns:
        dict: A dictionary mapping example names to the created lists
    """
    examples = {}

    # Empty list
    examples["empty_list"] = []

    # List with initial values
    examples["numbers"] = [1, 2, 3, 4, 5]

    # List with mixed data types
    examples["mixed_types"] = [1, "hello", 3.14, True, [1, 2]]

    # List created with the list() constructor
    examples["from_constructor"] = list("Python")  # Creates a list of characters

    # List created using list comprehension
    examples["comprehension"] = [x**2 for x in range(1, 6)]  # Squares of 1 to 5

    # List created from another sequence
    examples["from_tuple"] = list((10, 20, 30))

    # List with repeated elements
    examples["repeated"] = [0] * 5  # [0, 0, 0, 0, 0]

    # Nested lists (list of lists)
    examples["nested"] = [[1, 2], [3, 4], [5, 6]]

    return examples


def list_access_examples(sample_list):
    """
    Demonstrate different ways to access elements in a list.

    Args:
        sample_list (list): The list to access elements from

    Returns:
        dict: A dictionary of examples showing different access patterns
    """
    if not sample_list:
        sample_list = [10, 20, 30, 40, 50, 60, 70]

    examples = {}

    # Accessing by index
    examples["first_element"] = sample_list[0]  # First element (index 0)
    examples["third_element"] = sample_list[2]  # Third element (index 2)

    # Negative indexing
    examples["last_element"] = sample_list[-1]  # Last element
    examples["second_to_last"] = sample_list[-2]  # Second to last element

    # Slicing
    examples["first_three"] = sample_list[:3]  # First three elements
    examples["middle_three"] = sample_list[2:5]  # Elements from index 2 to 4
    examples["last_three"] = sample_list[-3:]  # Last three elements

    # Slicing with step
    examples["every_second"] = sample_list[::2]  # Every second element
    examples["reversed"] = sample_list[::-1]  # List in reverse

    return examples


def list_modification_examples():
    """
    Demonstrate various ways to modify lists.

    Returns:
        dict: Examples of list modifications
    """
    examples = {}

    # Changing elements
    change_list = [1, 2, 3, 4, 5]
    change_list[2] = 30  # Change the third element
    examples["change_element"] = change_list  # [1, 2, 30, 4, 5]

    # Appending elements
    append_list = [1, 2, 3]
    append_list.append(4)  # Add to the end
    examples["append"] = append_list  # [1, 2, 3, 4]

    # Extending a list
    extend_list = [1, 2, 3]
    extend_list.extend([4, 5])  # Add multiple elements
    examples["extend"] = extend_list  # [1, 2, 3, 4, 5]

    # Inserting elements
    insert_list = [1, 2, 4, 5]
    insert_list.insert(2, 3)  # Insert at index 2
    examples["insert"] = insert_list  # [1, 2, 3, 4, 5]

    # Removing elements
    remove_list = [1, 2, 3, 4, 3, 5]
    remove_list.remove(3)  # Remove first occurrence of 3
    examples["remove"] = remove_list  # [1, 2, 4, 3, 5]

    # Removing by index
    pop_list = [1, 2, 3, 4, 5]
    popped = pop_list.pop(2)  # Remove and return element at index 2
    examples["pop"] = {"list": pop_list, "popped_value": popped}  # [1, 2, 4, 5], 3

    # Clearing a list
    clear_list = [1, 2, 3]
    clear_list.clear()  # Remove all elements
    examples["clear"] = clear_list  # []

    # List concatenation
    examples["concatenation"] = [1, 2, 3] + [4, 5]  # [1, 2, 3, 4, 5]

    return examples


def list_operations_examples():
    """
    Demonstrate common list operations and methods.

    Returns:
        dict: Examples of list operations
    """
    examples = {}

    # Length of a list
    examples["length"] = len([1, 2, 3, 4, 5])  # 5

    # Check membership
    examples["membership"] = 3 in [1, 2, 3, 4, 5]  # True

    # Count occurrences
    count_list = [1, 2, 3, 2, 4, 2, 5]
    examples["count"] = count_list.count(2)  # 3 (occurrences of 2)

    # Find index
    index_list = [10, 20, 30, 40, 50]
    examples["index"] = index_list.index(30)  # 2 (index of value 30)

    # Sorting
    sort_list = [3, 1, 4, 1, 5, 9, 2]
    sort_list.sort()  # Sort in place
    examples["sort"] = sort_list  # [1, 1, 2, 3, 4, 5, 9]

    # Sorting with key function
    words = ["apple", "Banana", "cherry", "Date"]
    sorted_words = sorted(words, key=str.lower)  # New sorted list, case-insensitive
    examples["sorted"] = sorted_words  # ['apple', 'Banana', 'cherry', 'Date']

    # Reversing
    reverse_list = [1, 2, 3, 4, 5]
    reverse_list.reverse()  # In-place reversal
    examples["reverse"] = reverse_list  # [5, 4, 3, 2, 1]

    # Min and max
    number_list = [3, 1, 4, 1, 5, 9, 2]
    examples["min"] = min(number_list)  # 1
    examples["max"] = max(number_list)  # 9

    # Sum
    examples["sum"] = sum(number_list)  # 25

    # List comprehensions
    examples["comprehension_filter"] = [x for x in range(10) if x % 2 == 0]  # Even numbers
    examples["comprehension_transform"] = [x**2 for x in range(1, 6)]  # Squares

    # Copy a list
    original = [1, 2, 3]
    # Shallow copy methods
    examples["copy_method"] = original.copy()  # Using copy method
    examples["copy_slicing"] = original[:]  # Using slicing
    examples["copy_constructor"] = list(original)  # Using list constructor

    # Nested list copy (shallow vs deep)
    import copy
    nested_original = [1, [2, 3], 4]
    examples["shallow_copy"] = nested_original.copy()  # Nested lists share references
    examples["deep_copy"] = copy.deepcopy(nested_original)  # Complete independent copy

    return examples


def list_iteration_examples():
    """
    Demonstrate different ways to iterate through lists.

    Returns:
        dict: Examples of list iteration techniques
    """
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    examples = {}

    # Basic for loop
    results_basic = []
    for fruit in fruits:
        results_basic.append(f"I like {fruit}s")
    examples["basic_loop"] = results_basic

    # Enumeration
    results_enum = []
    for i, fruit in enumerate(fruits):
        results_enum.append(f"{i+1}. {fruit}")
    examples["enumeration"] = results_enum

    # List comprehension
    examples["comprehension"] = [fruit.upper() for fruit in fruits]

    # Multiple lists with zip
    vegetables = ["carrot", "broccoli", "spinach"]
    pairs = []
    for fruit, veggie in zip(fruits[:3], vegetables):  # Zip stops at the shortest list
        pairs.append(f"{fruit} and {veggie}")
    examples["zip"] = pairs

    # Filtered iteration
    filtered = []
    for fruit in fruits:
        if 'e' in fruit:
            filtered.append(fruit)
    examples["filtered_loop"] = filtered

    return examples


def list_performance_tips():
    """
    Provide performance tips for working with lists.

    Returns:
        dict: Performance tips for lists
    """
    return {
        "append_vs_concatenation": "Prefer list.append() over += for adding single items (faster)",
        "extend_vs_concatenation": "Prefer list.extend() over += for adding multiple items (faster)",
        "list_comprehension": "List comprehensions are faster than manual for-loop list building",
        "length_check": "Use 'if not my_list' instead of 'if len(my_list) == 0' for empty list check",
        "copy_large_lists": "Be careful with large list copies - they consume memory",
        "avoid_insert": "Avoid list.insert(0, x) for stack operations - use collections.deque instead",
        "join_strings": "Use ''.join(string_list) instead of += to concatenate many strings",
        "sorted_vs_sort": "Use list.sort() for in-place sorting, sorted() when you need the original list"
    }


def common_list_patterns():
    """
    Demonstrate common programming patterns using lists.

    Returns:
        dict: Common list programming patterns
    """
    examples = {}

    # Filtering
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    examples["filter_evens"] = [x for x in numbers if x % 2 == 0]
    examples["filter_function"] = list(filter(lambda x: x > 5, numbers))

    # Mapping
    examples["map_squares"] = [x**2 for x in numbers]
    examples["map_function"] = list(map(lambda x: x*2, numbers))

    # Accumulation pattern
    total = 0
    for num in numbers:
        total += num
    examples["accumulation"] = total

    # Finding maximum/minimum with conditions
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
    examples["longest_word"] = max(words, key=len)
    examples["shortest_word"] = min(words, key=len)

    # Counting occurrences
    from collections import Counter
    letters = ["a", "b", "a", "c", "b", "a", "d"]
    examples["counter"] = dict(Counter(letters))

    # Grouping (using dictionary)
    animals = ["cat", "dog", "crow", "deer", "dolphin", "cobra"]
    grouped_by_first_letter = {}
    for animal in animals:
        first_letter = animal[0]
        if first_letter not in grouped_by_first_letter:
            grouped_by_first_letter[first_letter] = []
        grouped_by_first_letter[first_letter].append(animal)
    examples["grouping"] = grouped_by_first_letter

    # List flattening
    nested_list = [[1, 2], [3, 4], [5, 6]]
    examples["flatten_comprehension"] = [item for sublist in nested_list for item in sublist]

    # Remove duplicates
    duplicates = [1, 2, 2, 3, 4, 3, 5, 1, 6]
    examples["remove_duplicates"] = list(dict.fromkeys(duplicates))  # Order-preserving
    examples["remove_duplicates_set"] = list(set(duplicates))  # Order not guaranteed

    return examples


def interactive_list_demo():
    """
    Function for interactive list operation demonstration.

    This function can be called from a main script to allow users to
    interactively try list operations.
    """
    print("\n=== Python Lists Interactive Demo ===\n")

    # Create a list
    my_list = []
    print(f"Created empty list: {my_list}")

    # Add items
    while True:
        item = input("\nEnter an item to add to the list (or 'done' to continue): ")
        if item.lower() == 'done':
            break

        # Try to convert to int or float if it looks like a number
        try:
            if '.' in item:
                item = float(item)
            else:
                item = int(item)
        except ValueError:
            # Keep as string if not convertible
            pass

        my_list.append(item)
        print(f"List now contains: {my_list}")

    if not my_list:
        # Use a default list if the user didn't add any items
        my_list = [1, 2, 3, 4, 5]
        print(f"\nUsing default list: {my_list}")

    print("\n=== List Operations ===")

    while True:
        print("\nCurrent list:", my_list)
        print("\nChoose an operation:")
        print("1. Access elements (by index or slice)")
        print("2. Add elements (append or insert)")
        print("3. Remove elements (remove, pop)")
        print("4. Sort the list")
        print("5. Reverse the list")
        print("6. Find element (index, count)")
        print("7. List information (length, min, max, sum)")
        print("8. Create a new list from this one (map, filter)")
        print("9. Exit demo")

        choice = input("\nEnter your choice (1-9): ")

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
                        result = my_list[start:end]
                    else:
                        result = my_list[start:end:step]
                else:
                    # It's an index
                    result = my_list[int(index_input)]
                print(f"Result: {result}")
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")

        elif choice == '2':
            # Add elements
            add_type = input("(a)ppend or (i)nsert? ").lower()

            item = input("Enter the item to add: ")
            try:
                # Convert to number if it looks like one
                if '.' in item:
                    item = float(item)
                else:
                    try:
                        item = int(item)
                    except ValueError:
                        # Keep as string
                        pass

                if add_type.startswith('i'):
                    position = int(input("Enter the position to insert at: "))
                    my_list.insert(position, item)
                else:
                    my_list.append(item)

                print(f"Updated list: {my_list}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            # Remove elements
            if not my_list:
                print("List is already empty!")
                continue

            remove_type = input("(r)emove by value or (p)op by index? ").lower()

            try:
                if remove_type.startswith('p'):
                    index_input = input("Enter index to pop (or leave empty for last element): ")
                    if index_input:
                        removed = my_list.pop(int(index_input))
                    else:
                        removed = my_list.pop()
                    print(f"Removed: {removed}")
                else:
                    value = input("Enter value to remove: ")
                    # Try to convert to a number if it might be one
                    try:
                        if '.' in value:
                            value = float(value)
                        else:
                            value = int(value)
                    except ValueError:
                        # Keep as string
                        pass

                    my_list.remove(value)

                print(f"Updated list: {my_list}")
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")

        elif choice == '4':
            # Sort the list
            try:
                reverse_input = input("Sort in reverse order? (y/n): ").lower()
                reverse = reverse_input.startswith('y')

                try:
                    my_list.sort(reverse=reverse)
                    print(f"Sorted list: {my_list}")
                except TypeError:
                    print("Error: Cannot sort a list with mixed types.")

                    # Offer to sort strings only
                    if input("Sort string elements only? (y/n): ").lower().startswith('y'):
                        str_items = [x for x in my_list if isinstance(x, str)]
                        str_items.sort(reverse=reverse)
                        print(f"Sorted strings: {str_items}")

                    # Offer to sort numbers only
                    if input("Sort numeric elements only? (y/n): ").lower().startswith('y'):
                        num_items = [x for x in my_list if isinstance(x, (int, float))]
                        num_items.sort(reverse=reverse)
                        print(f"Sorted numbers: {num_items}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '5':
            # Reverse the list
            my_list.reverse()
            print(f"Reversed list: {my_list}")

        elif choice == '6':
            # Find element
            find_type = input("(i)ndex of first occurrence or (c)ount occurrences? ").lower()

            value = input("Enter the value to find: ")
            # Try to convert to a number if it might be one
            try:
                if '.' in value:
                    value = float(value)
                else:
                    value = int(value)
            except ValueError:
                # Keep as string
                pass

            try:
                if find_type.startswith('i'):
                    idx = my_list.index(value)
                    print(f"First occurrence of {value} is at index {idx}")
                else:
                    count = my_list.count(value)
                    print(f"{value} appears {count} time(s) in the list")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '7':
            # List information
            print(f"Length: {len(my_list)}")

            # Check if we can compute min/max/sum
            all_numeric = all(isinstance(x, (int, float)) for x in my_list)

            if all_numeric and my_list:
                print(f"Minimum: {min(my_list)}")
                print(f"Maximum: {max(my_list)}")
                print(f"Sum: {sum(my_list)}")
                print(f"Average: {sum(my_list)/len(my_list):.2f}")
            elif my_list:
                print("Min/Max/Sum not available for mixed-type lists")

                # Check if we have any strings to find longest/shortest
                str_items = [x for x in my_list if isinstance(x, str)]
                if str_items:
                    print(f"Longest string: {max(str_items, key=len)}")
                    print(f"Shortest string: {min(str_items, key=len)}")

        elif choice == '8':
            # Create a new list (map, filter)
            operation = input("(m)ap or (f)ilter? ").lower()

            if operation.startswith('m'):
                print("Available transformations:")
                print("1. Double each number")
                print("2. Square each number")
                print("3. Convert to uppercase (strings)")
                print("4. Get length of each item")

                map_choice = input("Choose transformation (1-4): ")

                if map_choice == '1':
                    result = [x * 2 if isinstance(x, (int, float)) else x for x in my_list]
                elif map_choice == '2':
                    result = [x ** 2 if isinstance(x, (int, float)) else x for x in my_list]
                elif map_choice == '3':
                    result = [x.upper() if isinstance(x, str) else x for x in my_list]
                elif map_choice == '4':
                    result = [len(str(x)) for x in my_list]
                else:
                    print("Invalid choice")
                    continue

            else:  # Filter
                print("Available filters:")
                print("1. Even numbers only")
                print("2. Odd numbers only")
                print("3. Strings only")
                print("4. Numbers only")

                filter_choice = input("Choose filter (1-4): ")

                if filter_choice == '1':
                    result = [x for x in my_list if isinstance(x, (int, float)) and x % 2 == 0]
                elif filter_choice == '2':
                    result = [x for x in my_list if isinstance(x, (int, float)) and x % 2 != 0]
                elif filter_choice == '3':
                    result = [x for x in my_list if isinstance(x, str)]
                elif filter_choice == '4':
                    result = [x for x in my_list if isinstance(x, (int, float))]
                else:
                    print("Invalid choice")
                    continue

            print(f"Result: {result}")
            if input("Replace current list with this result? (y/n): ").lower().startswith('y'):
                my_list = result

        elif choice == '9':
            break

        else:
            print("Invalid choice, please try again.")

    print("\nThanks for exploring Python lists!")