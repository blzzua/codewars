//# https://www.codewars.com/kata/58981e716551af31b100063f/solutions/javascript

function regularMonths(currMonth) {
  let mmyy = currMonth.split('-');
  let mm = parseInt(mmyy[0]);
  let yy = parseInt(mmyy[1]);
  while (true) {
    let dt = new Date(yy, mm, 1);
    if (dt.getDay() == 1) {
      break;
    }
    mm += 1;
    if (mm >= 12) {
      mm = 0;
      yy += 1;
    }
  }
  return `${String(mm+1).padStart(2, '0')}-${yy}`;
}

