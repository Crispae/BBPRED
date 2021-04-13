
#utils.py


__all__ = ["smiles_validator",
           "Disc_validator",
           "DESCRIPTOR_LIST",
            "DataFrame_creator",
            "as_csv",]

from rdkit.Chem import MolFromSmiles
import numbers
import rdkit
import pandas as pd

DESCRIPTOR_LIST = ["topological",
"moreaubroto",
"moran",
"molproperty",
"moe",
"kappa",
"geary",
"constitution",
"connectivity",
"charge",
"cats2d",
"bcut",
"basak",
"scaffolds"
]

def smiles_validator(smiles):
    if isinstance(smiles,numbers.Number):
        raise ValueError("Molecules must be valid SMILES notation not integer.")
        
    if smiles is None or (smiles.strip() == ""):
        raise ValueError("smiles field must not be empty")

    if isinstance(MolFromSmiles(smiles),rdkit.Chem.rdchem.Mol):
        return True
    else:
        raise ValueError("Molecules must be valid SMILE notation of chemical.")


def Disc_validator(descriptor):
    for descript in descriptor:
        if descript.lower() not in DESCRIPTOR_LIST:
            raise ValueError(f" {descript} is not in descriptors list.")
        return True

def DataFrame_creator(args,size,):
    if size == "full":
        pd.options.display.max_rows=None
        pd.options.display.max_columns=None
    data = {}
    for k in args:
        if args.get(k) == None:
            continue
        data.update(**args[k])
    return pd.DataFrame([data])

def path_validator(path):
    if (path == None) or (path.strip() == "") :
        raise ValueError("Path must not be empty")
    return True

def as_csv(dataframe,path):
    if isinstance(dataframe,pd.core.frame.DataFrame) and path_validator(path):
        return dataframe.to_csv(path)
    else:
        raise ValueError("DataFrame object Required")


    


    




