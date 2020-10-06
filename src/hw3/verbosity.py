import pandas as pd

def get_verbosity_dict(df, canonical_ponies, canonical_ponies_keys):
    
    pony_speech_count = {}
    for i, canonical in enumerate(canonical_ponies):
        pony_key = canonical_ponies_keys[i]
        pony_speech_count[pony_key] = 0
        
        previous_row = None
        previous_row_spoken_index = -1
        for index, row in df.iterrows():
            if(row['pony'].lower() == canonical.lower()):
                if(previous_row is None):
                    pony_speech_count[pony_key]+=1
                    previous_row_spoken_index = index
                elif(previous_row_spoken_index == (index - 1)):
                    if(previous_row["title"] != row["title"]):
                        # adding consecutive talking if in different espisodes
                        pony_speech_count[pony_key]+=1
                        previous_row_spoken_index = index
                else:
                    pony_speech_count[pony_key]+=1
                    previous_row_spoken_index = index

            previous_row = row

    
        
    total_speech_count = 0
    for pony_key in pony_speech_count:
        total_speech_count += pony_speech_count[pony_key]
    

    pony_verbosity = {}
    for pony_key in pony_speech_count:
        pony_verbosity[pony_key] = round(pony_speech_count[pony_key] / total_speech_count, 2)

    return pony_verbosity
