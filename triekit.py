class Trie:
    class TrieNode:
        # TrieNode is internal.  Feel free to add
        # to the argument list for its init function.
        # add to this init function whatever data members you like
        def __init__(self, char):
            self.children = {}  # a dictionary of char-node pairs
            self.char = char
            self.is_end_of_word = False
            self.counter = 1

    # You cannot alter the prototype of this __init__ function
    # However you can add whatever data members you need
    def __init__(self):
        self.root = self.TrieNode('')
        self.words_with_prefix = []

        # function adds word to the Trie

    def insert(self, word):
        node = self.root

        # iterate through each letter in word
        for char in word:
            # if child contains char, keep looping
            if char in node.children:
                node = node.children[char]

            # once the character is not found
            else:
                # create new node
                new_node = Trie.TrieNode(char)
                node.children[char] = new_node
                # point that character to new_node
                node = new_node

        node.is_end_of_word = True
        node.counter += 1

    def get_prefix(self, node, prefix):
        """returns None, just assigns find_word if it reaches the end of the word"""

        for child in node.children.values():
            if child.is_end_of_word:
                # add the found word in the list of words
                self.words_with_prefix.append(prefix + child.char)

            # keep looking for words with the updated
            self.get_prefix(child, prefix + child.char)

    # function searches for word and its count in the Trie, returns True if found, False otherwise
    def search(self, word):
        node = self.root

        # loop through each char in word
        for char in word:
            if char not in node.children:
                # if not in trie, return False
                return False
            else:
                # assign it to node
                node = node.children[char]

        return node.is_end_of_word

    def begins_with(self, prefix):
        """ returns the list of all words that begin with prefix in the Trie in alphabetical order """
        node = self.root
        self.words_with_prefix = []

        # loop through each letter in prefix
        for letter in prefix:
            if letter not in node.children:
                # empty word list
                return []
            else:
                node = node.children[letter]

        # check if prefix is a word
        if self.search(prefix):
            # add prefix to word_list
            self.words_with_prefix.append(prefix)

        # look for more words that have the prefix
        self.get_prefix(node, prefix)

        # sort the list of words and return it
        return sorted(self.words_with_prefix)

    def get_all(self):
        """ returns the list of all words in the Trie in alphabetical order """
        node = self.root

        return self.begins_with(node.char)
