fs = require('fs');
fs.readFile(
  'Kap1_9_8_JSON_Baum.json',
  'utf8',
  function (err,data) {
    if (err) {
      return console.log(err);
    }
    console.log(data);
    var obj = JSON.parse(data);
    console.log(obj);
  }
);
