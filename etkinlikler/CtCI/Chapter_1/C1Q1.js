// Yazılım Mülakatlarına Hazırlık #12 - 2022/05/14

// QUESTION:
// Is Unique: Implement an algorithm to determine if a string has all unique characters.
// What if you cannot use additional data structures?

// TIPS:
// Ask for the character set size

// SOLUTION 1:
// Keep track with a set
// Time: O(n) Space: O(n)
const isUnique = str => {
  const chars = new Set();

  for (let i = 0; i < str.length; i++) {
    if (chars.has(str[i])) {
      return false;
    }
    chars.add(str[i]);
  }

  return true;
};

// SOLUTION 2:
// Sort first
// Time: O(nlogn) Space: O(n)
const isUnique2 = str => {
  str = str.split('').sort().join('');
  for (let i = 1; i < str.length; i++) {
    if (str[i] === str[i - 1]) {
      return false;
    }
  }
  return true;
};

// SOLUTION 3:
// Flag all chars
// Time: O(n) Space: O(c)
// Time / Space O(1) ? because the size is constant
const isUnique3 = str => {
  // If character set is ASCII (128 characters)
  if (str.length > 128) return false;

  const chars = Array(128).fill(false);
  for (let i = 0; i < str.length; i++) {
    let code = str.charCodeAt(i);
    if (chars[code]) {
      return false;
    }
    chars[code] = true;
  }
  return true;
};

// SOLUTION 4:
// Compare all pairs
// Time: O(n^2) Space: O(1)
const isUnique4 = str => {
  for (let first = 0; first < str.length; first++) {
    for (let second = first + 1; second < str.length; second++) {
      if (str[first] === str[second]) {
        return false;
      }
    }
  }
  return true;
};

// TESTING
const tests = [
  ['abcdefghi', true],
  ['jklpoiuqwerzxcvmnsadf', true],
  ['1234567890', true],
  ['AaBbCcDdeFg1234567890(*&^%$#@!)', true],
  ['abcadef', false],
  ['aaaaaaaaaa', false],
  ['abcdefghijklmnopqrstuvwxyza', false],
  ['1234567890asdklf1', false],
  ['!@#$%^&*()(*#($&#(*$&#*($&#()))))', false],
];

tests.forEach(test => {
  let actual = isUnique(test[0]);
  console.log(
    `${actual === test[1] ? 'PASSED' : 'FAILED'} - ${
      test[1] ? 'UNIQUE' : 'NOT UNIQUE'
    } - ${test[0]}`
  );
});
