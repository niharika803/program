def longest_subsequence_divisible_by_5(stone_values):
    # Initialize variables
    prefix_sum = 0
    remainder_index_map = {0: -1}  # To handle cases where the subsequence starts from index 0
    max_length = 0
    start_index = -1

    # Iterate through the list of stone values
    for i, value in enumerate(stone_values):
        prefix_sum += value
        remainder = prefix_sum % 5

        if remainder in remainder_index_map:
            # Calculate the length of the current valid subsequence
            prev_index = remainder_index_map[remainder]
            current_length = i - prev_index

            # Update max_length and start_index if a longer subsequence is found
            if current_length > max_length:
                max_length = current_length
                start_index = prev_index + 1
        else:
            # Store the first occurrence of this remainder
            remainder_index_map[remainder] = i

    # Extract the longest subsequence
    if max_length > 0:
        return stone_values[start_index:start_index + max_length]
    else:
        return []

# Example usage
stone_values = [4, 1, 2, 3, 5, 6]
result = longest_subsequence_divisible_by_5(stone_values)
print("Longest subsequence with sum divisible by 5:", result)