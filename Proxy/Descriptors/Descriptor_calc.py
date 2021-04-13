## Descriptor_calc.py


__all__ = ["Descriptor",]



from PyBioMed.PyMolecule import (
moreaubroto,
moran,
moe,
ghosecrippen,
geary,
fingerprint,
estate,
connectivity,
charge,
cats2d,
bcut,
Scaffolds
)
# Descriptor_calc.py

from rdkit.Chem import MolFromSmiles
import rdkit
import numbers
from .utils import *
from . import molproperty,constitution,kappa,basak,topology



class Descriptor:
    
    
    def __init__(self,smiles):
        if smiles_validator(smiles):
            self._smiles = smiles
            self._molecule = MolFromSmiles(self._smiles)
        self._topological = None
        self._moreaubroto = None
        self._moran = None
        self._molproperty = None
        self._moe = None
        self._kappa = None
        self._ghosecrippen = None
        self._geary = None
        self._fingerprint = None
        self._estate = None
        self._constitution = None
        self._connectivity = None
        self._charge = None
        self._cats2d = None
        self._bcut = None
        self._basak = None
        self._scaffolds = None
        


    
    @property
    def smiles(self):
        return self._smiles

    @smiles.setter
    def smiles(self,value):
        self.__init__(value)

    @property
    def topological(self):
        if self._topological is None:
            self._calculate_descriptor()
        return self._topological
    @property
    def moran(self):
        if self._moran is None:
            self._calculate_descriptor()
        return self._moran
    
    @property
    def molproperty(self):
        if self._molproperty is None:
            self._calculate_descriptor()
        return self._molproperty
    
    @property
    def moe(self):
        if self._moe is None:
            self._calculate_descriptor()
        return self._moe
    
    @property
    def moreaubroto(self):
        if self._moreaubroto is None:
            self._calculate_descriptor()
        return self._moreaubroto
    
    @property
    def kappa(self):
        if self._kappa is None:
            self._calculate_descriptor()
        return self._kappa
    
    @property
    def ghosecrippen(self):
        if self._ghosecrippen is None:
            self._calculate_descriptor()
        return self._ghosecrippen
    @property
    def geary(self):
        if self._geary is None:
            self._calculate_descriptor()
        return self._geary
    
    @property
    def fingerprint(self):
        if self._fingerprint is None:
            self._calculate_descriptor()
        return self._fingerprint
    
    @property
    def estate(self):
        if self._estate is None:
            self._calculate_descriptor()
        return self._estate

    @property
    def constitution(self):
        if self._constitution is None:
            self._calculate_descriptor()
        return self._constitution

    @property
    def connectivity(self):
        if self._connectivity is None:
            self._calculate_descriptor()
        return self._connectivity
    
    @property
    def charge(self):
        if self._charge is None:
            self._calculate_descriptor()
        return self._charge

    @property
    def cats2d(self):
        if self._cats2d is None:
            self._calculate_descriptor()
        return self._cats2d

    @property
    def bcut(self):
        if self._bcut is None:
            self._calculate_descriptor()
        return self._bcut

    @property
    def basak(self):
        if self._bcut is None:
            self._calculate_descriptor()
        return self._basak

    @property
    def scaffolds(self):
        if self._bcut is None:
            self._calculate_descriptor()
        return self._scaffolds
    @property
    def list_descriptors(self):
        return (*DESCRIPTOR_LIST,)
    

    def get(self,args,*,as_dataframe=False,as_Csv=False,path="",size=None):
        if self._topological is None:
            self._calculate_descriptor()
        disc= {}
        for arg in args:
            disc.setdefault(arg,self.__dict__[f"_{arg}"])
        if as_dataframe:
            return DataFrame_creator(disc,size)
        if as_Csv:
            return as_csv((DataFrame_creator(disc),size),path)
        return disc
            

    def _kappaCalculator(self):
        return kappa.GetKappa(self._molecule)

    
    def _basakDescriptor(self):
        return basak.Getbasak(self._molecule)

    def _calculate_descriptor(self):
        self._topological = topology.GetTopology(self._molecule)
        self._moreaubroto = moreaubroto.GetMoreauBrotoAuto(self._molecule)
        self._moran = moran.GetMoranAuto(self._molecule)
        self._molproperty = molproperty.GetMolecularProperty(self._molecule)
        self._moe = moe.GetMOE(self._molecule)
        self._kappa =  self._kappaCalculator()
        self._geary = geary.GetGearyAuto(self._molecule)
        self._constitution = constitution.GetConstitutional(self._molecule)
        self._connectivity = connectivity.GetConnectivity(self._molecule)
        self._charge = charge.GetCharge(self._molecule)
        self._cats2d = cats2d.CATS2D(self._molecule)
        self._bcut = bcut.GetBurden(self._molecule)
        self._basak = self._basakDescriptor()


    
    def get_all(self,*,as_dataframe=False,as_Csv=False,path="",size=None):
        if as_dataframe:
            return DataFrame_creator(self.get(DESCRIPTOR_LIST),size=size)
        if as_Csv:
            return as_csv(DataFrame_creator(self.get(DESCRIPTOR_LIST),size),path)
            
        return self.get(DESCRIPTOR_LIST)


    def __repr__(self):
         return (f"Descriptor(smiles='{self.smiles}')[RdkitMolecule:'{self._molecule}']")

    def __len__(self):
        if self._topological is None:
             return 0
        else:
            return len(DESCRIPTOR_LIST) 
