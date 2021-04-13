## data_balancer.py


__all__ = ["OverSampler",
            "UnderSampler",
            "MixSampler",]


from imblearn.over_sampling import (RandomOverSampler,
ADASYN,
KMeansSMOTE,
SMOTE,
BorderlineSMOTE,
SVMSMOTE,
SMOTENC,)
from .utils import *

class Balancer:
    """
    This class implements various methods to balance the
    datasets
      
      # Oversampling
      # Under sampling
      # mix-sampling
    
    
    """
    pass


class OverSampler(Balancer):

    def ROver_sampler(Self,dataset,sampling_strategy="auto",random_state=None):
        X_modified,Y_modified = RandomOverSampler(sampling_strategy=sampling_strategy,random_state=random_state).fit_resample(*Data_split(dataset))
        return X_modified.merge(Y_modified,left_index=True,right_index=True)

    def Adasyn_sampler(self,dataset,sampling_strategy="auto",random_state=None,n_neighbors=5,n_jobs=1):
        X_modified,Y_modified = ADASYN(sampling_strategy=sampling_strategy,random_state=random_state,
        n_jobs=n_jobs).fit_resample(*Data_split(dataset))
        return X_modified.merge(Y_modified,left_index=True,right_index=True)
    
    def Smote_sampler(self,sampling_strategy="auto",random_state=None,m_neighbors=10,kind="regular"):
        X_modified,Y_modified = SMOTE(sampling_strategy=sampling_strategy,random_state=random_state,m_neighbors=m_neighbors,kind=kind)
        return X_modified.merge(Y_modified,left_index=True,right_index=True)




    
class UnderSampler(Balancer):
    pass

class MixSampler(Balancer):
    pass

class Variance_inflation_factor:
    pass
