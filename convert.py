from nltk import pos_tag
from nltk.tree import Tree
from nltk.chunk import conlltags2tree


tokens = ['In', 'Beirut', ',', 'a', 'string', 'of', 'officials',
          'voiced', 'their', 'anger', ',', 'while', 'at',
          'the', 'United', 'Nations', 'summit', 'in', 'New', 
          'York', ',', 'Prime', 'Minister', 'Fouad', 'Siniora',
          'said', 'the', 'Lebanese', 'people', 'are', 'resolute',
          'in', 'preventing', 'such', 'attempts', 'from',
          'destroying', 'their', 'spirit', '.']
tags = ['O', 'B-geo', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 
        'O', 'O', 'O', 'O', 'B-org', 'I-org', 'O', 'O', 'B-geo', 
        'I-geo', 'O', 'B-per', 'O', 'B-per', 'I-per', 'O', 'O', 
        'B-gpe', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 
        'O', 'O', 'O']
		
# tag each token with pos
pos_tags = [pos for token, pos in pos_tag(tokens)]
# convert the BIO / IOB tags to tree
conlltags = [(token, pos, tg) for token, pos, tg in zip(tokens, pos_tags, tags)]
ne_tree = conlltags2tree(conlltags)

# parse the tree to get our original text
original_text = []
for subtree in ne_tree:
    # skipping 'O' tags
    if type(subtree) == Tree:
        original_label = subtree.label()
        original_string = " ".join([token for token, pos in subtree.leaves()])
        original_text.append((original_string, original_label))
		
print(original_text)
"""
Output:
[('Beirut', 'geo'),
 ('United Nations', 'org'),
 ('New York', 'geo'),
 ('Prime', 'per'),
 ('Fouad Siniora', 'per'),
 ('Lebanese', 'gpe')]
"""
