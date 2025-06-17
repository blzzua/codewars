// https://www.codewars.com/kata/56e2ede2c92c6cb1370012ba

function snake(cols,rows){
const A = Array.from({ length: rows }, () => Array(cols).fill('■'));
  for (let iy = 0; iy < rows; iy++) {
      for (let ix = 0; ix < cols; ix++) {
          if ((iy + ix) % 2 === 1) {
              A[iy][ix] = '□';
          }
      }

      if ((iy - 2) % 8 === 0 || (iy - 2) % 8 === 1) {
          for (let ix = 0; ix < cols - 2; ix++) {
              A[iy][ix] = '∷';
          }
      }

      if ((iy - 6) % 8 === 0 || (iy - 6) % 8 === 1) {
          for (let ix = 2; ix < cols; ix++) {
              A[iy][ix] = '∷';
          }
      }
  };
  return A.map(row => row.join('')).join('\n');
}

/* translated from python
import numpy as np
def snake(cols,rows):
  A = np.ndarray( (rows, cols), dtype=object);
  A[:] = '■'
  for iy, ix in np.ndindex(A.shape):
      if (iy + ix) % 2 == 1: A[iy, ix] = '□'
      if (iy - 2) % 8 in (0, 1):
          A[iy, :-2] = '∷'
      if (iy - 6) % 8 in (0, 1):
          A[iy, 2:] = '∷'
  return '\n'.join([''.join(c for c in line ) for line in A])
*/

