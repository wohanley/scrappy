import nltk
from itertools import izip

class ScrapExtracter:
    
    def __init__(self):
        self._iob_tagger = IobTagger()
        
    def extract_scraps(self, text):
        """
        Turns text into a list of scraps. In NLTK parlance, scraps are
        chunks where possible, combined with any tokens that aren't
        part of any chunk, combined with whitespace.
        """
        tokens = nltk.word_tokenize(text) # step 1: tokenize
        tagged_tokens = nltk.pos_tag(tokens) # step 2: tag parts of speech
        
        tokens = [(token) for (token, pos) in tagged_tokens]
        pos_tags = [(pos) for (token, pos) in tagged_tokens]
        
        pos_iob_tags = self._iob_tagger.tag(pos_tags) # step 3: tag IOB chunks
        
        # we need a string in CoNLL format, so a bit of finagling here
        fully_tagged = izip(tokens, pos_iob_tags)
        lines = [' '.join([token, pos, iob])
                 for (token, (pos, iob)) in fully_tagged if iob]
        
        # step 4: build chunk parse tree
        return nltk.chunk.conllstr2tree('\n'.join(lines))
    
class IobTagger(nltk.tag.SequentialBackoffTagger):
    """
    An IOB chunk tagger trained on Treebank. Unigram/Bigram is most
    efficient according to <http://streamhacker.com/2008/12/29/
    how-to-train-a-nltk-chunker/>.
    """
    
    def __init__(self):
        """
        Train an IOB chunk tagger on the Treebank corpus. This is a
        *chunk tagger*, so a separate chunker is needed for a parse
        tree.
        """
        treebank = nltk.corpus.treebank_chunk.chunked_sents()[:2000]
        train_chunks = self._conll_tag_chunks(treebank)
        u_chunker = nltk.tag.UnigramTagger(train_chunks)
        self._chunker = nltk.tag.BigramTagger(train_chunks, backoff=u_chunker)
        
    def _conll_tag_chunks(self, chunked_sentences):
        tagged_sentences = [nltk.chunk.tree2conlltags(tree)
                            for tree in chunked_sentences]
        return [[(pos, iob) for (token, pos, iob) in chunk_tags]
                for chunk_tags in tagged_sentences]
    
    def tag(self, pos_tags):
        """
        Add IOB tags to the list of part of speech tags passed in. So, from
        (pos) to (pos, iob).
        """
        return self._chunker.tag(pos_tags)
    
def pick_tree(node, pick_tag, found=[]):
    
    if isinstance(node, nltk.tree.Tree):
        for child in node:
            pick_tree(child, pick_tag, found)
    elif node.node == pick_tag:
        found.push(node)

def tree_to_string(tree):
    ' '.join([node[0] for node in tree.flatten()])