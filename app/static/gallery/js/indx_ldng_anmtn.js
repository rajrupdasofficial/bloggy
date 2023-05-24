window.addEventListener('DOMContentLoaded', function() {
    var loadingContainer = document.getElementById('loading-container');
    var loadingAnimation = document.getElementById('loading-animation');
    var loadingText = document.getElementById('loading-text');
  
    // Show the loading screen and processing animation
    loadingContainer.style.display = 'flex';
  
    // Set the desired delay time in milliseconds (e.g., 2000 for 2 seconds)
    var delayTime = 2000;
  
    // Delay the loading of content using setTimeout
    setTimeout(function() {
      // Hide the processing animation
      loadingAnimation.style.display = 'none';
  
      // Update the loading text
      loadingText.textContent = 'Processing...';
  
      // Make an AJAX request to load the content of index.html
      var xhr = new XMLHttpRequest();
      xhr.open('GET', 'index.html', true);
      xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
          if (xhr.status === 200) {
            // Display the loaded content
            document.body.innerHTML = xhr.responseText;
  
            // Hide the loading screen
            loadingContainer.style.display = 'none';
          } else {
            // Handle error if the request fails
            console.error('Error loading content:', xhr.status);
  
            // Update the error flag
            var errorOccurred = true;
  
            // Hide the loading screen with error message if error occurred
            if (errorOccurred) {
              loadingText.textContent = 'Error loading content.';
              setTimeout(function() {
                loadingContainer.style.display = 'none';
              }, 2000); // Show the error message for 2 seconds before hiding
            }
          }
        }
      };
  
      xhr.send();
    }, delayTime);
  });
  