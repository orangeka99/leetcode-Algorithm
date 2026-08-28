var reverse = function (x) {
  let str_x = String(x);
  let opr = "";
  if (str_x[0] == "-") {
    opr = str_x[0];
    str_x = str_x.slice(1);
  }
  const isInt32 = (val) => Number.isInteger(val) && (val | 0) === val;

  //   str_x = str_x.replaceAll("0", "");
  let digits = Array.from(str_x, Number);
  let digits_order = [];
  let post = str_x.indexOf("0");
  let str_tmp = [];
  let str_g = "";

  if (post != -1) {
    for (let i = 0; i < digits.length; i++) {
      if (i == 0) {
        digits_order.push(digits[i]);
      } else {
        if (digits[i] == 0) {
          //   str_tmp[1] = 0;
          str_tmp.push(0);
        } else {
          if (str_tmp[0] == 0) {
            // str_tmp[str_tmp.length - 1] = 9;
            digits_order = [...digits_order, ...str_tmp];
            str_tmp = [];
          }
          digits_order.push(digits[i]);
        }
      }
    }

    digits = digits_order;
    console.log(digits);
  }
  digits = digits.reverse();
  if (opr != "") {
    digits[0] = digits[0] * -1;
  }
  let singleNumber = Number(digits.join(""));
  if (isInt32(singleNumber) == false) {
    console.log(0);
    return 0;
  }
  return singleNumber
  console.log(singleNumber);
};