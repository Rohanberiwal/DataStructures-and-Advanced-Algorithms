# Trie (Prefix Tree) Implementation and Usage in Prefix Search

A Trie, also known as a prefix tree, is a special type of tree used to store associative data structures. A common application of a Trie is storing a predictive text or autocomplete dictionary, but it can be used for various other purposes such as spell checking and matching algorithms.

## Structure

- Each node represents a single character of a word.
- The root node is empty and does not contain any character.
- Each path down the tree may represent a word.
- Nodes can store data or be marked to represent the end of a word.

## Operations

1. **Insertion**: Adding a word to the Trie.
2. **Search**: Checking if a word or prefix exists in the Trie.
3. **Deletion**: Removing a word from the Trie.

## Use in Prefix Search

Tries are particularly effective for prefix search. For example, if you want to find all words in a dictionary that start with a given prefix, you can traverse the Trie starting from the root to the node representing the last character of the prefix, and then list all the words that branch out from this node.

## Example

Here's how you can implement a Trie and use it for prefix search:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage
trie = Trie()
dictionary = ["a", "b", "c"]
for word in dictionary:
    trie.insert(word)

sentence = "aadsfasf absbs bbab cadsfafs"
words = sentence.split(" ")

for i in range(len(words)):
    for j in range(len(words[i])):
        if trie.starts_with(words[i][:j + 1]):
            if trie.search(words[i][:j + 1]):
                words[i] = words[i][:j + 1]
                break

print(" ".join(words))  # Output: "a a b c"
