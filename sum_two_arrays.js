function twoSum(nums, target) {
  // Create a map to store the complements of each number in the array
  const complements = new Map();

  // Loop through each number in the array
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    // Check if the complement of the current number is in the map
    if (complements.has(target - num)) {
      // If so, return the indices of the two numbers
      return [complements.get(target - num), i];
    } else {
      // Otherwise, add the current number and its index to the map
      complements.set(num, i);
    }
  }

  // If no solution is found, return an empty array
  return [];
}
