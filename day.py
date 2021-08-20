import datetime

def getDay(yr, mt, dy):
    return datetime.datetime(yr, mt, dy).strftime("%A")

def main():
    print(getDay(2021, 8, 19))
  
if __name__=="__main__":
    main()