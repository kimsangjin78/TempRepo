// from data.js
var tableData = data;

var text = d3.select("#datetime");

// Select the table
var tbody = d3.select("tbody");

function handleChange(event) 
{
  // grab the value of the input field
  var inputText = d3.event.target.value;

  var filteredData = tableData.filter(sighting => sighting.datetime === inputText);

  data.forEach(function(filteredData) 
  {
    var row = tbody.append("tr");
    Object.entries(filteredData).forEach(function([key, value]) 
    {
      console.log(key, value);
      // Append a cell to the row for each value
      // in the weather report object
      var cell = row.append("td");
      cell.text(value);
    });
  });
}

text.on("change", handleChange);