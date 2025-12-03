banks = []

with open("input.txt", "r") as file:
    banks = [line.strip() for line in file.readlines()]

total_joltage = 0
# Bruteforce strategy first
for bank in banks:
    largest_joltage = 0

    # Any 2 digit number formed will be larger than a single digit number
    # So we can just skip the last index since a one-digit only left_battery will always be less
    for left_battery_idx in range(0, len(bank) - 1, 1):
        left_battery = bank[left_battery_idx]
        for right_battery_idx in range(left_battery_idx + 1, len(bank), 1):
            joltage = int(left_battery + bank[right_battery_idx])
            if joltage > largest_joltage:
                largest_joltage = joltage

    total_joltage += largest_joltage

print(total_joltage)
