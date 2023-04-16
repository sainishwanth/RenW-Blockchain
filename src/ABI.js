const fs = require('fs');
const contract = JSON.parse(fs.readFileSync('/Users/sainishwanth/Documents/HackVerse/truffle_proj/build/contracts/RenW.json', 'utf8'));
console.log(JSON.stringify(contract.abi));