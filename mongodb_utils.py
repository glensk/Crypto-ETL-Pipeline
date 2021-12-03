import pandas as pd
from pymongo import MongoClient

''' from https://medium.com/analytics-vidhya/how-to-upload-a-pandas-dfframe-to-mongodb-ffa18c0953c1
'''

def connectdb():
    # Connect to MongoDB
    password = "Justd2ss"
    if password == "XXX":
        print('Please specify the password!')
        raise KeyError
    client =  MongoClient("mongodb+srv://albert:"+password+"@cluster0.n8ekn.mongodb.net/myFirstdfbase?retryWrites=true&w=majority")
    db = client['db1']
    collection = db['cn1']
    return collection

def write_db(df):
    collection = connectdb()
    collection.drop() ### the whole db is written 
    df.reset_index(inplace=True)
    df_dict = df.to_dict("records") # Insert collection
    collection.insert_many(df_dict)
    print('written...')
    return

def read_db():
    collection = connectdb()
    df = pd.DataFrame(list(collection.find()))
    df = df.drop(['_id','index'],axis=1)
    return df

def drop_db():
    collection = connectdb()
    collection.drop()
    return

