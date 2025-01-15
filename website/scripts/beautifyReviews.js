fetch('reviews.json')
    .then(response => response.json())
    .then(data => {
        const averageRating = calculateAverageRating(data);
        displayAverageRating(averageRating);
        displayReviews(data);
    })
    .catch(error => console.error("Error loading reviews:", error));

// Function to calculate the average rating
function calculateAverageRating(reviews) {
    let totalRating = 0;
    reviews.forEach(review => {
        const rating = parseFloat(review.human_fields['★']); // Get rating from human_fields
        totalRating += rating;
    });
    const average = totalRating / reviews.length;
    return average;
}

// Function to display the average rating at the top
function displayAverageRating(average) {
    const averageRatingContainer = document.getElementById('average-rating');

    // Create an element to show the average rating
    const ratingText = document.createElement('div');
    ratingText.classList.add('average-rating-text');
    ratingText.textContent = `Average Rating: ${average.toFixed(1)} / 5`;  // Show rounded average

    const starRating = document.createElement('div');
    starRating.classList.add('average-star-rating');

    // Calculate the number of full and half stars
    const fullStars = Math.floor(average);  // Full stars (rounded down)
    const hasHalfStar = (average % 1) >= 0.5;  // Check if half star is needed

    // Add the correct number of full stars
    for (let i = 0; i < fullStars; i++) {
        const star = document.createElement('stars');
        star.classList.add('filled');
        star.textContent = '★';  // Filled star symbol
        starRating.appendChild(star);
    }

    // Add half star if needed
    if (hasHalfStar) {
        const halfStar = document.createElement('stars');
        halfStar.classList.add('half');
        halfStar.textContent = '★';  // Half star symbol (using a filled star with CSS)
        starRating.appendChild(halfStar);
    }


    const empty = document.createElement('empty');
    empty.classList.add('empty');
    const emptyStars = 5 - Math.ceil(average) + 1;  // Remaining empty stars
    for (let i = 0; i < emptyStars; i++) {
        const star = document.createElement('stars');
        star.textContent = '✰';  // Empty star symbol
        empty.appendChild(star);
        starRating.appendChild(empty);
    }

    averageRatingContainer.appendChild(ratingText);
    averageRatingContainer.appendChild(starRating);
}


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

        const rawDate = new Date(review.created_at);
        const formattedDate = rawDate.toLocaleDateString('en-GB', {
            day: '2-digit',
            month: 'short',
            year: 'numeric',
        });

        const date = document.createElement('p');
      date.classList.add('review-date');
      date.textContent = formattedDate;

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
        reviewFooter.appendChild(date);

        reviewFooter.appendChild(starRating);

        reviewDiv.appendChild(reviewFooter);

        // Append review to container
        reviewsContainer.appendChild(reviewDiv);
    });
}

document.getElementById("reviews-container").onmousemove = e => {
    for(const card of document.getElementsByClassName("review")){
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      card.style.setProperty("--mouse-x", `${x}px`);
      card.style.setProperty("--mouse-y", `${y}px`);
    }
  }
