class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<HashMap, List> map = new HashMap<>();
        for(String str: strs) {
            HashMap<Character, Integer> freq = new HashMap<>();
            for(int i=0; i<str.length(); i++) {
                if(!freq.containsKey(str.charAt(i)))
                    freq.put(str.charAt(i), 1);
                else
                    freq.put(str.charAt(i), freq.get(str.charAt(i))+1);
            }
            if(!map.containsKey(freq)) {
                List<String> strings = new ArrayList<>();
                strings.add(str);
                map.put(freq, strings);
            }
            else {
                List<String> strings = map.get(freq);
                strings.add(str);
                map.put(freq, strings);
            }
        }
        List<List<String>> res = new ArrayList<>();
        for(Map.Entry<HashMap, List> entry: map.entrySet()) {
            res.add(entry.getValue());
        }
        return res;
        
    }
}
