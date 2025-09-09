/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left=0;
    let right= height.length-1;
    let maxArea =0;

    while (left < right){
        let ht = Math.min(height[right], height[left]);
        let width = (right -left);
        let area = ht * width;
        maxArea = Math.max(maxArea, area);
        if (height[left] < height[right]){
            left++;
        }else{
            right--;
        }

    }
    return maxArea;
};
