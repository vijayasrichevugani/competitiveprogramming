    import java.util.Arrays;
    import java.util.*;
    import java.util.Scanner;
       
    public class Anagram {  
        static void CheckAnagram(String str1, String str2) {  
            String s1 = str1.replaceAll("\\s", "");  
            String s2 = str2.replaceAll("\\s", "");  
            boolean status = true;  
            if (s1.length() != s2.length()) {  
                status = false;  
            } else {  
                char[] ArrayS1 = s1.toLowerCase().toCharArray();  
                char[] ArrayS2 = s2.toLowerCase().toCharArray();  
                Arrays.sort(ArrayS1);  
                Arrays.sort(ArrayS2);  
                status = Arrays.equals(ArrayS1, ArrayS2);  
            }  
            if (status) {  
                System.out.println("true");  
            } else {  
                System.out.println("false");  
            }  
        }  
       
        public static void main(String[] args) {  
            CheckAnagram("anagram","nagaram");
            CheckAnagram("Keep", "Peek");  
            CheckAnagram("Mother In Law", "Hitler Woman");  
            CheckAnagram("School Master", "The Classroom ");
            CheckAnagram("ASTRONOMERS","NO MORE STARS ");
            CheckAnagram("Toss","Shot");
            CheckAnagram("joy","enjoy");
            CheckAnagram("Debit Card","Bad Credit");
            CheckAnagram("SiLeNt CAT","LisTen AcT");
            CheckAnagram("Dormitory","Dirty Room");
        }  
    }  
