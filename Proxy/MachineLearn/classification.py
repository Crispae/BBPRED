## classification.py

__all__ = ["Lazy",]

from .lazy import LazyClassifier 
from .utils import *
from sklearn.model_selection import train_test_split
import pandas



class Lazy:
    

    def _lazy_split(self,descriptors_data,test_size,random_state):
        if Data_frame_validator(descriptors_data):
            data = descriptors_data.drop("Target",axis=1)
            Target = descriptors_data["Target"]
            X_train, X_test, y_train, y_test = train_test_split(data, Target,test_size=test_size,random_state =random_state,stratify=Target)
            return [X_train,X_test,y_train,y_test]
        
    def _lazy_classifier(self,tests,verbose,ignore_warnings):
        clf = LazyClassifier(verbose=verbose,ignore_warnings=ignore_warnings, custom_metric=None)
        models,predictions = clf.fit(*tests)
        return (models,predictions)


    def lazy_classify(self,descriptors,test_size=0.3,random_state=42,verbose=False,ignore_warnings=True):
        return self._lazy_classifier(self._lazy_split(descriptors,test_size,random_state),verbose=verbose,ignore_warnings=ignore_warnings)

            


class custom:
    pass






class NaiveByes(custom):
#     def Naive_fit(self):
#         def pick_best(X_train, X_test, y_train, y_test,):
#     best = (None, 0)
#     for var_smoothing in range(-7, 1):
#         clf = GaussianNB(var_smoothing=pow(10, var_smoothing))
#         clf.fit(X_train, y_train)
#         y_pred = clf.predict(X_test)
#         accuracy = (y_pred == y_test).sum()
#         if accuracy > best[1]:
#             best = (clf, accuracy)
#     print('best accuracy', best[1] / len(y_test))
#     return best[0]
# model = pick_best(*cl_data1,)


    pass




class Svm(custom):
    pass










