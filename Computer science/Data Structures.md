### Linked List
Arrays store elements in contiguous memory locations, resulting in easily calculable addresses for the elements stored and this allows faster access to an element at a specific index. Linked lists are less rigid in their storage structure and elements are usually not stored in contiguous locations, hence they need to be stored with additional tags giving a reference to the next element. This difference in the data storage scheme decides which data structure would be more suitable for a given situation.

- A linked list is a linear data structure that stores a collection of data elements dynamically.

- Nodes represent those data elements, and links or pointers connect each node.

- Each node consists of two fields, the information stored in a linked list and a pointer that stores the address of its next node.

- The last node contains null in its second field because it will point to no node.

- A linked list can grow and shrink its size, as per the requirement.

- It does not waste memory space.



### Stack
First-in last-out data structure
**Stack** is a linear data structure that follows a particular order in which the operations are performed. The order may be **LIFO(Last In First Out)** or **FILO(First In Last Out)**. LIFO implies that the element that is inserted last, comes out first and **FILO** implies that the element that is inserted first, comes out last.
### Queue
There are four different types of queues in data structures:
1. **Simple Queue**:
    - A simple queue is a linear data structure where elements are inserted at the rear (also called the "tail") and removed from the front (also called the "head").
    - It follows the FIFO (First-In-First-Out) principle, meaning the element that is added first will be removed first.
    - Simple queues are commonly used in various applications such as CPU scheduling, breadth-first search algorithms, and printer queues.
2. **Circular Queue**:
    - A circular queue is an improvement over the simple queue where the rear and front pointers wrap around the queue, forming a circle.
    - It addresses the inefficiency of the simple queue where the rear pointer reaches the end of the array, leaving unused space in the queue.
    - Circular queues effectively utilize the available space and allow for continuous insertion and deletion of elements without needing to shift elements.
    - To implement a circular queue, you need to use modular arithmetic to manage the wrapping of pointers around the array.
3. **Priority Queue**:
    - A priority queue is a type of queue where each element has a priority assigned to it.
    - Elements with higher priorities are dequeued before elements with lower priorities.
    - Priority queues can be implemented using various data structures such as arrays, linked lists, heaps, or binary search trees.
    - Common applications of priority queues include task scheduling, Dijkstra's algorithm, and Huffman coding.
4. **Double-Ended Queue (Deque)**:
    - A double-ended queue, also known as a deque, is a versatile data structure that allows insertion and deletion of elements from both the front and the rear ends.
    - Unlike a simple queue where elements are inserted and removed from only one end, a deque supports operations at both ends.
    - Deques can be implemented using arrays, linked lists, or other data structures.
    - They are useful in situations where elements need to be added or removed from both ends efficiently, such as implementing a deque as a stack or a queue.
### Hash Table

### Tree

#### Binary tree

#### Binary search tree

#### Full binary tree

#### Complete binary tree

#### Balanced tree