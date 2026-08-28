/**
 * @param {number[]} nums
 * @return {number[]}
 */
const resultArray = function (nums) {
    let nums_ori = nums;
    let arr1 = [];
    let arr2 = [];
    let result = [];
    if (nums_ori.length == 1 && nums_ori.length == 2) {
        console.log("len = 1");
        return nums_ori;
    }

    arr1.push(nums_ori[0]);
    arr2.push(nums_ori[1]);

    for (let i = 2; i < nums_ori.length; i++) {
        if (arr1[arr1.length - 1] > arr2[arr2.length - 1]) {
            arr1.push(nums_ori[i]);
        } else {
            arr2.push(nums_ori[i]);
        }
    }

    result = [...arr1, ...arr2];
    // document.getElementById("gg").innerHTML = result;
    return result;
};
