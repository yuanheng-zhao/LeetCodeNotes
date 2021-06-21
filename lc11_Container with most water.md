# LeetCode Practice - 11. Container With Most Water


### Tag：`Array`, `Two Pointers`
### Difficulty: Medium
### Link：https://leetcode.com/problems/container-with-most-water/

<br>

## Description:

Given `n` non-negative integers `a1`, `a2`, ..., `an` , where each represents a point at coordinate `(i, ai)`. `n` vertical lines are drawn such that the two endpoints of the line `i` is at `(i, ai)` and `(i, 0)`. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container. 

**Example 1:**

<img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" alt="LeetCode example">
Input: height = [1,8,6,2,5,4,8,3,7]<br>
Output: 49<br>
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

**Example 2:**<br>
Input: height = [1,1]<br>
Output: 1

**Example 3:**<br>
Input: height = [4,3,2,1,4]<br>
Output: 16

<br>

## Scratches
Let two pointers moving toward to each others in opposite directions, which is Similar to pairing two elements in a sorted array with the target sum.

In each loop, always let the shorter "fence" to move 1 unit length, and check the capacity of the newly generated "container".

<br>

## My Solution:
```java
public int maxArea(int[] height) {
    if (height == null || height.length <= 1) return 0;
    
    int l = 0;
    int r = height.length - 1;
    int maxArea = Math.min(height[l], height[r]) * (height.length - 1);
    
    while (l < r) {
        if (height[l] <= height[r]) {
            l++;
        } else {  // height[l] > height[r]
            r--;
        }
        if (Math.min(height[l], height[r]) * (r - l) > maxArea) {
            maxArea = Math.min(height[l], height[r]) * (r - l);
        }
    }
    
    return maxArea;
}
```
