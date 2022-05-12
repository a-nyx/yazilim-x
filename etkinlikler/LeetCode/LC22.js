// Yazılım Mülakatlarına Hazırlık #12 - 2022/05/14
// Generate Parentheses: https://leetcode.com/problems/generate-parentheses/
// YouTube #10: https://youtu.be/jcMVX1_iJHc

// Backtracking
const generateParenthesis = n => {
  let results = [];
  backtrack(n, results, [], 0, 0);
  return results;
};

const backtrack = (n, results, current, open, close) => {
  if (open + close === n * 2) {
    results.push(current.join(''));
    return;
  }

  if (open < n) {
    current[open + close] = '(';
    backtrack(n, results, current, open + 1, close);
  }

  if (close < open) {
    current[open + close] = ')';
    backtrack(n, results, current, open, close + 1);
  }
};

// SAME
const generateParenthesis2 = n => {
  let results = [];
  let current = [];

  const backtrack = (open, close) => {
    if (open + close === n * 2) {
      results.push(current.join(''));
      return;
    }

    if (open < n) {
      current[open + close] = '(';
      backtrack(open + 1, close);
    }

    if (close < open) {
      current[open + close] = ')';
      backtrack(open, close + 1);
    }
  };

  backtrack(0, 0);
  return results;
};

console.log(generateParenthesis(3));
