def remove_duplicates(sequence):
    seen = set()  # To track the seen elements
    result = []   # For list without duplicates

    # Iterate through each element in the sequence
    for item in sequence:
        if item not in seen:
            seen.add(item)  # Add the unseen elements to set
            result.append(item)  # Append non-duplicates to result list
    return result

# SAMPLE INPUT
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]

# SAMPLE TEST CASE:
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
