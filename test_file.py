def same_parity(numbers: list[int]) -> list:
    new_list = []
    for i in range(len(numbers)):
        if numbers[0] % 2 and numbers[i] % 2:
            new_list.append(numbers[i])
        elif numbers[0] % 2 == 0 and numbers[i] % 2 == 0:
            new_list.append(numbers[i])
    return new_list


nums: list = [int(i) for i in input().split(',')]

print(same_parity(nums))
