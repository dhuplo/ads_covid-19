import pandas as pd
import numpy as np

from datetime import datetime

def store_relational_JH_data():
    data_path_1 = r"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/" \
                  r"master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    pd_raw = pd.read_csv(data_path_1)
    pd_data_base = pd_raw.rename(columns={"Country/Region": "country", "Province/State": "state"})
    pd_data_base["state"] = pd_data_base["state"].fillna("no")
    pd_data_base = pd_data_base.drop(["Lat", "Long"], axis=1)
    pd_relational_model = pd_data_base.set_index(['state', 'country']) \
        .T \
        .stack(level=[0, 1]) \
        .reset_index() \
        .rename(columns={'level_0': 'date',
                         0: 'confirmed'},
                )
    pd_relational_model["date"] = pd_relational_model.date.astype("datetime64[ns]")
    pd_relational_model.confirmed = pd_relational_model.confirmed.astype(int)
    pd_relational_model.to_csv('../data/processed/COVID_relational_confirmed.csv', sep=';', index=False)
    print("No. of rows stored:" +str(pd_relational_model.shape[0]))
    print("Data Acquired and Stored as COVID_relational_confirmed.csv")



if __name__ == "__main__":
    print("Preparing data for Confirmed Covid Cases and Doubling rate Ploting... ")
    store_relational_JH_data()