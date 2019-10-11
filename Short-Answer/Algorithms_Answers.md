#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) A single loop is O(n).

b) O(n^2) There is a nested while loop inside a for loop. The inner loop has a complexity O(n) and it is run n times.

c) O(n)

## Exercise II

In this case we would use Binary Search because floors of a building can be considered a sorted array. The floors are in numeric order from 1, being the first floor to whatever the number on the last floor would be depending on the how many floors the building has in total.

Binary search inputs a sorted list of elements and outputs the position at which the element is located if found within the list. Otherwise it returns null. The algorithm runs in O(n log n) time. It does this by finding the mid point(mid) a the list and comparing the value in it to elements on its left(low) and right(high) side and discarding the side that could not possibly contain the value you are looking for and repeating the process until you find it. The first time you discard you already eliminate half of the remaing values every time.
