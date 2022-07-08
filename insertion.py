li = [24, 34, 31, 34, 23, 15, 18, 49, 25, 30, 48, 4, 3, 13, 27, 16, 5, 25, 35, 4, 7, 6, 10, 47, 30, 1, 42, 21, 12, 21, 35, 43, 25, 18, 12, 25, 27, 25, 47, 4, 27, 13, 29, 43, 33, 34, 23, 22, 28, 38]

def insertionSort(arr):
    for i in range(1, len(arr)): # start at index 1 and stop at end of array
        check = arr[i] # set current index to be the comparison 'card'
        j = i-1 # set the card to the left of the check 'card'
        while j >= 0 and check < arr[j] : # compare that index before instance of array is >=0 , and that the value of check is less than value of card to left
                arr[j + 1] = arr[j] # swap 'i' with current 'j', move the smaller value left
                j -= 1 # reset the card thats on the left
        arr[j + 1] = check # reset the check card to the one after the swapped card

insertionSort(li)
print(li)