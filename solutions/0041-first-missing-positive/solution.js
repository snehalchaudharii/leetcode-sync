/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    n= nums.length;

    const swap = (arr, i, j) =>{
        [arr[i], arr[j]]= [arr[j], arr[i]];
    }

    for(let i=0; i< n; i++){
        while( nums[i]> 0 && nums[i]<= n && nums[i] != nums[nums[i]-1]){
            swap(nums, i, nums[i]-1);
        }
    }

    for(let i=0; i< n; i++){
        if(nums[i] !== i+1){
            return i+1;
        }
    }
    return n+1;



//    let n= nums.length;
//     for(i= 1; i<= n+1 ; i++){
//         if (!nums.includes(i)){
//             return i;
//         }
//     }


};
