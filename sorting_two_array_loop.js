// Define two arrays
let array1 = [3, 1, 4, 2];
let array2 = [5, 6, 7, 8];

// Bubble sort the arrays
for (let i = 0; i < array1.length; i++) {
  for (let j = 0; j < array1.length - 1; j++) {
    if (array1[j] > array1[j + 1]) {
      // Swap elements in array1
      let temp = array1[j];
      array1[j] = array1[j + 1];
      array1[j + 1] = temp;

      // Swap elements in array2
      temp = array2[j];
      array2[j] = array2[j + 1];
      array2[j + 1] = temp;
    }
  }
}

// Print the sorted arrays
console.log("Array 1: " + array1);
console.log("Array 2: " + array2);