import string
def check_mention(dialog, other_pony, start_index):
    index = dialog.find(other_pony, start_index)
    ending_index = index + len(other_pony)
    if(index == -1):
        return False
    elif((index != 0) and (dialog[index - 1] not in string.whitespace) and (dialog[index - 1] not in string.punctuation)):
        return False
    elif((ending_index < len(dialog)) and (dialog[ending_index] not in string.whitespace) and (dialog[ending_index] not in string.punctuation)):
        return False
    else:
        return True

def mentions_name(dialog, other_pony, start_index):
    results = {}
    index = dialog.find(other_pony, start_index)
    ending_index = index + len(other_pony)
    results["ending_index"] = ending_index
    results["mention"] = check_mention(dialog, other_pony, start_index)
    
    return results

def analyze_for_one_word_pony(dialog, other_pony):
    start_index = 0
    last_index = len(dialog)
    more_to_find = True
    count = 0
    while(more_to_find):
        results = mentions_name(dialog, other_pony, start_index)
        start_index = results["ending_index"]
        more_to_find = check_mention(dialog, other_pony, start_index)
        if(results["mention"]):
            count+=1
    return count


def analyze_for_two_word_pony(dialog, other_pony):
    other_pony_names = other_pony.split(" ")
    first_name_count = analyze_for_one_word_pony(dialog, other_pony_names[0])
    second_name_count = analyze_for_one_word_pony(dialog, other_pony_names[1])
    full_name_count = analyze_for_one_word_pony(dialog, other_pony)
    
    count = (first_name_count + second_name_count) - full_name_count
    return count



def analyze_dialog(dialog, other_pony):
    
    two_word_ponies = ["Twilight Sparkle", "Pinkie Pie", "Rainbow Dash"]

    count = 0
    if(other_pony in two_word_ponies):
        count = analyze_for_two_word_pony(dialog, other_pony)
    else:
        count = analyze_for_one_word_pony(dialog, other_pony)

    return count





def get_mentions_of(df, pony_name, canonical_ponies_without_current_pony, canonical_ponies_without_current_pony_keys):
    ponys_mentions = {}

    for other_pony_key in canonical_ponies_without_current_pony_keys:
        ponys_mentions[other_pony_key] = 0
    
    for index, row in df.iterrows():
        if(row['pony'].lower() == pony_name.lower()):
            for j, other_pony in enumerate(canonical_ponies_without_current_pony):
                ponys_mentions[canonical_ponies_without_current_pony_keys[j]] += analyze_dialog(row['dialog'], other_pony)
    return ponys_mentions

def get_ratios_dict(pony_dict, canonical_ponies_without_current_pony_keys):
    sum = 0
    for pony in canonical_ponies_without_current_pony_keys:
        sum += pony_dict[pony]
    
    ratio_dict = {}
    for pony in canonical_ponies_without_current_pony_keys:
        ratio_dict[pony] = round(pony_dict[pony] / sum, 2)
    return ratio_dict


def get_mentions_dict(df, canonical_ponies, canonical_ponies_keys):

    mentions_dict = {}
    # we are going to iterate through each pony and form a dictionary for each
    for i, pony_name in enumerate(canonical_ponies):

        pony_key = canonical_ponies_keys[i]
        canonical_ponies_without_current_pony = canonical_ponies.copy()
        canonical_ponies_without_current_pony.remove(pony_name)
        canonical_ponies_without_current_pony_keys = canonical_ponies_keys.copy()
        canonical_ponies_without_current_pony_keys.pop(canonical_ponies.index(pony_name))

        pony_dict = get_mentions_of(df, pony_name, canonical_ponies_without_current_pony, canonical_ponies_without_current_pony_keys)
        mentions_dict[pony_key] = get_ratios_dict(pony_dict, canonical_ponies_without_current_pony_keys)

    return mentions_dict