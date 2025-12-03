ranges = []
with open("input.txt") as f:
    ranges = f.read().strip().split(",")

sum_invalid_ID = 0
# Im lazy so let's bruteforce
for current_range in ranges:
    splitted = current_range.split("-")
    start = int(splitted[0].strip())
    end = int(splitted[1].strip())
    for i in range(start, end + 1, 1):
        num_stringified = str(i)
        if len(num_stringified) % 2 != 0:
            continue  # Skip any odd number lengths (since it can't host a repeating pattern)
        # Invalid IDs are some sequence of digits REPEATED TWICE
        # Which means, we just need to compare: 1st half + 2nd half same
        mid = int(len(num_stringified) / 2)
        first_part = num_stringified[0:mid]
        second_part = num_stringified[mid : len(num_stringified)]
        if first_part == second_part:
            sum_invalid_ID += i

print(sum_invalid_ID)
