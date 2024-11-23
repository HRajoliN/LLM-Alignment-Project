// UI Enhancements - Adding Animations, Dark Mode Toggle, and Tooltips

document.addEventListener('DOMContentLoaded', function() {
    // Dark Mode Toggle
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const body = document.body;
  
    darkModeToggle.addEventListener('click', () => {
      body.classList.toggle('dark-mode');
      if (body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark');
      } else {
        localStorage.setItem('theme', 'light');
      }
    });
  
    // Persist Dark Mode Setting
    if (localStorage.getItem('theme') === 'dark') {
      body.classList.add('dark-mode');
    }
  
    // Tooltip Initialization
    const tooltips = document.querySelectorAll('.tooltip');
    tooltips.forEach(tooltip => {
      tooltip.addEventListener('mouseover', function() {
        const tooltipText = document.createElement('span');
        tooltipText.className = 'tooltip-text';
        tooltipText.innerText = this.getAttribute('data-tooltip');
        this.appendChild(tooltipText);
      });
      tooltip.addEventListener('mouseout', function() {
        const tooltipText = this.querySelector('.tooltip-text');
        if (tooltipText) this.removeChild(tooltipText);
      });
    });
  
    // GSAP Animations for Elements
    gsap.from('.card', {
      duration: 1,
      y: 50,
      opacity: 0,
      stagger: 0.2,
      ease: 'power2.out'
    });
  });
  