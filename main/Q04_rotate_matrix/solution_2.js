const rotateMatrix = matrix => {
    // Mirror the matrix horizontally
    matrix.reverse();

    // Transpose (Flip diagonally) the matrix
    for (let row = 0; row < matrix.length; row++) {
        for (let col = row + 1; col < matrix.length; col++) {
            [matrix[row][col], matrix[col][row]] = [
                matrix[col][row],
                matrix[row][col]
            ];
        }
    }
};

module.exports = rotateMatrix;
