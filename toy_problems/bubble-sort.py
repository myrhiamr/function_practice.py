def bubble_sort(lst):
	for i in range(len(lst) - 1):
		swapped = False
		print(f"Pass", i + 1)
		for j in range(len(lst) - 1):
			print(f"Comparing {lst[j]} to {lst[j+1]}")
			if lst[j] > lst[j+1]:
				# Standard (long) way to swap list elements
				# temp = lst[j]
				# lst[j] = lst[j+1]
				# lst[j+1] = temp

				# List unpacking (shortcut) way to swap list elements
				lst[j], lst[j+1] = lst[j+1], lst[j]
				swapped = True
		if not swapped:
			return lst

	return lst

sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
print("Sorted list:", bubble_sort(sample_list))
# print(f"Sorted list: {sample_list}")
