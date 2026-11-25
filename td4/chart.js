// A working skeleton: read it, run it, then adapt it.
fetch("data/summary.json")                       // 1. ask for the file
  .then(response => response.json())             // 2. read it as JSON
  .then(summary => {                             // 3. use the data
    const labels = summary.history.map(point => point.year);
    const values = summary.history.map(point => point.value);

    // TODO 4B: write the country code in the title of the page

    new Chart(document.getElementById("chart"), {
      type: "line",                              // TODO 4A: change the type
      data: {
        labels: labels,
        datasets: [{ label: "Share of individuals (%)", data: values }]
      }                                          // TODO 4C: add the options after this brace
    });
  });
