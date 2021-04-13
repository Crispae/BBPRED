## utils.py
import pandas as pd
from collections import Counter



__all__ = ["Data_frame_validator","Data_split","label_counter"]

def Data_frame_validator(dataframe):
    if isinstance(dataframe,pd.core.frame.DataFrame) and ("Target" in dataframe.columns) :
        return True
    else:
        raise ValueError(" Correct DataFrame type is not given Dataframe must have 'Target' column")

def label_counter(series):
    if isinstance(series,pd,pandas.core.series.Series):
        return True
    else:
        raise ValueError("Must  be Series type of object.")
def Data_split(Dataframe):
    if Data_frame_validator(Dataframe):
        x,y = Dataframe.drop(["Target"],axis=1),Dataframe["Target"]
        return [x,y]
    i