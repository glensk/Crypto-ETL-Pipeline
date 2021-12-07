# Crypto ETL Pipeline

An ETL Pipeline for loading (and analyzing) data from glassnode.com / defillama.com. The obtained data is/can be uploaded to a cloud hosted MongoDB backed by a free-tier AWS; Analysis using plotly 


- You can use this notebook (tvl_analysis.ipynb) without the cloud-hosted mongoDB database -without any loss of functionality- by commening out 2 lines in the tvl_analysis.ipynb notebook (In the section Write to & read from MongoDB):
  mu.write_db(dall)
  dall = mu.read_db() # resets dall dataframe
  

requirements: (conda or pip install)
  - pandas
  - numpy
  - plotly
  - pymongo
![picture alt](tvl.png "ToTal Value Locked")
