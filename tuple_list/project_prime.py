#simulate an app that checks for a prime number.
nums = [1,2,3,4,5,6,7,8,9,10]
prime_num = []
troi = 20
for num in nums:
    if troi % num != 0:
        prime_num.append(troi)
    print(prime_num)
