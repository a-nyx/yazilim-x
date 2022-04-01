const setMatrixZeroes = matrix => {
    const zeroRow = r => {
        for (let c = 0; c < matrix[r].length; c++) {
            matrix[r][c] = 0;
        }
    };

    const zeroCol = c => {
        for (let r = 0; r < matrix.length; r++) {
            matrix[r][c] = 0;
        }
    };

    const rows = new Set();
    const cols = new Set();

    for (let r = 0; r < matrix.length; r++) {
        for (let c = 0; c < matrix[r].length; c++) {
            if (matrix[r][c] === 0) {
                rows.add(r);
                cols.add(c);
            }
        }
    }

    for (let r = 0; r < matrix.length; r++) {
        for (let c = 0; c < matrix[r].length; c++) {
            if (rows.has(r) || cols.has(c)) {
                matrix[r][c] = 0;
            }
        }
    }
};

module.exports = setMatrixZeroes;
