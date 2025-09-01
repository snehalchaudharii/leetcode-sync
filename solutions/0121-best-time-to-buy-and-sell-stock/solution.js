/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxProfit =0;
    let buy= 0, sell=1;

    while(sell < prices.length){
        if(prices[sell] > prices[buy]){
            maxProfit = Math.max(maxProfit, prices[sell]-prices[buy]);
        }
        else{
            buy = sell;
        }
        sell++;
    }

return maxProfit;







    // let profit = 0;
    // let maxProfit = 0;
    // for(let i=0; i< prices.length; i++){
    //     for(let j=i+1; j< prices.length; j++){
    //         profit = prices[j]- prices[i];
    //         if (profit > 0){
    //             maxProfit = Math.max(maxProfit, profit);
    //     }
    //     }
        
    // }
    // return maxProfit;
};
