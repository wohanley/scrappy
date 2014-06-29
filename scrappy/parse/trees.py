import nltk
import functools

def tree_leaf_decide(node, tree_action, leaf_action):
    """
    Take action on a node in a parse tree based on whether it is a leaf
    or a subtree.
    """
    if isinstance(node, nltk.tree.Tree):
        return tree_action()
    else:
        return leaf_action()

def tree_to_text(node):
    """
    Convert an NLTK parse tree to the text it represents.
    """
    tree_action = lambda: ' '.join([subtree[0] for subtree in node.flatten()])
    leaf_action = lambda: node[0]
    return tree_leaf_decide(node, tree_action, leaf_action)

def pick_tree(node, pick_tag):
    """
    Search through a parse tree from the given node down, searching for
    nodes tagged with pick_tag. I'm not sure this function is actually
    going to be needed for anything - my original thought was that it
    would be needed to find chunks, but that isn't actually hard. Do
    not use this yet, it isn't properly tested.
    """
    found = []
    _pick_tree_recurse(node, pick_tag, found)
    return found
    
def _pick_tree_recurse(node, pick_tag, found):
    tree_action = functools.partial(_pick_tree, node, pick_tag, found)
    leaf_action = functools.partial(_pick_leaf, node, pick_tag, found)
    tree_leaf_decide(node, tree_action, leaf_action)
        
def _pick_tree(node, pick_tag, found):
    for child in node:
            pick_tree(child, pick_tag, found)

def _pick_leaf(node, pick_tag, found):
    if node.node == pick_tag:
        found.push(node)