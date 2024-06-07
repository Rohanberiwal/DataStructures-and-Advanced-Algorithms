# Trie (Prefix Tree) Implementation for Prefix Search

## Overview
A Trie, also known as a Prefix Tree, is a tree data structure used for efficient retrieval of strings or words with a given prefix. It allows for quick prefix-based searches and is commonly used in applications like autocomplete, spell checkers, and search engines.

## Implementation Details
1. **Node Structure**: Each node in the Trie contains the following components:
    - `value`: The character stored in the node.
    - `children`: A dictionary (or an array) mapping characters to child nodes.
    - `is_end_of_word`: A boolean flag indicating whether the node represents the end of a word.

2. **Trie Class**: The Trie class contains methods for inserting words into the Trie and searching for words with a given prefix.
    - `insert(word)`: Inserts a word into the Trie.
    - `search(word)`: Searches for a word in the Trie. Returns True if the word exists in the Trie, False otherwise.
    - `starts_with(prefix)`: Searches for words with a given prefix in the Trie. Returns True if any word in the Trie starts with the prefix, False otherwise.

3. **Insertion Operation**: When inserting a word into the Trie, each character of the word is inserted as a node in the Trie. The `is_end_of_word` flag is set to True for the last character of the word.

4. **Search Operation**: To search for a word in the Trie, traverse the Trie starting from the root. For each character in the word, check if there is a corresponding child node. If the traversal reaches the end of the word and the `is_end_of_word` flag is True, the word exists in the Trie.

5. **Prefix Search Operation**: The `starts_with` method is used to search for words with a given prefix. Similar to the search operation, traverse the Trie starting from the root. For each character in the prefix, check if there is a corresponding child node. If the traversal reaches the end of the prefix, there are words in the Trie with that prefix.

## Usage
```python
# Create a Trie object
trie = Trie()

# Insert words into the Trie
trie.insert("apple")
trie.insert("banana")
trie.insert("application")

# Search for words
print(trie.search("banana"))  # Output: True
print(trie.search("appl"))    # Output: False

# Search for words with a prefix
print(trie.starts_with("app"))  # Output: True
print(trie.starts_with("ban"))  # Output: True
print(trie.starts_with("or"))   # Output: False
