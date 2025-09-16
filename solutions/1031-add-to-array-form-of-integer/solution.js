/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function(num, k) {
    let res=[];
    let carry = k;
    let i = num.length-1;

    while(i>= 0 || carry > 0){
        if(i >= 0){
            carry += num[i];
        }
        res.push(carry%10);
        carry = Math.floor(carry / 10);
        i--;
    }
    return res.reverse();
    
};
