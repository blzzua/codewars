// https://www.codewars.com/kata/59aac10dd0a5ff951100002a

function arraysEqual(arr1, arr2) {
    if (arr1.length !== arr2.length) {
        return false;
    }
    for (let i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) {
            return false;
        }
    }
    return true;
}


function findIndexOfSubArray(a) {
    if (a.length <= 1) {
        return [0, 0];
    }
    const sa_asc = a.slice().sort((x, y) => x - y);
    const sa_desc = a.slice().sort((x, y) => y - x);
    if (arraysEqual(a, sa_asc) || arraysEqual(a, sa_desc)) {
        return [0, 0];
    }
    const res1 = [];
    const res2 = [];

    for (let i = 0; i < a.length; i++) {
        if (a[i] !== sa_asc[i]) {
            res1.push(i);
        }
        if (a[i] !== sa_desc[i]) {
            res2.push(i);
        }
    }

    const len1 = res1.length;
    const len2 = res2.length;

    if (len1 < len2) {
        return [res1[0], res1[len1 - 1]];
    } else if (len1 > len2) {
        return [res2[0], res2[len2 - 1]];
    } else { // len1 === len2 
        const end1 = res1[len1 - 1];
        const end2 = res2[len2 - 1];

        if (end1 <= end2) {
            return [res1[0], end1];
        } else {
            return [res2[0], end2];
        }
    }
}
