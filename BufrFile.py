from eccodes import *



class bufrFile(object):
    def __init__(self,FileName):
        self._fobj=open(FileName, "rb")
        self._nmsg=codes_count_in_file(self._fobj)
    @property
    def nmsg(self):
        return self._nmsg
    def generate_bids(self):
        for i in range(0, self.nmsg):
            bid=codes_bufr_new_from_file(self._fobj)
            yield bid 
            
    def __del__(self):
        self._fobj.close()

        

