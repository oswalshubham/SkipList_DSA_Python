#SkipList Data Structure
This project was a part of **Data Structures and Algorithms**, Master's level course, under guidance of Prof. Ravi Varadrajan.
The project is about **SkipList Data Structure**, and its implementation in Python.

A little overview about **SkipList**:

SkipList is implementation over Linked Lists, after which:
Time to search in a LinkedList(SkipList) is reduced to **O(logn)** from **O(n)**->(Normal search complexity of LinkedList).
Time to insert as well as remove is reduced to **O(logn)** from **O(n)**.

And how is this achieved in SkipList:
We can have multiple layers which act as expressways. Each layer contains few nodes, which can be at any position in LinkedList.

![image](https://user-images.githubusercontent.com/95557338/165607270-835ed3d1-97e1-4a03-83a4-c159ad529601.png)

It works as binary search for multiple levels, and hence O(logn) complexity can be achieved.

Its takes up some space, as we add extra levels with nodes, with in order to improve time we compromise space.

A little about implementation:

Each node object has key, value associated with it, and instead of just one link, we have an array of links which store the next node from current node level wise.

While inserting, we keep a track of nodes visited on each level before moving one level down. The height(or levels) in which the node to be inserted in determined randomly, and is inserted upto the height. Here's where we use the nodes we stored level wise while moving down. As we add the node up from level 0, we check the previous node at each level from stored nodes to determine where it has to be inserted on each level.

**Test.py** is interactive implementation starting from empty SkipList, and lets user enter their choice to either insert, delete, find, find closest key after, and display.
**PerformanceAnalyzer.py** analyses performance for different input sizes to check if the complexity remains almost same for any input size.

Hope you like the implementation!
