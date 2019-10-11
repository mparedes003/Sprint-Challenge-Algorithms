#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) A single loop is O(n).

b) O(n^2) There is a nested while loop inside a for loop. The inner loop has a complexity O(n) and it is run n times.

c) O(n)

## Exercise II

In this case we would use Binary Search because floors of a building can be considered a sorted array. The floors are in numeric order from 1, being the first floor to whatever the number on the last floor would be depending on the how many floors the building has in total.

Binary search inputs a sorted list of elements and outputs the position at which the element is located if found within the list. Otherwise it returns null. The algorithm runs in O(log n) time. It does this by finding the mid point(mid) a the list and comparing the value in it to elements on its left(low) and right(high) side and discarding the side that could not possibly contain the value you are looking for and repeating the process until you find it. The first time you discard you already eliminate half of the remaing values every time.

Given: n = the number of floors the building has

       f = the floor/point at which when an egg is dropped that it breaks upon impact when reaching the ground floor

Visualization: |ground floor| egg remains intact < f =< broken egg |n floor|

To find f, with the least amount of eggs dropped, we need find the middle floor of the building and drop an egg from there and see if it breaks when it hits the ground floor.

If it breaks, we know we do not need to try to drop an egg from any other higher floor. This is where half of the list is instantly eliminated. We would then need to find the middle of the remaining floors on the list and try an egg drop from there.

If it does not break, we know we do not need to try to drop an egg from any other lower floor. Half of the list is instantly eliminated.
We would then need to find the middle of the remaining floors on the list and try an egg drop from there.

We keep doing this until we have only 2 floors left in our list of floors. The higher of the 2 floors remaining is f.
