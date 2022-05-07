import itertools


def weight(solution, W):
    return sum([x*y for x, y in zip(solution, W)])


def profit(solution, P):
    return sum([x*y for x, y in zip(solution, P)])


def zero_one_bruteforce(P, W, M):
    n = len(P)
    solutions = [bin(i)[2:].rjust(n, "0") for i in range(2**n)]
    solutions = [[int(x) for x in solution] for solution in solutions]
    profits = [profit(solution, P) for solution in solutions]
    weights = [weight(solution, W) for solution in solutions]

    max_profit = -1
    solution = None

    for i in range(len(solutions)):
        if weights[i] <= M:
            if profits[i] > max_profit:
                solution = solutions[i]
                max_profit = profits[i]

    return solution, max_profit


def fractional_bruteforce(P, W, M):
    n = len(P)
    profit_weight_ratio = [x/y for x, y in zip(P, W)]

    temp = []
    for weight in W:
        bit_strings = [bin(x)[2:].rjust(weight, "0") for x in range(2**weight)]
        temp.append(bit_strings)

    max_profit = 0
    solution = []

    for combination in list(itertools.product(*temp)):
        profit = weight = 0

        for i in range(n):
            profit += sum([int(combination[i][j]) * profit_weight_ratio[i] for j in range(W[i])])
            weight += sum([int(combination[i][j]) for j in range(W[i])])

        if weight <= M and profit > max_profit:
            max_profit = profit
            solution = combination

    solution = []
    for i in range(n):
        weight_ratio = sum([int(solution[i][j]) / W[i] for j in range(W[i])])
        solution.append(round(weight_ratio, 2))
    return solution, max_profit


def fractional_greedy(P, W, M):
    n = len(P)
    profit_weight_ratio = [x/y for x, y in zip(P, W)]
    index = [i for i in range(n)]

    index.sort(key=lambda i: profit_weight_ratio[i], reverse=True)

    max_profit = 0
    solution = [0 for _ in range(n)]

    for i in index:
        if W[i] <= M:
            solution[i] = 1
            max_profit += P[i]
            M -= W[i]
        else:
            solution[i] = round(M / W[i], 2)
            max_profit += P[i] * (M / W[i])
            break

    return solution, max_profit


def zero_one_dynamic(P, W, M):
    n = len(P)
    tabulated_data = [[0 for _ in range(M + 1)] for _ in range(n + 1)]
    chosen_items = [[0 for _ in range(M + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for x in range(M + 1):
            profit1 = P[i-1] + tabulated_data[i-1][x-W[i-1]]
            profit2 = tabulated_data[i-1][x]
            if i == 0 or x == 0:
                tabulated_data[i][x] = 0
            elif W[i-1] <= x:
                tabulated_data[i][x] = max(profit1, profit2)
                if profit1 > profit2:
                    chosen_items[i][x] = 1
            else:
                tabulated_data[i][x] = profit2

    picks = []
    K = M
    for i in range(n, 0, -1):
        if chosen_items[i][K] == 1:
            picks.append(i)
            K -= W[i-1]
    picks.sort()
    picks = [x-1 for x in picks]

    solution = [1 if z in picks else 0 for z in range(n)]
    max_profit = tabulated_data[n][M]

    return solution, max_profit


if __name__ == "__main__":
    P = [60, 100, 120]
    W = [10, 20, 30]
    M = 50

    print("0/1 Bruteforce: ", zero_one_bruteforce(P, W, M))
    print("Fractional Bruteforce: ", fractional_bruteforce(P, W, M))
    print("Fractional Greedy: ", fractional_greedy(P, W, M))
    print("0/1 Dynamic Programming: ", zero_one_dynamic(P, W, M))
