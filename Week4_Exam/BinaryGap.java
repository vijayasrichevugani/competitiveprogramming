public class BinaryGap {
    public static int BinaryGap(int N) {
        int maxGap = 0;
        int currentGap = 0;
        boolean oneFound = false;
        
        while (N > 0) {
          if (N % 2 == 1) {
            oneFound = true;
            maxGap = Math.max(currentGap, maxGap);
            currentGap = 0;
          } else if (oneFound) {
            currentGap++;
          }
          
          N /= 2;
        }
        
        return maxGap;
    }

    public static void main(String[] args){
        System.out.println(BinaryGap(0));
        System.out.println(BinaryGap(55));
        System.out.println(BinaryGap(-5));
        System.out.println(BinaryGap(12354));
        System.out.println(BinaryGap(6));
        System.out.println(BinaryGap(256));
    }
}
