import nltk
from itertools import izip
import os
from scrappy.parse.trees import tree_to_text

class ScrapExtracter:
    
    def __init__(self):
        self._iob_tagger = IobTagger()
        
    def extract_scraps(self, text):
        """
        Turns text into a list of scraps. In NLTK parlance, scraps are
        chunks where possible, combined with any tokens that aren't
        part of any chunk, combined with whitespace.
        """
        conll_sentences = [self._sentence_to_conll_string(sentence)
                           for sentence in nltk.sent_tokenize(text)]
        
        return self._collect_scraps(conll_sentences)
    
    def _sentence_to_conll_string(self, sentence):
        tokens = nltk.word_tokenize(sentence) # tokenize sentence
        tagged_tokens = nltk.pos_tag(tokens) # tag parts of speech
        
        tokens = [(token) for (token, pos) in tagged_tokens]
        pos_tags = [(pos) for (token, pos) in tagged_tokens]
        
        pos_iob_tags = self._iob_tagger.tag(pos_tags) # tag IOB chunks
        
        # we need a string in CoNLL format, so a bit of finagling here.
        # A CoNLL string looks like this:
        # Word POS IOB
        # Word POS IOB
        # ...
        fully_tagged = izip(tokens, pos_iob_tags)
        lines = [' '.join([token, pos, iob])
                 for (token, (pos, iob)) in fully_tagged if iob]
        
        return os.linesep.join(lines)
    
    def _collect_scraps(self, conll_sentences):
        
        scraps = []
        
        for conll_sentence in conll_sentences:
        # build chunk parse tree
            tree = nltk.chunk.conllstr2tree('\n'.join(conll_sentences))
            for chunk in tree:
                scraps.append(tree_to_text(chunk))
                
        return scraps
            
    
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

