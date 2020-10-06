

def get_follow_ratios_dict(pony_dict, canonical_ponies_without_current_pony_keys):
    sum = 0
    for pony in canonical_ponies_without_current_pony_keys:
        sum += pony_dict[pony]
    ratio_dict = {}
    for pony in canonical_ponies_without_current_pony_keys:
        ratio_dict[pony] = round(pony_dict[pony] / sum, 2)
    return ratio_dict

def make_lower(str_list):
    for i in range(len(str_list)):
        str_list[i] = str_list[i].lower()
    return str_list

def get_follow_of(df, pony_name, canonical_ponies_without_current_pony, canonical_ponies_without_current_pony_keys):
    pony_dict = {}
    for i, person in enumerate(canonical_ponies_without_current_pony):
        pony_dict[canonical_ponies_without_current_pony_keys[i]] = 0

    lower_canonical_without_current_pony = make_lower(canonical_ponies_without_current_pony[:-1])
    previous_row = None
    for index, row in df.iterrows():
        if((row['pony'].lower() == pony_name.lower()) and (previous_row is not None)):
            if(previous_row['pony'].lower() == pony_name.lower()):
                pass
            elif(previous_row['pony'].lower() in lower_canonical_without_current_pony):
                if(previous_row["title"] == row["title"]):
                    for i, person in enumerate(lower_canonical_without_current_pony):
                        if(previous_row['pony'].lower() == person.lower()):
                            pony_dict[canonical_ponies_without_current_pony_keys[i]] += 1
                else:
                    pass
            else:
                pony_dict["other"] += 1
        previous_row = row

    return pony_dict

def get_follow_on_comments_dict(df, canonical_ponies, canonical_ponies_keys):
    
    follow_dict = {}
    for i, pony_name in enumerate(canonical_ponies):
        pony_key = canonical_ponies_keys[i]

        canonical_ponies_without_current_pony = canonical_ponies.copy()
        canonical_ponies_without_current_pony.remove(pony_name)
        canonical_ponies_without_current_pony.append("Other")
        canonical_ponies_without_current_pony_keys = canonical_ponies_keys.copy()
        canonical_ponies_without_current_pony_keys.pop(canonical_ponies.index(pony_name))
        canonical_ponies_without_current_pony_keys.append("other")

        pony_dict = get_follow_of(df, pony_name, canonical_ponies_without_current_pony, canonical_ponies_without_current_pony_keys)
        follow_dict[pony_key] = get_follow_ratios_dict(pony_dict, canonical_ponies_without_current_pony_keys)

    return follow_dict
