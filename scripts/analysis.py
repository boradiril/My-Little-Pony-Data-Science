import argparse
import csv
import pandas as pd
import sys
import json
import os.path as osp

from hw3.verbosity import get_verbosity_dict
from hw3.mentions import get_mentions_dict
from hw3.follow_on_comments import get_follow_on_comments_dict
from hw3.non_dictionary_words import get_non_dict_words_dict

canonical_ponies = ["Twilight Sparkle", "Applejack", "Rarity", "Pinkie Pie", "Rainbow Dash", "Fluttershy"]
canonical_ponies_keys = ["twilight", "applejack", "rarity", "pinkie", "rainbow", "fluttershy"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--json_filename", help="The name of the output file in .json format can be provided with -o flag. (optional)")
    parser.add_argument('file_path', help="The file path to the dataset to be analyzed needs to be provided as an argument.")
    args = parser.parse_args()
    dataset_csv = args.file_path
    
    dataset_file_path = osp.join(osp.dirname(__file__), "..", "data", dataset_csv)
    c = 0
    df_raw = pd.read_csv(dataset_file_path)
    
    df = df_raw[["title", "pony", "dialog"]]


    verbosity_dict = get_verbosity_dict(df, canonical_ponies, canonical_ponies_keys)
    # print(verbosity_dict) 
    #{'twilight': 0.26, 'applejack': 0.15, 'rarity': 0.15, 'pinkie': 0.15, 'rainbow': 0.17, 'fluttershy': 0.12}
    
    mentions_dict = get_mentions_dict(df, canonical_ponies, canonical_ponies_keys)
    # print(mentions_dict)
    # {'twilight': {'applejack': 108, 'rarity': 117, 'pinkie': 212, 'rainbow': 141, 'fluttershy': 121}, 'applejack': {'twilight': 99, 'rarity': 76, 'pinkie': 92, 'rainbow': 64, 'fluttershy': 39}, 'rarity': {'twilight': 82, 'applejack': 95, 'pinkie': 62, 'rainbow': 65, 'fluttershy': 60}, 'pinkie': {'twilight': 119, 'applejack': 58, 'rarity': 55, 'rainbow': 105, 'fluttershy': 55}, 'rainbow': {'twilight': 74, 'applejack': 59, 'rarity': 36, 'pinkie': 100, 'fluttershy': 75}, 'fluttershy': {'twilight': 66, 'applejack': 19, 'rarity': 47, 'pinkie': 29, 'rainbow': 46}}
    # {'twilight': {'applejack': 0.15, 'rarity': 0.17, 'pinkie': 0.3, 'rainbow': 0.2, 'fluttershy': 0.17}, 'applejack': {'twilight': 0.27, 'rarity': 0.21, 'pinkie': 0.25, 'rainbow': 0.17, 'fluttershy': 0.11}, 'rarity': {'twilight': 0.23, 'applejack': 0.26, 'pinkie': 0.17, 'rainbow': 0.18, 'fluttershy': 0.16}, 'pinkie': {'twilight': 0.3, 'applejack': 0.15, 'rarity': 0.14, 'rainbow': 0.27, 'fluttershy': 0.14}, 'rainbow': {'twilight': 0.22, 'applejack': 0.17, 'rarity': 0.1, 'pinkie': 0.29, 'fluttershy': 0.22}, 'fluttershy': {'twilight': 0.32, 'applejack': 0.09, 'rarity': 0.23, 'pinkie': 0.14, 'rainbow': 0.22}}
    
    follow_on_comments_dict = get_follow_on_comments_dict(df, canonical_ponies, canonical_ponies_keys)
    # print(follow_on_comments_dict)
    # {'twilight': {'applejack': 0.09, 'rarity': 0.08, 'pinkie': 0.11, 'rainbow': 0.1, 'fluttershy': 0.08, 'other': 0.53}, 'applejack': {'twilight': 0.15, 'rarity': 0.14, 'pinkie': 0.11, 'rainbow': 0.14, 'fluttershy': 0.08, 'other': 0.39}, 'rarity': {'twilight': 0.13, 'applejack': 0.16, 'pinkie': 0.1, 'rainbow': 0.11, 'fluttershy': 0.1, 'other': 0.4}, 'pinkie': {'twilight': 0.18, 'applejack': 0.12, 'rarity': 0.1, 'rainbow': 0.15, 'fluttershy': 0.07, 'other': 0.39}, 'rainbow': {'twilight': 0.17, 'applejack': 0.12, 'rarity': 0.09, 'pinkie': 0.12, 'fluttershy': 0.1, 'other': 0.4}, 'fluttershy': {'twilight': 0.18, 'applejack': 0.11, 'rarity': 0.14, 'pinkie': 0.09, 'rainbow': 0.15, 'other': 0.34}}

    non_dictionary_words_dict = get_non_dict_words_dict(df, canonical_ponies, canonical_ponies_keys)
    # print(non_dictionary_words_dict)

    results_dict = {}
    results_dict["verbosity"] = verbosity_dict
    results_dict["mentions"] = mentions_dict
    results_dict["follow_on_comments"] = follow_on_comments_dict
    results_dict["non_dictionary_words"] = non_dictionary_words_dict
    
    if(len(sys.argv) >= 3):
        with open(args.json_filename, 'w') as json_file:
            json.dump(results_dict, json_file, indent=2, separators=(',', ': '))
    else:       
        print(json.dumps(results_dict, indent=2, separators=(',', ': ')))

if __name__ == '__main__':
    main()

