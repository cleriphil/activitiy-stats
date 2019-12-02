
from collections import Counter

# # dummy data
# all_activities = [[a, b, c],[b, d, f],[b, a], [c, d, e],[a, c, e], [c, d, e, f]]

tag_corpus = [['cat', 'fish'], ['cat'], ['fish', 'dog', 'cat']]  

unique_tags = ['dog', 'cat', 'fish'] 
co_occurences = {key:Counter() for key in unique_tags}

def do_thing():
for tags in tag_corpus: 
    tallies = Counter(tags)
    for key in tags: 
        co_occurences[key] = co_occurences[key] + tallies
return co_occurences

# https://stackoverflow.com/questions/36657691/how-to-efficiently-tally-co-occurrences-in-python-list-of-lists

# on command line:
# import main
# https://docs.python.org/2/tutorial/modules.html