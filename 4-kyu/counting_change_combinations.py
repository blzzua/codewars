# https://www.codewars.com/kata/541af676b589989aed0009e7

def count_change_recurisve(money, coins, n):
    if money == 0:
        return 1
    elif money < 0 or len(coins) == n:
        return 0
    else:
        return count_change_recurisve(money - coins[n], coins, n) + count_change_recurisve(money, coins, n + 1)

def count_change(money, coins):
    return count_change_recurisve(money, coins, 0)

# clever nonrecursive solution:
tries = {0: 1}
for coin in coins:
    for i in range(coin, money + 1):
        tries[i] = tries.get(i,0) + tries.get(i - coin, 0)
return tries[money]
