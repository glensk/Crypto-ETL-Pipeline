# swissblock
crypto tvl - marketcat - price analysis


git clone https://github.com/glensk/swissblock.git

cd swissblock

open the tvl_analysis.ipynb notebook

- You can use this notebook without the cloud-hosted mongoDB database -without any loss of functionality- by commening out 2 lines in the tvl_analysis.ipynb notebook (In the section Write to & read from MongoDB):
  mu.write_db(dall)
  dall = mu.read_db() # resets dall dataframe
  

requirements: (conda or pip install)
  - pandas
  - numpy
  - plotly
  - pymongo
