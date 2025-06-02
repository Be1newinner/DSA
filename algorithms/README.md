### 1. Linear DS

#### 1. Arrays/Lists

* **Operations: Traversal, Insertion, Deletion, Rotation**
    * **Algorithms/Patterns:**
        * **Two Pointers:** Extremely common. Used for problems requiring simultaneous traversal from different ends or keeping track of two positions.
            * *Examples:* Finding pairs with a given sum (sorted array), checking for palindromes, reversing an array/string in-place, removing duplicates from sorted array, partitioning arrays (e.g., separating even/odd numbers).
            * *Why it's important:* Efficiently reduces nested loops, often bringing $O(N^2)$ to $O(N)$ time complexity.
        * **Sliding Window:** For problems involving subarrays/substrings of a fixed or variable size.
            * *Examples:* Maximum sum subarray of size K, longest substring without repeating characters, minimum window substring, checking if a permutation of a string is present in another.
            * *Why it's important:* Optimizes problems that would otherwise require iterating through all possible subarrays/substrings. Crucial for problems involving contiguous segments.
        * **Kadane's Algorithm:** Specifically for "Maximum Subarray Sum" problem.
            * *Why it's important:* Classic dynamic programming (DP) problem, often a stepping stone to more complex DP. Shows the idea of optimal substructure.
        * **Prefix Sums:** For quickly querying sums of subarrays.
            * *Examples:* Range sum queries, subarray sum equals K.
            * *Why it's important:* Pre-computation allows $O(1)$ query time after an $O(N)$ pre-processing step.
    * **FAANG Insights:** Interviewers often test your ability to handle in-place modifications and edge cases (empty arrays, single elements, large inputs). Think about the space complexity implications of your approach.

#### 2. Strings

* **Algorithms/Patterns:**
    * **Two Pointers (again!):** For palindrome checks, reversing strings, validating parentheses.
    * **Hashing/Hash Maps:** For anagrams (counting character frequencies), finding duplicate characters, unique characters.
    * **String Manipulation (Built-in or Manual):** `StringBuilder` or similar for efficient concatenation/modification.
    * **Pattern Matching:**
        * **KMP (Knuth-Morris-Pratt):** While less frequent for direct implementation in *coding* interviews, understanding its *concept* (LPS array) is valuable. It's often used as a background for discussions on efficient string searching.
        * **Rabin-Karp:** Also less frequent for direct coding, but concept of rolling hash is important.
        * *More common for interviews:* Simple substring search or problems that can be solved with built-in functions or two-pointer/sliding window approaches first.
    * **Trie (covered later):** Crucial for prefix-based string problems.
    * **FAANG Insights:** Pay attention to character sets (ASCII, Unicode), case sensitivity, and empty strings. String problems often test your ability to handle edge cases and understand the cost of string immutability in some languages.

#### 3. Linked Lists

