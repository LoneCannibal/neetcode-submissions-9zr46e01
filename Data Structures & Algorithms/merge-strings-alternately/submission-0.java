class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder s = new StringBuilder();
        int w1=0, w2=0;
        while(w1<word1.length() || w2<word2.length()) {
            if(w1 == word1.length()) {
                s.append(word2.substring(w2, word2.length()));
                break;
            }
            
            if(w2 == word2.length()) {
                s.append(word1.substring(w1,word1.length()));
                break;
            }
            
            if((w1+w2)%2 ==0) {
                s.append(word1.charAt(w1));
                w1++;
            }
                
            else {
                s.append(word2.charAt(w2));
                w2++;
            }
            
            
        }
        return s.toString();
    }
}