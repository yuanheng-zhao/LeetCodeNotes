# LeetCode Practice - 84. Largest Rectangle in Histogram


### Tag：`Stack`, `Dynamic Programming`
### Difficulty: Hard
### Link：https://leetcode.com/problems/largest-rectangle-in-histogram/

<br>

## Description:

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the *area of the largest rectangle in the histogram*.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg" alt="LeetCode example">

Input: heights = [2,1,5,6,2,3]<br>
Output: 10<br>
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg" alt="LeetCode example">

Input: heights = [2,4]<br>
Output: 4

<br>

## Scratches

- Create an extended array `heights_extended = [elements for elements in heights, 0]`.

- Move a pointer *i* from `0` to `heights_extended.length - 1`.

When we want to close the right border of the rectangle and possibly get more area?

- as soon as we process a shorter bar than some bar(s) we have walked through and saved in `stack_heights`: Since the `length of the current bar < some bar(s) passed before`, this is the chance we create a rectangle with the `length of the higher/longer bar(s) * (current index i - index of the higher bar(s))`
- the other sort of possibly larger rectangles we want: flat, shorter than the currently processing bar and walked-through bars but spanning on the x-axis.

<br>

## My Solution:
```java
public int largestRectangleArea(int[] heights) {
    int maxArea = 0;
    Stack<Integer> s_starts = new Stack<Integer>();
    Stack<Integer> s_heights = new Stack<Integer>();
    
    // extend a bar
    int[] heights_extended = new int[heights.length + 1];
    System.arraycopy(heights, 0, heights_extended, 0, heights.length);
    heights_extended[heights.length] = 0;
    
    for (int i = 0; i < heights_extended.length; i++) {
        int lastStartPointer = heights_extended.length + 1;
        while (!s_heights.empty() && s_heights.peek() > heights_extended[i]) {
            lastStartPointer = s_starts.peek();
            int currArea = (i - s_starts.pop()) * s_heights.pop();
            if (currArea > maxArea) maxArea = currArea;
        }
        
        if (s_heights.empty() || s_heights.peek() < heights_extended[i]) {
            s_starts.push(Math.min(i, lastStartPointer)); 
            s_heights.push(heights_extended[i]);
        }
    }
    
    return maxArea;
}
```
