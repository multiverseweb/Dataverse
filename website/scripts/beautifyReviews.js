fetch('../scripts/reviews.json')
  .then(response => response.json())
  .then(data => displayReviews(data))
  .catch(error => console.error("Error loading reviews:", error));

function displayReviews(reviews) {
  const reviewsContainer = document.getElementById('reviews-container');
  reviews.forEach(review => {
    // Create review elements
    const reviewDiv = document.createElement('div');
    reviewDiv.classList.add('review');
    
    // Review Header (Name)
    const reviewHeader = document.createElement('div');
    reviewHeader.classList.add('review-header');
    
    const name = document.createElement('h3');
    name.textContent = review.name;  // Name of the reviewer
    reviewHeader.appendChild(name);
    
    reviewDiv.appendChild(reviewHeader);
    
    // Review Content (Message)
    const reviewContent = document.createElement('div');
    reviewContent.classList.add('review-content');
    reviewContent.innerHTML = review.body; // Display the message in HTML
    reviewDiv.appendChild(reviewContent);
    
    // Review Footer (Rating)
    const reviewFooter = document.createElement('div');
    reviewFooter.classList.add('review-footer');
    
    const starRating = document.createElement('div');
    starRating.classList.add('star-rating');
    
    // Extract the rating from "human_fields" (stored as a string)
    const stars = parseInt(review.human_fields['★']);  // Convert the rating string to an integer
    
    // Add the correct number of stars (only filled stars)
    for (let i = 0; i < stars; i++) {
      const star = document.createElement('star');
      star.textContent = '★';  // Filled star symbol
      starRating.appendChild(star);
    }

    reviewFooter.appendChild(starRating);
    
    reviewDiv.appendChild(reviewFooter);
    
    // Append review to container
    reviewsContainer.appendChild(reviewDiv);
  });
}
