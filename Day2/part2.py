ranges = []
with open("input.txt") as f:
    ranges = f.read().strip().split(",")

sum_invalid_ID = 0


def check_divisor(divisor, num_stringified):
    if len(num_stringified) % divisor != 0:
        # Does not split equally, skip
        return False

    # Divide it equally into x parts
    length_of_each_part = int(len(num_stringified) / divisor)
    part = num_stringified[0:length_of_each_part]  # init to first part

    for x in range(length_of_each_part, len(num_stringified), length_of_each_part):
        # print(f"comparing: {part} | {num_stringified[x : x + length_of_each_part]}")
        if part != num_stringified[x : x + length_of_each_part]:

            return False  # Not correct

    # print(f"correct number! {num_stringified}")
    return True


# Im lazy so let's bruteforce
for current_range in ranges:
    splitted = current_range.split("-")
    start = int(splitted[0].strip())
    end = int(splitted[1].strip())
    for i in range(start, end + 1, 1):
        num_stringified = str(i)
        # print(i)

        # Invalid IDs are some sequence of digits REPEATED >AT LEAST< TWICE
        # We could try to bruteforce the division then? 2 to len(num_stringified)
        for divisor in range(2, len(num_stringified) + 1, 1):
            if check_divisor(divisor, num_stringified):
                sum_invalid_ID += i
                break  # We found 1, onto the next number!


print(sum_invalid_ID)
