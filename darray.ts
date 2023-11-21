// Ensure data is an array before proceeding
if (!Array.isArray(data)) {
 console.error('Error: data must be an array');
 return;
}

// Iterate through the array and parse each element as an integer
for (let i = 0; i < data.length; i++) {
 if (typeof data[i] === 'string') {
    data[i] = parseInt(data[i], 10);

    // Check if parsing was successful and if the parsed value is a finite number
    if (isNaN(data[i]) || !isFinite(data[i])) {
      console.error(`Error: unable to parse element at index ${i} as an integer`);
      return;
    }
 } else {
    console.error(`Error: element at index ${i} is not a string`);
    return;
 }
}

// Print each element with its index
data.forEach((element, index) => {
 console.log(`index ${index}: ${element}`);
});