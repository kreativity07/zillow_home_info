// Bar Chart
var trace1 = {
  x: ["valuation_range_high", "valuation_range_low", "last_sold_price", "zestimate"],
  y: [299209, 270713, 215000, 284961],
  type: "bar"
};

var data = [trace1];

var layout = {
  title: "Zillow Home Bar Chart",
xaxis: { title: "Home Value"},
yaxis: { title: "Price Range"}
};

Plotly.newPlot("plot", data, layout);


// // Pie Chart
// var trace1 = {
//   labels: ["valuation_range_high", "valuation_range_low", "last_sold_price", "zestimate"],
//   values: [299209, 270713, 215000, 284961],
//   type: "pie"
// };

// var data = [trace1];

// var layout = {
//   title: "Zillow Home Pie Chart",
// labels: { title: "Home Value"},
// values: { title: "Price Range"}
// };

// Plotly.newPlot("plot", data, layout);

