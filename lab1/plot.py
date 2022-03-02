import matplotlib.pyplot as plt

from search import binary_search, linear_search

# [100, 200, 300, ...., 100000]
number_of_data = range(100, 100000, 100)

# Time Complexities
linear_worst_case_times = [linear_search(range(num), num)["duration"] for num in number_of_data]
binary_worst_case_times = [binary_search(range(num), num)["duration"] for num in number_of_data]

linear_best_case_times = [linear_search(range(num), 0)["duration"] for num in number_of_data]
binary_best_case_times = [binary_search(range(num), (num - 1) // 2)["duration"] for num in number_of_data]


fig, (plt1, plt2) = plt.subplots(nrows=1, ncols=2)

plt1.plot(number_of_data, binary_worst_case_times, ".", label="Worst Case")
plt1.plot(number_of_data, binary_best_case_times, "*", label="Best Case")
plt1.set_xlabel("Array Size")
plt1.set_ylabel("Time (in microseconds)")
plt1.set_title("Binary Search")
plt1.legend()

plt2.plot(number_of_data, linear_worst_case_times, ".", label="Worst Case")
plt2.plot(number_of_data, linear_best_case_times, "*", label="Best Case")
plt2.set_xlabel("Array Size")
plt2.set_ylabel("Time (in microseconds)")
plt2.set_title("Linear Search")
plt2.legend()

plt.show()
