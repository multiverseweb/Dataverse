const form = document.getElementById('ratingForm');

form.addEventListener('submit', async function (event) {
    event.preventDefault();

    const formData = new FormData(form);
    const data = {
        name: formData.get('name'),
        email: formData.get('email'),
        rating: formData.get('rating'),
        review: formData.get('review')
    };

    try {
        const response = await fetch('/submit-review', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const result = await response.json();

        const messageElement = document.getElementById('responseMessage');
        if (result.success) {
            messageElement.textContent = "Thank you for your review!";
            messageElement.style.color = 'green';
            form.reset();
        } else {
            messageElement.textContent = "There was an error submitting your review.";
            messageElement.style.color = 'red';
        }
    } catch (error) {
        const messageElement = document.getElementById('responseMessage');
        messageElement.textContent = "There was an error submitting your review: " + error.message;
        messageElement.style.color = 'red';
    }
});
