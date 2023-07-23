from pymongo import MongoClient
import pandas as pd
from .methods import insertion_sort

# connecting
cluster = MongoClient("mongodb://localhost:27017")
collection = cluster["quiz_analytics"]["quiz_analytics"]


def get_analytics_dataframes(caption, count):

    # getting data from db
    quiz_results = collection.find({"caption": caption}).sort("result")

    # setting dict structure and idx
    df_dict = {"count": [], "result": []}
    idx = 0

    for r in quiz_results:
        # checking if result array is empty or result is equal to existing result on idx
        if not df_dict["result"] or r["result"] == df_dict["result"][idx]:
            if r["result"] in df_dict["result"]:
                # increasing count
                df_dict["count"][idx] += 1
            else:
                # adding element
                df_dict["result"].append(r["result"])
                df_dict["count"].append(1)
        else:
            # incrementation and adding
            idx += 1
            df_dict["result"].append(r["result"])
            df_dict["count"].append(1)

    # sort by count
    insertion_sort(df_dict)

    # leave certain count of elements
    df_dict["count"] = df_dict["count"][0:count]
    df_dict["result"] = df_dict["result"][0:count]

    return pd.DataFrame(df_dict)


def insert_dict(data):
    collection.insert_one(data)


