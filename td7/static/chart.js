// A working skeleton: it draws what the API returns. Adapt it.
let chart = null;

function load() {
  const code = document.getElementById("country").value;
  fetch("/api/data?country=" + encodeURIComponent(code))
    .then(response => response.json())
    .then(rows => {
      // TODO 4B: if the answer is an error, show it in #message and stop
      const labels = rows.map(row => row.year);
      const values = rows.map(row => row.value);
      if (chart) {
        chart.destroy();          // remove the previous chart
      }
      chart = new Chart(document.getElementById("chart"), {
        type: "line",
        data: { labels: labels, datasets: [{ label: code, data: values }] }
      });
    });
}

document.getElementById("load").addEventListener("click", load);
load();
