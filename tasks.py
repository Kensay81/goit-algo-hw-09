import random
import timeit

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    res = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            res[coin] = count
    return res

def find_min_coins(amount_test, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount_test + 1)
    dp[0] = 0
    coin_used = [[] for _ in range(amount_test + 1)]
    
    for i in range(1, amount_test + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin_used[i - coin] + [coin]
    
    result = {}
    for coin in coin_used[amount_test]:
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
    
    return result

print("Функція жадібного алгоритму\n")
amount = 113
used_coins = find_coins_greedy(amount)
print(f"Використані монети для суми {amount} - {used_coins}")
find_coins_time = timeit.timeit('find_coins_greedy(amount)', globals=globals(), number=10)
print(f"Час виконання find_coins_greedy{amount} - {find_coins_time} секунд")

amount_test = 1557
used_coins = find_coins_greedy(amount_test)
print(f"Використані монети для суми {amount_test} - {used_coins}")
find_coins_time = timeit.timeit('find_coins_greedy(amount_test)', globals=globals(), number=10)
print(f"Час виконання find_coins_greedy для суми {amount_test} - {find_coins_time} секунд")

amount_test = 55557
used_coins = find_coins_greedy(amount_test)
print(f"Використані монети для суми {amount_test} - {used_coins}")
find_coins_time = timeit.timeit('find_coins_greedy(amount_test)', globals=globals(), number=10)
print(f"Час виконання find_coins_greedy для суми {amount_test} - {find_coins_time} секунд\n")


print("Функція динамічного програмування\n")
amount = 113
used_coins = find_min_coins(amount)
print(f"Використані монети для суми {amount} - {used_coins}")
find_coins_time = timeit.timeit('find_min_coins(amount)', globals=globals(), number=10)
print(f"Час виконання find_min_coins для суми {amount} - {find_coins_time} секунд")

amount_test = 1557
used_coins = find_min_coins(amount_test)
print(f"Використані монети для суми {amount_test} - {used_coins}")
find_coins_time = timeit.timeit('find_min_coins(amount_test)', globals=globals(), number=10)
print(f"Час виконання find_min_coins для суми {amount_test} - {find_coins_time} секунд")


amount_test = 55557
used_coins = find_min_coins(amount_test)
print(f"Використані монети для суми {amount_test} - {used_coins}")
find_coins_time = timeit.timeit('find_min_coins(amount_test)', globals=globals(), number=10)
print(f"Час виконання find_min_coins для суми {amount_test} - {find_coins_time} секунд\n")

