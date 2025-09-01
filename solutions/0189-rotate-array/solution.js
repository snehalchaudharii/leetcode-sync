/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    n= nums.length;
    k = k % n; // in case: k is graeter than n

    function reverse(arr, start, end){
        while(start< end){
            [arr[start], arr[end]]= [arr[end], arr[start]];
            start++;
            end--;
        }
    }

    reverse(nums, 0, n-1); // reverse entire array
    reverse(nums, 0, k-1); // then reverse first k elements
    reverse(nums, k, n-1); // reverse remaining elements



    // // Time Complexity: O(k × n)
    // // Space Complexity: O(1)
    // while(k > 0){
    //     nums.unshift(nums[n-1]);
    //     nums.pop();
    //     k--;
    // }
    // return nums;
};
