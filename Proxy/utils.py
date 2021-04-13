## utils.py
import hashlib
import pandas as pd
import os
import rdkit
from rdkit.Chem import MolFromSmiles
__all__ = ["file_validator",
            "Data_dict",
            "Data_frame",
            "File_hash_calculator",
            "smiles_validator"
            ]

def file_validator(path):
    if (path == None) or (path.strip() == ""):
        raise ValueError("Enter path of csv file")
    if os.path.isfile(path):
        return True
    else:
        raise ValueError(f"{path} the specified path doesnot  exist....")

def Data_dict(data,):
    Data = {}
    for k in data:
        if data.get(k) == None:
            continue
        Data.update(**data[k])
    return Data

def Data_frame(data,target):
    descriptor_data = pd.DataFrame(data)
    if descriptor_data.shape[0] == len(target):
        descriptor_data.insert(descriptor_data.shape[1],column="Target",value=target)
    return descriptor_data

def Dir_validator(path):
    pass

def File_hash_calculator(filename):
    if file_validator(filename):
        md5_hash = hashlib.md5()
        with open(filename,"rb") as f:
            # Read and update hash in chunks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                md5_hash.update(byte_block)
            return md5_hash.hexdigest()

def smiles_validator(smiles,target):
    print(smiles)
    new_target = []
    valid_smiles = []
    for _,i in enumerate(smiles):
        try:
            if isinstance(MolFromSmiles(i),rdkit.Chem.rdchem.Mol):
                valid_smiles.insert(_,i)
                new_target.insert(_,target[_])
        except:
            print(smiles)
                
    if len(valid_smiles) == len(new_target):
        return [valid_smiles,new_target]
        




