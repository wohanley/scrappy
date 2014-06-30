import unittest
from mock import MagicMock
import nltk
from scrappy.parse.trees import tree_to_text

class TestTreeToText(unittest.TestCase):

    def test_tree_to_text_tree(self):
        tree = MagicMock(spec=nltk.tree.Tree)
        tree.flatten.return_value = (("This is", "tag"), ("a test", "tag"))
        
        result = tree_to_text(tree)
        
        tree.flatten.assert_called_once()
        self.assertEqual("This is a test", result, "should flatten tree")

    def test_tree_to_text_leaf(self):
        leaf_node = MagicMock()
        leaf_node.__getitem__.return_value = "test value"
        
        result = tree_to_text(leaf_node)
        
        leaf_node.__getitem__.assert_called_once_with(0)
        self.assertEqual("test value", result, "should return text from leaf")


class TestPickTree(unittest.TestCase):
    """
    Tests for the pick_tree function that I'm still not sure is needed.
    """
    
    tree = (
            ("NP", ("My", "PRP"), ("name", "NN")),
            ("is", "VBZ"),
            ("NP", ("Willy", "NNP")),
            (",", ","),
            ("and", "CC"),
            ("NP", ("I", "PRP")),
            ("eat", "VBP"),
            ("NP", ("delicious", "JJ"), ("bagels", "NNS")),
            (".", ".")
        )
    
    def test_pick_tree_empty(self):
        pass
    
    def test_pick_tree_single_tag(self):
        pass
    
    def test_pick_tree_single_tag_missing(self):
        pass
    
    def test_pick_tree_tag_list(self):
        pass
    
    def test_pick_tree_tag_list_missing(self):
        pass
    
    def test_pick_tree_leaf(self):
        pass


if __name__ == "__main__":
    unittest.main()