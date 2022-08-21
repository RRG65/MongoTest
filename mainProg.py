from BufrFile import bufrFile
from BufrMsg import bufrMsg
from pymongo import  MongoClient
import sys 
import time 

def main():
    fname=sys.argv[1]
    start=time.time()
    client=MongoClient()
    db=client.bufrdb
    bcollection=db.ozone
    bfo=bufrFile(fname)
    print(f" nmsg {bfo.nmsg}")
    for bid in bfo.generate_bids():
        bmo=bufrMsg(bid)
        print(f"\t nsubsets {bmo.nsubsets}")
        jd=bmo.get_jdata(["latitude","longitude", "year", "month", "day", "hour", "minute", "second", "#1#integratedOzoneDensity",
        "#1#integratedOzoneDensity->firstOrderStatisticalValue" ])
        bcollection.insert_one(jd)
      
        
    end=time.time()
    print(f" elapsed {end-start:.2f}")
    
if  __name__=="__main__":
    main()
