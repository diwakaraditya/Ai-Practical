#Implement Greedy search algorithm for Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i

        # Find the index of the minimum element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

            # Print the array after each swap to show progress
            print(f"Step {i + 1}: {' '.join(map(str, arr))}")

def main():
    # Take user input
    n = int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter the elements: ").split()))

    # Perform the selection sort with step-by-step output
    selection_sort(arr)

    # Print the final sorted array
    print("Final sorted array:", ' '.join(map(str, arr)))

if __name__ == "__main__":
    main()


#sample output Enter the number of elements: 5
#Enter the elements: 64 25 12 22 11
#Step 1: 11 25 12 22 64
#Step 2: 11 12 25 22 64
#Step 3: 11 12 22 25 64
#Final sorted array: 11 12 22 25 64
