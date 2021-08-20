def getPrimeNumbers(arr):
    result = []
    for a in arr:
        if isPrimeNumber(a):
            result.append(a)
    
    print(result)

def isPrimeNumber(a):
    for x in range(2, (a/2 + 1)):
        if a%x == 0:
            return False
    
    return True

def main():
    getPrimeNumbers([2,3,4,5,6,7,8,9,10])
  
if __name__=="__main__":
    main()