from toxic_comment_collection import get_dataset, get_all_datasets, generate_statistics
import pandas as pd

#get_all_datasets(config_path="./src/toxic_comment_collection/config.json", api_config_path='./src/toxic_comment_collection/api_config.json') # skip_download=True
#get_dataset('ousidhoum2019ar')

df = pd.read_csv("./files/combined.tsv", sep="\t")

new_df = df[['text', 'labels', 'file_language', 'file_name']].copy()
new_df = new_df.rename(columns={"labels": "label", "file_language":"language", "file_name":"source"})


#print(df.head())
print(new_df.head())
new_df.to_csv('./formatted.csv', sep='\t', index=False)
generate_statistics('./files')
