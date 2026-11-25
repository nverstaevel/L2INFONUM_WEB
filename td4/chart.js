// A working skeleton: read it, run it, then adapt it.
fetch("data/summary.json")
  .then(response => response.json())
  .then(summary => {
    const labels = summary.history.map(point => point.year);
    const values = summary.history.map(point => point.value);

    new Chart(document.getElementById("chart"), {
      type: "line",                         // TODO: try "bar"
      data: {
        labels: labels,
        datasets: [{ label: "Share of individuals (%)", data: values }]
      }
    });
  });
// TODO: put the country code in the title with
// document.getElementById("title").textContent = ...
