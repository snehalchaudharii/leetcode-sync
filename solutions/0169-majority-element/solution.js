/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let candidate = 0;
    let count= 0
    for(let num of nums){
        if (count === 0){
            candidate = num;
        }
        count += (num === candidate) ? 1 : -1;
    }
    return candidate





    // let n = nums.length;

    // for(let i = 0 ; i< n; i++){
    //     let count=0;
    //     for(let j=0; j< n; j++){
    //         if(nums[i]===nums[j]){
    //             count++;
    //         }
    //     }

    //     if(count > Math.floor(n/2)){
    //         return nums[i];
    // }
    // }

    
    
};
