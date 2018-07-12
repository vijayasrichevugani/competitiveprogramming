import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
public class UniqueMorseCode {
    public static void main(String[] args) {
        ArrayList<String> input = new ArrayList<>();
            
            //Testcase:1
            input.add("gin");
            input.add("msg");
            input.add("gig");
            input.add("zen");
            
            //Testcase:2
            // input.add("a");
            // input.add("z");
            // input.add("g");
            // input.add("m");   
            
            //Testcase:3
            // input.add("a");
            // input.add("b");
            // input.add("c");
            // input.add("d");
            
            //Testcase:4
            // input.add("hig");
            // input.add("sip");
            // input.add("pot");
            
            //Testcase:5
            // input.add("bhi");
            // input.add("vsv");
            // input.add("sgh");
            // input.add("vbi");

        String [] In = new String[input.size()];
        for(int i=0;i<input.size();i++){
            In[i]=input.get(i);
    }
    System.out.println(uniqueMorseCodeRepr(In));
}
public static int uniqueMorseCodeRepr(String[] words) {
         String [] morseCodes = {".-","-...","-.-.","-..",".","..-.","--.","...."
         ,"..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
         "..-","...-",".--","-..-","-.--","--.."}; 
         HashSet<String> set = new HashSet<>();
         for(String x : words){ 
             String result="";
             for(char y : x.toCharArray()){ 
                 result+=morseCodes[y-'a'];
             }
             set.add(result);
         }
         return set.size();   
    }
}
