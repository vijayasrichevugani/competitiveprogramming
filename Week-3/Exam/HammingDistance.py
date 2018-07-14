def main(): 
    def hammingDistance(x, y): 
        result = 0 
        for i in str(bin(x ^ y)): 
            if i == '1': 
                result += 1 
        return result 
    print hammingDistance(25, 30) 
    print hammingDistance(1, 4) 
    print hammingDistance(25, 30) 
    print hammingDistance(100, 250) 
    print hammingDistance(1, 30) 
    print hammingDistance(0, 255) 
    
    
if __name__ == '__main__': main()
