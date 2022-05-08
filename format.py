from toxic_comment_collection import get_dataset, get_all_datasets, generate_statistics

get_all_datasets(config_path="./src/toxic_comment_collection/config.json", skip_download=True, api_config_path='./src/toxic_comment_collection/api_config.json')
#get_dataset('ousidhoum2019ar')
import pandas as pd
df = pd.read_csv("./files/combined.tsv", sep="\t")
new_df = df[['text', 'labels', 'file_language', 'file_name']].copy()
new_df = new_df.rename(columns={"labels": "label", "file_language":"language", "file_name":"source"})


print(new_df.head())
new_df.to_csv('./files/formatted.csv', sep='\t', index=False)
generate_statistics('./files')
