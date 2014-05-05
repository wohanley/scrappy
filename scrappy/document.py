class Document(object):
    """
    A document backed by a collection of scraps.
    """
    
    @property
    def parse_tree(self):
        return self._parse_tree
    
    @parse_tree.setter
    def parse_tree(self, tree):
        self._parse_tree = tree

    def __init__(self, conll_tree=None):
        self._parse_tree = conll_tree