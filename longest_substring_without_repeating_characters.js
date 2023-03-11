function lengthOfLongestSubstring(s) {
  let maxLength = 0;
  let start = 0;
  let end = 0;
  let charSet = new Set();

  while (end < s.length) {
    if (!charSet.has(s[end])) {
      charSet.add(s[end]);
      end++;
      maxLength = Math.max(maxLength, end - start);
    } else {
      charSet.delete(s[start]);
      start++;
    }
  }

  return maxLength;
}
