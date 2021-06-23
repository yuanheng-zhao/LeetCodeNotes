# LeetCode Practice - 792. Number of Matching Subsequences


### Tag：`Array`, `HashTable`
### Difficulty: Medium
### Link：https://leetcode.com/problems/number-of-matching-subsequences/

<br>

## Description:

Given a string `s` and an array of strings `words`, return the number of `words[i]` that is a subsequence of `s`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

**Example 1:**
```
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
```

**Example 2:**
```
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
```
<br>

## Scratches

**Note** this problem asks about *subsequence* but not *substring*.

Traverse the array `words`: TLE!  
Instead, we will traverse each character in the string `s`

For Example 1:   
s = "abcde", `Hash{'a': ["a", "acd", "ace"], 'b': ["bb"], 'c':[], 'd':[], ...}`, `ans=0`  
s.charAt(0) = 'a', `Hash{'a': [], 'b': ["bb"], 'c': ["cd", "ce"], 'd': [], ...}`, `ans=1`  
s.charAt(1) = 'b', `Hash{'a': [], 'b': ["b"], 'c': ["cd", "ce"], 'd': [], ...}`, `ans=1`  
s.charAt(2) = 'c', `Hash{'a': [], 'b': ["b"], 'c': [], 'd': ["d"], 'e': ["e"], ...}`, `ans=1`  
s.charAt(3) = 'd', `Hash{'a': [], 'b': ["b"], 'c': [], 'd': [], 'e': ["e"], ...}`, `ans=2`  
s.charAt(4) = 'e', `Hash{'a': [], 'b': ["b"], 'c': [], 'd': [], 'e': [], ...}`, `ans=3`  
Walked throught all characters in s, `final ans = 3`

<br>

## My Solution (Java):
```java
public int numMatchingSubseq(String s, String[] words) {
    int ans = 0;
    
    if (s.length() < 1 || words.length < 1) return ans;
    
    Map<Character, Queue<String>> adjacency = new HashMap<Character, Queue<String>>();
    
    // 26 English letters -> queue
    // each character in each word should be lower-case
    for (int i = 0; i < 26; i++) {
        Queue<String> q = new LinkedList<String>();
        adjacency.put((char) ('a' + i), q); 
    }
    // add words to the adjacency hashtable on their first chars
    for (int i = 0; i < words.length; i++) 
        adjacency.get(words[i].charAt(0)).offer(words[i]);
    
    for (int i = 0; i < s.length(); i++) {            
        Queue<String> currQ = adjacency.get(s.charAt(i));
        // the size of currQ might be changed in the following loop
        int numElements = currQ.size();
        
        for (int j = 0; j < numElements; j++) {
            String word = currQ.poll();
            if (word.length() == 1) {
                ans++;
            } else {
                // add the remaining substring to the queue with the corresponding key (initial of the substring) 
                adjacency.get(word.charAt(1)).offer(word.substring(1));
            }
        }
    }

    return ans;
}
```
