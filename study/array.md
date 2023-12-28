## Introduction

Arrays hold values of the same type at contiguous memory locations. In an array, we're usually concerned about two things - the position/index of an element and the element itself.

## Advantages

- Store multiple elements of the same type with one single variable name
- Accessing elements is fast as long you have the index, as opposed to linked lists where you have to traverse from head.

## Disadvantages

- Addition and removeal of elements into/from the middle of an array is slow because the remaining elements need to be shifted to accomodate the new/missing element. An exception to this is if the position to be inserted/removed is at the end of the array.

- If we cannot alter the size of an array after initialization. Insertion can be O(n) if we have to resize the array. The new array has to be allocated and existing elements have to be copied over.
  [arrays in python](https://www.guru99.com/array-data-structure.html)

## Common Terms

- Subarray A range of contiguous values within an array.
- Subsequence A sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements

## Time Complexity

| Operation            | Big-0     | Note                                                                                                  |
| -------------------- | --------- | ----------------------------------------------------------------------------------------------------- |
| Access               | 0(1)      |                                                                                                       |
| Search               | 0(n)      |                                                                                                       |
| Search(sorted)       | 0(log(n)) |                                                                                                       |
| Insert               | 0(n)      | Insertion would require shifting all the subsequent elements to thte right by one and that takes O(n) |
| Insert(at the end)   | O(1)      | Special case of insertion where no other element needs to be shifted                                  |
| Remove               | O(n)      | Removal would require shifting all the subsequent elements to the left by one and that takes O(n)     |
| Remove ( at the end) | O(1)      | Special case of remove where no other element needs to be shifted                                     |

## Techniques

1. Sliding window
2. Two pointers
3. Traversing from the right
4. Sorting the array - merge intervals, non-overlapping intervals
5. Prefix sum / Suffix sum product 2.
6. Index as a hash key

## Recommended problems

1. Two Sum
2. Best Time to Buy and Sell Stock
3. Product of Array Except Self
4. Maximum Subarray
5. Contains duplicate
6. Maximum Product Subarray
7. Search in Rotated Sorted Array
8. 3Sum
9. Contianer with most water
10. Sliding window maximum
