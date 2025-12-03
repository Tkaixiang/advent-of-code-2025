banks = []

with open("input.txt", "r") as file:
    banks = [line.strip() for line in file.readlines()]


# Need to do DP for this - Classical coin pick DP problem
# Each dp[idx][remaining_len] returns the largest combination of joltage (in str)
# E.g dp[2][12] # Starting at idx 2, with 12 chars, what is the best combi
memo = []


def dp(idx, remaining_len, bank, memo):
    if idx == len(bank) or remaining_len == 0:
        return ""

    if memo[idx][remaining_len]:
        return memo[idx][remaining_len]

    # Pick this digit or not
    choose_current_str = bank[idx] + dp(idx + 1, remaining_len - 1, bank, memo)
    choose_current = int(choose_current_str)

    # If our remaining_len >= remaining bank len, we can no longer afford to NOT pick
    remaining_bank_len = len(bank) - idx
    if remaining_len >= remaining_bank_len:
        return choose_current_str

    do_not_choose_current_str = dp(idx + 1, remaining_len, bank, memo)
    do_not_choose_current = int(do_not_choose_current_str)

    # If choosing the current digit results in a greater battery, choose the current
    if choose_current > do_not_choose_current:
        memo[idx][remaining_len] = choose_current_str
        return choose_current_str

    memo[idx][remaining_len] = do_not_choose_current_str
    return do_not_choose_current_str


total = 0
for bank_idx, bank in enumerate(banks):
    # Re-init memo table
    memo = []
    for x in range(0, len(bank), 1):
        memo.append([False for y in range(13)])

    largest_joltage = int(dp(0, 12, bank, memo))
    total += largest_joltage
    print(f"Processed {bank_idx}/{len(banks)}")

print(total)
