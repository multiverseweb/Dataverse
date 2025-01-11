// Function to toggle between light and dark modes
function toggleTheme() {
    var body = document.body;
    body.classList.toggle('dark-theme');
    // Store theme in localStorage so it's persistent
    if (body.classList.contains('dark-theme')) {
        localStorage.setItem('theme', 'dark');
    } else {
        localStorage.setItem('theme', 'light');
    }
}

// On page load, apply the saved theme
window.onload = function() {
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-theme');
    }
}
