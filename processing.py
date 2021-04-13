from Proxy import Descriptor
from sys import path
import pandas as pd
import numpy as np
import pickle


class Predictor:
    """
    Predictor clas: make predcition of unkown molecule
    
    """

    def __init__(self):
        ## loading model and transformer
        self.transformer_ = self.transformer_loader()
        self.predictor_ = self.model_loader()
        self._all_prop = None


    def model_loader(self):
        """
        method to load trained model
        
        """
        try:
            with open("./models/Extree.pkl","rb") as model:
                predictor_ = pickle.load(model)
        except:
            raise ValueError("Problem loading model..")
        return predictor_
        
    def smiles(self,data):
        """"
        extract all features from the smiles of chemical

        """
        try:
            des = Descriptor(data)
            self._all_prop =  des.get_all(as_dataframe=True)
            return self._all_prop
        except ValueError:
            raise ValueError("smiles conversion Error")

    def molecular_prop(self):






    def data_cleaner(self,data):
        """
        clean dataset from null values and other
        
        """
        assert isinstance(data, pd.DataFrame), "df needs to be a pd.DataFrame"
        data.dropna(inplace=True)
        indices_to_keep = ~data.isin([np.nan, np.inf, -np.inf]).any(1)
        return data[indices_to_keep].astype(np.float64)

    def transformer_loader(self):
        """
        Trained model of transformer is loaded.
        
        """
        try:
            with open("./models/transformer1.pkl","rb") as model:
                transformer = pickle.load(model)
        except:
            raise ValueError("Problem loading Transformer..")
        return transformer

    def transform_data(self,data):

        """
        transform data according to their variance
        
        """
        if isinstance(data,pd.DataFrame):

            try:
                self.transformer_.transform(data)
                return data[data.columns[self.transformer_.get_support(indices=True)]]
            except:
                raise ValueError("data transformation error...")
        else:
            raise ValueError("Data Error...")
        
    def test_data(self,smiles_):
        try:
            descriptors = self.smiles(smiles_)
            cleaned_transformed = self.transform_data(self.data_cleaner(descriptors))
        except:
            raise ValueError(" Error occured.")
        return cleaned_transformed

    def final_predict(self,data):
        result = self.predictor_.predict(data)
        return result




