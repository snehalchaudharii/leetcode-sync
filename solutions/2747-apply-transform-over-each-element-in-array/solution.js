/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    for(let i=0; i< arr.length; i++){
        arr[i]= fn(arr[i], i)
    }
    return arr
};


// arr = [1, 2, 3]
// fn = function doublePlusIndex(n, i) {
//     return 2 * n + i;
// }
