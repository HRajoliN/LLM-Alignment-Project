// Interactive Chart.js Visualizations

document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('modelPerformanceChart').getContext('2d');
    const modelPerformanceChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['Epoch 1', 'Epoch 2', 'Epoch 3', 'Epoch 4', 'Epoch 5'],
        datasets: [{
          label: 'Training Loss',
          data: [0.8, 0.6, 0.4, 0.3, 0.2],
          borderColor: 'rgba(75, 192, 192, 1)',
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          fill: true,
          tension: 0.4
        }, {
          label: 'Validation Loss',
          data: [0.9, 0.7, 0.5, 0.4, 0.3],
          borderColor: 'rgba(255, 99, 132, 1)',
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          fill: true,
          tension: 0.4
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'top',
          },
          tooltip: {
            mode: 'index',
            intersect: false,
          }
        },
        interaction: {
          mode: 'nearest',
          axis: 'x',
          intersect: false
        },
        scales: {
          x: {
            display: true,
            title: {
              display: true,
              text: 'Epoch'
            }
          },
          y: {
            display: true,
            title: {
              display: true,
              text: 'Loss'
            }
          }
        }
      }
    });
  });
  