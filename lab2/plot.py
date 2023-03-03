import matplotlib.pyplot as plt

from sort import insertion_sort, merge_sort

array_sizes = range(10, 1000, 10)

insertion_best_case_execution_times = []
insertion_worst_case_execution_times = []
merge_sort_execution_times = []

for size in array_sizes:
    arr = list(range(size))
    reversed_arr = list(reversed(arr))
    insertion_best_case_execution_times.append(insertion_sort(arr))
    insertion_worst_case_execution_times.append(insertion_sort(reversed_arr))
    merge_sort_execution_times.append(merge_sort(arr, 0, len(arr) - 1))


# First plot
fig, (plt1, plt2) = plt.subplots(nrows=1, ncols=2)

plt1.plot(
    array_sizes,
    insertion_best_case_execution_times,
    "*",
    label="Best Case")
plt1.plot(
    array_sizes,
    insertion_worst_case_execution_times,
    ".",
    label="Worst Case")
plt1.set_title("Insertion Sort")
plt1.set_xlabel("Array Size")
plt1.set_ylabel("Execution Time (in ns)")
plt1.legend()

plt2.plot(array_sizes, merge_sort_execution_times, "*", label="Best Case")
plt2.set_title("Merge Sort")
plt2.set_xlabel("Array Size")
plt2.set_ylabel("Execution Time (in ns)")
plt2.legend()

plt.show()

# Second Plot
fig, (plt1, plt2) = plt.subplots(nrows=1, ncols=2)

plt1.plot(
    array_sizes,
    insertion_best_case_execution_times,
    "*",
    label="Best Case")
plt1.set_title("Insertion Sort Best Case")
plt1.set_xlabel("Array Size")
plt1.set_ylabel("Execution Time (in ns)")
plt1.legend()


plt2.plot(
    array_sizes,
    insertion_worst_case_execution_times,
    ".",
    label="Worst Case")
plt2.set_title("Insertion Sort Worst Case")
plt2.set_xlabel("Array Size")
plt2.set_ylabel("Execution Time (in ns)")
plt2.legend()

plt.show()