* **Operations: Reversing, Merging, Sorting**
    * **Algorithms/Patterns:**
        * **Two Pointers (Fast & Slow Pointers):** The most common technique for linked list problems.
            * *Examples:* Cycle detection (Floyd's Cycle-Finding Algorithm), finding the middle of a list, finding the $N^{th}$ node from the end.
            * *Why it's important:* Allows traversal and comparison of nodes at different speeds, critical for relative positioning without knowing list length.
        * **Reversal:** Iterative and recursive methods.
            * *Examples:* Reverse a linked list, reverse a linked list in groups of K, palindrome linked list.
            * *Why it's important:* Fundamental linked list operation, often a building block for more complex problems.
        * **Merging Sorted Lists:**
            * *Why it's important:* Often seen in "merge K sorted lists" (which uses a min-heap) or as part of a merge sort implementation on linked lists.
    * **FAANG Insights:** Be comfortable manipulating pointers correctly. Drawing diagrams is highly recommended. Understand the difference in complexity and elegance between iterative and recursive solutions. Edge cases: empty list, single node, two nodes.

#### 4. Stacks and Queues

* **Implementation using lists or collections**
    * **Algorithms/Patterns:**
        * **Valid Parentheses/Brackets:** Classic stack application.
        * **Next Greater Element/Smaller Element:** Directly uses a monotonic stack.
        * **Monotonic Stack/Queue:** Maintaining a stack/queue where elements are always in increasing or decreasing order.
            * *Examples:* Largest Rectangle in Histogram, Sliding Window Maximum (using a deque for monotonic queue).
            * *Why it's important:* Optimizes problems by efficiently finding nearest greater/smaller elements or window maximums in $O(N)$ time.
        * **BFS (Breadth-First Search):** Uses a queue implicitly or explicitly.
            * *Examples:* Shortest path in unweighted graphs, level order traversal of a tree, finding all reachable nodes.
            * *Why it's important:* Guarantees finding the shortest path in terms of number of edges.
        * **Expression Evaluation:** Infix to Postfix conversion, evaluating postfix expressions.
        * **Browser History/Undo-Redo:** Conceptual use cases.
    * **FAANG Insights:** Understand when to use a stack (LIFO) vs. a queue (FIFO). Monotonic stacks/queues are a common "trick" for optimizing problems that might otherwise seem $O(N^2)$.

#### 5. Hashing

* **Hash Tables, Hash Maps**
    * **Algorithms/Patterns:**
        * **Frequency Counting:** For anagrams, finding unique elements, mode, etc.
        * **`O(1)` Lookups/Insertions/Deletions (average case):**
            * *Examples:* Two Sum, Subarray with Given Sum, finding duplicates in an array, checking for existence.
            * *Why it's important:* Transforms many $O(N^2)$ brute-force solutions to $O(N)$ by allowing quick lookups.
        * **Group Anagrams:** Using sorted strings or character counts as hash keys.
        * **Caching/Memoization:** Hash maps are the underlying data structure for dynamic programming memoization.
        * **Disjoint Set (Union-Find):** While not purely hashing, hash maps can be used to map arbitrary objects to indices if needed.
        * **FAANG Insights:** Be aware of worst-case scenarios (hash collisions leading to $O(N)$ operations), space-time trade-offs. Understand when to use a `HashSet` (for existence) vs. a `HashMap` (for key-value pairs/counts).

---

### 2. Non Linear DS

#### 1. Trees

* **Binary Trees, Binary Search Trees (BSTs)**
    * **Algorithms/Patterns:**
        * **Tree Traversals (DFS): In-order, Pre-order, Post-order:** Recursive implementations are common, iterative ones using a stack are often asked for deeper understanding.
            * *Why it's important:* Fundamental way to visit all nodes. In-order traversal of a BST yields sorted elements.
        * **BFS (Level Order Traversal):** Uses a queue.
            * *Why it's important:* Useful for problems requiring layer-by-layer processing, finding shortest path in unweighted tree.
        * **BST Specifics:** Insertion, deletion, search, finding min/max, validating if a tree is a BST.
            * *Why it's important:* Properties of BSTs (left < root < right) are frequently tested.
        * **Recursion:** Trees are inherently recursive. Many problems are solved elegantly with recursive thinking.
        * **Tree Properties:** Height, diameter, balanced tree checks.
        * **Lowest Common Ancestor (LCA):** A classic tree problem.
        * **Serialization/Deserialization:** Converting tree to string and back.
    * **Advanced (Less frequent for SDE1, but good to know concepts):**
        * **Trie:** Covered below.
        * **Segment Tree/Fenwick Tree (Binary Indexed Tree):** For range query problems (sum, min, max, etc.) on arrays that also involve updates. Highly optimized for specific competitive programming scenarios, sometimes seen in interviews for very specific roles.
    * **FAANG Insights:** Understand the difference between various traversals. Recursion is key. For BSTs, ensure you handle duplicates and edge cases. Practice drawing tree structures.

#### 2. Heaps

* **Min-Heap and Max-Heap (Priority Queues)**
    * **Algorithms/Patterns:**
        * **Top K Elements / Kth Smallest/Largest:** The most common application. Use a min-heap for largest K, a max-heap for smallest K.
        * **Median of Data Stream:** Maintaining two heaps (min-heap for upper half, max-heap for lower half).
        * **Merge K Sorted Lists/Arrays:** Using a min-heap to always get the smallest element across all lists.
        * **Dijkstra's Algorithm (Implicit use):** Uses a min-priority queue to efficiently extract the minimum distance vertex.
        * **Event Scheduling/Task Prioritization:** General applications.
    * **FAANG Insights:** Know the time complexity for heap operations ($O(\log N)$ for insert/delete, $O(1)$ for peek). Understand when to use a min-heap vs. a max-heap. Often a space-time tradeoff (e.g., sorting is $O(N \log N)$ but may be $O(1)$ space; heap solution is $O(N \log K)$ time and $O(K)$ space).

#### 3. Graphs

* **Representations: Adjacency Matrix/List**
    * **Algorithms/Patterns:**
        * **BFS (Breadth-First Search):** Shortest path in unweighted graphs, finding all connected components, level order traversal (for trees, which are special graphs).
        * **DFS (Depth-First Search):** Cycle detection, topological sort, finding connected components, path existence, backtracking.
        * **Topological Sorting:** For Directed Acyclic Graphs (DAGs). Kahn's algorithm (BFS-based) or DFS-based.
            * *Examples:* Course scheduling, task dependencies.
            * *Why it's important:* Orders nodes such that for every directed edge $U \to V$, $U$ comes before $V$.
        * **Dijkstra's Algorithm:** Shortest path in graphs with non-negative edge weights.
            * *Why it's important:* Standard algorithm for single-source shortest path problems.
        * **Minimum Spanning Tree (MST):** Kruskal's and Prim's algorithms.
            * *Why it's important:* Connects all vertices with minimum total edge weight. Less frequent for SDE1 coding but good to know concepts.
        * **Union-Find (Disjoint Set):** Used by Kruskal's, cycle detection in undirected graphs.
    * **FAANG Insights:** Mastering BFS/DFS is non-negotiable. Understand adjacency list vs. matrix suitability. Be ready to handle disconnected graphs, cycles, and directed/undirected graphs. Graph problems often test your ability to model real-world scenarios as graphs.

#### 4. Trie (Prefix Tree)

* **Algorithms/Patterns:**
    * **Prefix Search:** Autocomplete, spell checker.
    * **Word Search:** Finding words in a grid (often combined with DFS/backtracking).
    * **Longest Common Prefix:** Of a set of strings.
    * **Dictionary Implementation:** Efficient storage and retrieval of words based on prefixes.
    * **FAANG Insights:** Excellent for problems involving string prefixes. Know how to implement `insert`, `search`, and `startsWith`. Understand the space-time trade-off compared to hash maps (Tries can be more space-efficient for common prefixes, but worse for unique long strings).

#### 5. Disjoint Set (Union-Find)

* **Algorithms/Patterns:**
    * **Connectivity Problems:** Efficiently determining if two elements are in the same set/component.
    * **Cycle Detection in Undirected Graphs:** If adding an edge connects two already connected components, it forms a cycle.
    * **Kruskal's Algorithm:** Uses Union-Find to detect cycles when building an MST.
    * **Number of Connected Components:** In a graph or grid.
    * **Grid Problems:** Like "Number of Islands" or "Surrounded Regions" (can be solved with BFS/DFS too, but Union-Find offers an alternative perspective).
    * **FAANG Insights:** Crucial to implement with **path compression** and **union by rank/size** for near $O(\alpha(N))$ (amortized constant time) complexity. It's a powerful data structure for dynamic connectivity.

---

### Your Homework & Next Steps (FAANG-level Mentorship)

1.  **Complexity Analysis:** For *every* algorithm listed, you should be able to state its time and space complexity for best, average, and worst cases. For example, what's the space complexity of a recursive DFS on a skewed tree?
2.  **Implementation Practice:** Don't just understand the concept; implement these algorithms from scratch. Use your preferred stack (Node.js/TypeScript/Python).
3.  **Edge Cases:** Always ask yourself: What if the input is empty? What if it's null? What if it has one element? What if all elements are the same? What if constraints are at their maximum?
4.  **Problem Variations:** Once you solve a classic problem, try to think of 2-3 variations. For example, after "Two Sum," consider "Three Sum," "Four Sum," or "Two Sum (sorted array)."
5.  **Identify Trade-offs:** When should you use a hash map vs. sorting + two pointers? When is DFS better than BFS, and vice-versa? What are the space/time implications of recursive vs. iterative solutions?
6.  **"Why" Questions:** Why is path compression important in Union-Find? Why does Dijkstra's not work with negative weights?

**Quiz for You:**

Consider the "Merge K Sorted Lists" problem. You have `K` sorted linked lists, and you need to merge them into one sorted linked list.

* **Question 1:** What would be a naive approach to solve this, and what would its time complexity be?
* **Question 2:** How would you use one of the "Non Linear DS" you listed to optimize this problem? Describe the high-level approach and analyze its time and space complexity.
* **Question 3:** What are the trade-offs between your optimized approach and the naive approach, especially concerning `K`?

This level of detailed understanding and critical thinking is what distinguishes a FAANG-level engineer. Let's get to work!
