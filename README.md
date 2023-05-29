## Trie Data Structure

This code defines a Trie data structure, which is a tree-based data structure used for efficient word lookups and implementing autocomplete functionality. The Trie consists of `TrieNode` objects that represent individual characters in the words.

### TrieNode Attributes

The `TrieNode` class has the following attributes:

- `children`: A dictionary that maps characters to their corresponding child `TrieNode`s.
- `char`: The character represented by the `TrieNode`.
- `is_end_of_word`: A Boolean flag indicating whether the `TrieNode` represents the end of a word.
- `counter`: A counter to keep track of the number of times a word has been inserted into the Trie.

### Trie Class Methods

The `Trie` class has the following methods:

- `insert`: Inserts a word into the Trie by iterating through each character and creating new `TrieNode`s as needed.
- `get_prefix`: Recursively finds all words with a given prefix in the Trie and adds them to a list.
- `search`: Searches for a word in the Trie and returns `True` if found, `False` otherwise.
- `begins_with`: Returns a list of all words in the Trie that begin with a given prefix in alphabetical order.
- `get_all`: Returns a list of all words in the Trie in alphabetical order by calling `begins_with` on the root node.

Overall, this code provides the functionality to efficiently build and search words using a Trie data structure.


## Are there other ways to implement this?

A Trie is a tree based data structure which stores each of the characters of the words into nodes with a terminal marker to indicate the completion of a word.
The implementation of trie can also be done by using Sorted array and BST using strings.


- In a sorted array, we need to perform the search operation twice to list the words that begins with a given prefix and a BST has to perform the search for entire subtree that matches a node with prefix. Where as in a trie, we follow the pattern starting from root and retrieve the values that matches the prefix so that all other words in a trie can be ignored. A trie can never miss to insert or search for a word since it follows a pattern.
- It is easier to perform the search operation using a sorted array since the array elements ("strings" in case of implementation of trie) are already sorted in alphabetical order. In such case we can implement a binary search to perform search operations and has the efficient of O(logn), for n number of array elements.
To perform "begins_with" task in sorted array, similar to what a trie can do, we can find the first and last matching prefix elements and print whatever lies in between. Since this also uses binary search to look up for first and last elements, time complexity of begins_with using sorted array is also O(logn).
- If we implement the concept of trie as BST using strings, the values are stored in alphabetical order while insertion and we perform the search operation starting from root node If root is an exact match we return root or else we continue search by comparing if value to be searched is less than or greater than root. Either ways we ignore one half of the subtree and repeat this process recursively until we find the exact match. Since the search here also follows same as a binary search it's complexity is O(logn), for n number of nodes.
"begins_with" in a BST searches for the node with exact match as of prefix and returns the values until it doesn't find any matching prefix. Though it performs the search twice it is as efficient as a binary search.
- Insertion in a trie is performed by checking if there exists matching characters of the word already and adding upon them. If not, we create a new word and add it to the root of trie. Similarly insertion is also done in a BST. We check if the string which needs to be added already exists and compare it with root. If there is no root, add as a root. If not, go down to left or right subtrees and repeat this process recursively until we insert. Insertion occurs at O(logn) complexity. Sorted arrays also follow similar insertion implementation.

