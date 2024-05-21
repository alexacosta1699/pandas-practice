import sys, datetime
import pandas as pd
from icecream import ic

def createExcelFile(df):
    time_now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    df.to_excel(f"output_{time_now}.xlsx", index=False)
    return None
    
def createDataFrame(data):
    return pd.DataFrame(data=data)

def main():
    d = {'OpNo': [x for x in range(1,101)], 'Seconds': [x for x in range(101,201)]}
    df = createDataFrame(d)
    ic(df)
    createExcelFile(df)
    
    

if __name__ == "__main__":
    main()