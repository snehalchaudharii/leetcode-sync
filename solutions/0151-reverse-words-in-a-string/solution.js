/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    // (O(n) time, O(n) space)
    // let sSplit=s.trim().split(/\s+/);
    // return sSplit.reverse().join(" ");

    let words= s.split(' ');
    let result=[];
    for(let i= words.length-1; i>=0; i--){
        if(words[i]){
            result.push(words[i]);
        }
    }
    return result.join(" ");
};
