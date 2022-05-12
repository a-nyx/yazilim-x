// Yazılım Mülakatlarına Hazırlık #12 - 2022/05/14
// Contains Duplicate: https://leetcode.com/problems/contains-duplicate/
// SIMILAR TO: CtCI/Chapter_1/C1Q1.js

const containsDuplicate = nums => {
  const seen = new Set();

  for (let i = 0; i < nums.length; i++) {
    if (seen.has(nums[i])) {
      return true;
    }
    seen.add(nums[i]);
  }

  return false;
};
