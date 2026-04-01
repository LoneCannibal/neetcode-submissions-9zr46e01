class Solution {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder prefix = new StringBuilder("");
        int j=0, min=strs[0].length();
        for(int i=0; i<strs.length; i++)
            if(strs[i].length() < min)
                min = strs[i].length();
        while(prefix.length() != min) {
            for(int i=0; i<strs.length; i++) {
                if(strs[i].charAt(j) != strs[0].charAt(j))
                    return prefix.toString();
                if(i == strs.length -1) {
                    prefix.append(strs[0].charAt(j));
                    j++;
                }
            }
        }
        return prefix.toString();
        
    }
}