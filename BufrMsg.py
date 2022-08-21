from eccodes import *
import numpy as np

class bufrMsg(object):
    def __init__(self, Bid):
        self._bid=Bid 
        self._nsubsets=codes_get(self._bid, "numberOfSubsets")
        codes_set(self._bid, "skipExtraKeyAttributes", 1)
        codes_set(self._bid, "unpack", 1)
            
    @property
    def nsubsets(self):
        return self._nsubsets 
        
    def get_jdata(self, lstKeys):
        jdata={}
        for key in lstKeys:
            jdata[key]=bufrMsg.getdata(self._bid, key,self.nsubsets ).tolist()
        return jdata
        
    def __del__(self):
        codes_release(self._bid)
    
    @staticmethod
    def getdata(bid, key, nexpected=1):
        if nexpected==1:
            data=codes_get(bid, key)
        else:
            data=codes_get_array(bid, key)
            if data.size!=nexpected:
                data=data*np.ones(nexpected)
        return data
            
        
