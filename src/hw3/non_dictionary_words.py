import os.path as osp
import re
script_dir = osp.dirname(__file__)


def find_non_words(dialog, words_set):
    non_words = []
    
    pattern_unicode = re.compile('<U\+.*>')          
    dialog = re.sub(pattern_unicode, ' ', dialog)    
    split_dialog = re.split(r'\W+', dialog)
    while("" in split_dialog): 
        split_dialog.remove("") 
    
    for word in split_dialog:
        if word.lower() not in words_set:
            non_words.append(word)
    return non_words

def find_top_non_words(all_non_words_list):
    frequency = {}
    for word in all_non_words_list:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    top_words = sorted(frequency, key = frequency.get, reverse = True)
    return top_words[:5]
    
def find_non_words_in_df(df, pony_name, words_set):
    all_non_words_list = []
    for index, row in df.iterrows():
        if(row['pony'].lower() == pony_name.lower()):
            all_non_words_list.extend(find_non_words(row['dialog'], words_set))
    
    top_five_non_words = find_top_non_words(all_non_words_list)
    return top_five_non_words


def get_non_dict_words_dict(df, canonical_ponies, canonical_ponies_keys):
    non_words_dict = {}

    words_file = osp.join(script_dir,'..','..','data','words_alpha.txt')
    words_set = set(line.strip() for line in open(words_file))

    for i, pony_name in enumerate(canonical_ponies):
        pony_key = canonical_ponies_keys[i]
        non_words_dict[pony_key] = find_non_words_in_df(df, pony_name, words_set)        

    return non_words_dict