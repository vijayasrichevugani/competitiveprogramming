def main(): 
    def hammingDistance(x, y): 
        res = 0 
        for c in str(bin(x ^ y)): 
            if c == '1': 
                res += 1 
        return res 
    print hammingDistance(25, 30) 
    print hammingDistance(1, 4) 
    print hammingDistance(25, 30) 
    print hammingDistance(100, 250) 
    print hammingDistance(1, 30) 
    print hammingDistance(0, 255) 
    
    
if __name__ == '__main__': main()
