### Fenwick Tree (Binary Indexed Tree)

The Fenwick Tree, also known as the Binary Indexed Tree (BIT), is a data structure that efficiently supports cumulative frequency queries and updates on an array of values. It provides O(log n) time complexity for both update and query operations, making it suitable for tasks like counting inversions (bad pairs) efficiently.

#### Structure:
- **Initialization**: The Fenwick Tree is initialized with a size equal to the length of the array plus one (to accommodate 1-indexing).
- **Storage**: It typically stores the cumulative sums of elements in a binary tree structure, where each node's value represents the sum of a range of elements.
- **Representation**: The tree is usually implemented using an array (or list) for simplicity and efficiency.

#### Operations:
1. **Update Operation**:
   - Increments the value of a specific element in the array by a given amount.
   - The update operation involves updating all affected nodes in the Fenwick Tree to maintain the cumulative sums.
   - It uses bitwise operations to efficiently find the next node to update in the tree.

2. **Query Operation**:
   - Computes the cumulative sum of elements up to a specific index in the array.
   - The query operation involves traversing the Fenwick Tree from the specified index to the root, summing up the values along the way.
   - It also uses bitwise operations to efficiently find the next node to query in the tree.

#### Usage:
- **Prefix Sum Queries**: Fenwick Trees are commonly used to efficiently compute prefix sums of elements in an array.
- **Range Queries and Updates**: They can handle range queries and updates efficiently, making them useful in a variety of algorithms and data structures.
- **Inversion Counting**: Fenwick Trees can be used to efficiently count inversions in an array, which are pairs of indices (i, j) where i < j and nums[i] > nums[j].

#### Implementation:
- The provided code snippet demonstrates a Python implementation of the Fenwick Tree class, including methods for updating and querying the tree.
- This implementation assumes 1-indexing for simplicity but can be adjusted for 0-indexing if needed.
- The Fenwick Tree is versatile and can be adapted to various applications and problem scenarios where efficient cumulative frequency operations are required.
