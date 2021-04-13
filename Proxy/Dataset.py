## Dataset.py


__all__ = ["Proxy",
"Train",
"Predict"]

import pandas as pd
from .utils import *
from .Descriptors import *
from tqdm import tqdm
import logging


class Proxy:
    """
    It will communicate with diffrent object of BBPRED
    
    """
    def __init__(self):
        self.Full_Cached_DataFrame = None
        self.Cached_DataFrame_HASH = None


    def _Data_splitter(self,csv_file):
        if file_validator(csv_file):
            self.Cached_DataFrame_HASH = File_hash_calculator(csv_file)
            df = pd.read_csv(csv_file)
            SMILES = df["SMILES"]
            Target = df["Target"]
        return [SMILES,Target]

    def _Descriptor_calc(self,smiles_target,args=None):
        print(smiles_target)
        SMILES,Target = smiles_validator(*smiles_target)
        if args == None:
            data = []
            for i in tqdm(SMILES):
                dis = Descriptor(i)
                data.append(Data_dict(dis.get_all()))

            return Data_frame(data,Target)
        else:
            single_data = []
            for i in tqdm(SMILES):
                single_data.append(Data_dict(Descriptor(i).get(args)))
            return Data_frame(single_data,Target)



    def get_raw(self,csv_file,):
        SMILES , Target = self._Data_splitter(csv_file) 
        return pd.DataFrame({"SMILES":SMILES,
                            "Target":Target},)


    def get_raw_descriptor(self,csv_file,*args,as_csv=False,path=""):
        if File_hash_calculator(csv_file) == self.Cached_DataFrame_HASH:
            return self.Full_Cached_DataFrame
        else:
            self.Cached_DataFrame_HASH = None
            self.Full_Cached_DataFrame = None
            if len(args) == 0:
                if self.Full_Cached_DataFrame == None:
                    Smiles_data = self._Data_splitter(csv_file)
                    data = self._Descriptor_calc(Smiles_data)
                    self.Full_Cached_DataFrame = data
                    if as_csv:
                        return pd.to_csv(data,path)
                    return data
                else:
                    if as_csv:
                        return pd.to_csv(self.Full_Cached_DataFrame,path)
                    return self.Full_Cached_DataFrame
            if len(args) != 0:
                if self.Full_Cached_DataFrame == None:
                    smiles_data = self._Data_splitter(csv_file)
                    data = self._Descriptor_calc(smiles_data,args)
                    self.Full_Cached_DataFrame = data
                    if as_csv:
                        return pd.to_csv(data,path)
                    return data
                else:
                    if as_csv:
                        return pd.to_csv(self.Full_Cached_DataFrame,path)
                    return self.Full_Cached_DataFrame




    
class Train(Proxy):
    pass
    











class Predict(Proxy):
    pass
