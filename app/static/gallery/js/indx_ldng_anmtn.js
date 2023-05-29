window.addEventListener('DOMContentLoaded', function() {
  var loadingContainer = document.getElementById('loading-container');
  var loadingAnimation = document.getElementById('loading-animation');

  // Show the loading screen and processing animation
  loadingContainer.style.display = 'flex';
  loadingAnimation.style.display = 'block';

  // Set the desired delay time in milliseconds (e.g., 2000 for 2 seconds)
  var delayTime = 2000;

  // Delay the loading of content using setTimeout
  setTimeout(function() {
    // Hide the processing animation
    loadingAnimation.style.display = 'none';

    // Hide the loading screen
    loadingContainer.style.display = 'none';

    // Make an AJAX request to load the content of index.html
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'index.html', true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        // Display the loaded content
        document.body.innerHTML = xhr.responseText;
      }
    };
    xhr.send();
  }, delayTime);
});
