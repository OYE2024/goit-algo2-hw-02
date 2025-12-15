
from ast import main

def find_min_max_dc(arr, low, high):
    # Function to find minimum and maximum using divide and conquer approach
    if low == high:
        return arr[low], arr[low]
    
    elif low + 1 == high: 
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    else:
        mid = (low + high) // 2
        min1, max1 = find_min_max_dc(arr, low, mid)
        min2, max2 = find_min_max_dc(arr, mid + 1, high)
        
        overall_min = min(min1, min2)
        overall_max = max(max1, max2)
        
        return overall_min, overall_max

def main():
    array = input("Enter numbers separated by spaces: ").split()
    array = [int(num) for num in array] 
    n = len(array)
    min_value, max_value = find_min_max_dc(array, 0, n - 1)
    print("Array:", array)
    print("Minimum value:", min_value)
    print("Maximum value:", max_value)

if __name__ == "__main__":
    main()
    