# LeetCode Practice - 53. Maximum Subarray


### Tag：`Array`, `Dynamic Programming`, `Divide and Conquer`
### Difficulty: Easy
### Link：https://leetcode.com/problems/maximum-subarray/

<br>

## Description:

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example 1:**
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Example 2:**
```
Input: nums = [-2,-1,-3,-4,-1,-2,-1,-5,-4]
Output: -1
```

**Example 3:**
```
Input: nums = [1]
Output: 1
```

**Example 4:**
```
Input: nums = [5,4,-1,7,8]
Output: 23
```
<br>

## Notes

To solve the problem in O(n), we can use the Kadane's Algorithm.  
For each element walking through, compare it with the ` candidate sum` of the elements before it: if the value of the current element is larger, than update the `candidate sum` as this element itself, otherwise let `candidate sum += value of this element`.  
The largest `candidate sum` will be the maxSum  we look for.

<br>

## My Solution (Java) - Kadane's Algorithm:
```java
public int maxSubArray(int[] nums) {
    if (nums == null || nums.length < 1) return 0;
    
    // Kadane's Algorithm
    int currSum = nums[0];
    int maxSum = currSum;
    for (int i = 1; i < nums.length; i++) {
        currSum = (currSum + nums[i] < nums[i]) ? nums[i] : currSum + nums[i];
        maxSum = (currSum > maxSum) ? currSum : maxSum;
    }
    return maxSum;
}
```

### Follow up: 
If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

## Scratches:
For each small problem divided, there exist three conditions about the position of the `max subarray`:  
- The whole `max subarray` is in the left part of the current array;
- The whole `max subarray` is in the right part of the current array;
- The `max subarray` is crossing the midpoint (spanning from left half to the right half of the array).

FindMaxCrossing:   
starting from the midpoint, moving through to the left -> find the local max; then moving through to the right -> find the local max; make a summation of those two.

<img src="https://github.com/Zhaoyh-Jonathan/LeetCodePractice/blob/main/imgs/lc53_findMaxCrossing.jpg?raw=true" alt="findMaxCrossing JPG">


<br>

## My Solution (Java) - Divide & Conquer:
```java
public int maxSubArray(int[] nums) {        
    return findMaxSubarray(nums, 0, nums.length - 1);
}

// Divide & Conquer Method
private int findMaxSubarray(int[] A, int left, int right) {
    if (left == right) return A[left];
    
    int mid = left + (right - left) / 2;
    int leftMax = findMaxSubarray(A, left, mid);
    int midMax = maxCrossingSubarray(A, left, right, mid);
    int rightMax = findMaxSubarray(A, mid + 1, right);
    
    return Math.max(leftMax, Math.max(midMax, rightMax));
}

private int maxCrossingSubarray(int[] A, int l, int r, int m) {
    // Notice: l is never equal to r here
    // int mid = l + (r - l) / 2;  // no need to calculate again
    int sum = 0;
    int left_part = Integer.MIN_VALUE, right_part = Integer.MIN_VALUE;
    
    for (int i = m; i >= l; i--) {
        sum = sum + A[i];
        if (sum > left_part) left_part = sum;
    }
    sum = 0;
    for (int i = m + 1; i <= r; i++) {
        sum = sum + A[i];
        if (sum > right_part) right_part = sum;
    }
    
    return left_part + right_part;
}
```