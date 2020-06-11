const riverSizes = input => {
  let results = [];
  input.forEach((row, y) => {
    row.forEach((cell, x) => {
      if (input[y][x] === 1) {
        results.push(checkAdjacent(x, y, input));
      }
    });
  });
  return results;
};