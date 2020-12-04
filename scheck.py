import FinanceDataReader as fdr
import time
import datetime
from pytz import timezone, utc

KST = timezone('Asia/Seoul')

dfold = ""
while (True):
    now = datetime.datetime.now()
    now = KST.localize(now)
    time.sleep(1)
    #print(str(now))
    df = fdr.DataReader('028300', str(now)[:10])#str(now.tm_year)+"-"+str(now.tm_mon)+"-"+str(now.tm_mday))
    if(str(df) != dfold):
        print("=============================================================")
        print(df)
        dfold = str(df)
