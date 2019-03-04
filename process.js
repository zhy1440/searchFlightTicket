("use strict");
/*jshint esversion: 6 */
var fs = require("fs");
var _ = require("lodash");
const file_name = "./json/go.json";
const PHP_2_RMB = 7.7;

/**===================================== Get objects from file ==================================**/
const flightList = JSON.parse(fs.readFileSync(file_name));
for (const key in flightList) {
    if (flightList.hasOwnProperty(key)) {
        const flight = _.chain(flightList[key])
            .split("|")
            .filter((e) => e.includes("CNY"))
            .map((s) => s.substring(4).replace(",", ""))
            .min()
            .value();
        console.log(key, flight);
    }
}
// console.log(flightList)

/**========================================= New Object Model ====================================**/

/**========================================= Process objects ====================================**/

/**========================================= Utils Function ====================================**/

function sortFn(a, b) {
    var nameA = a.toUpperCase(); // ignore upper and lowercase
    var nameB = b.toUpperCase(); // ignore upper and lowercase
    if (nameA < nameB) {
        return -1;
    }
    if (nameA > nameB) {
        return 1;
    }
}

// console.log(result);
/**===================================== Save objects as file ==================================**/

// fs.writeFile("./outputData/" + file_name, JSON.stringify(objects, null, 4), "utf8", function(err) {
//     if (err) return console.log(err);
// });
