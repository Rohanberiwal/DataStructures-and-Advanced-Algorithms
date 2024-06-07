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
