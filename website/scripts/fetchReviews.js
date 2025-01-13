import fs from 'fs';
import fetch from 'node-fetch';

const NETLIFY_API_URL = "https://api.netlify.com/api/v1";
const ACCESS_TOKEN = ""; // Replace with your token
const SITE_ID = ""; // Replace with your form's ID

async function fetchFormSubmissions() {
  try {
    const response = await fetch(`${NETLIFY_API_URL}/sites/${SITE_ID}/form_submissions`, {
      headers: {
        Authorization: `Bearer ${ACCESS_TOKEN}`,
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`Failed to fetch submissions: ${response.statusText}`);
    }

    const submissions = await response.json();

    // Write submissions to a JSON file
    fs.writeFileSync("reviews.json", JSON.stringify(submissions, null, 2));

    console.log("Form submissions have been saved to reviews.json");
  } catch (error) {
    console.error("Error fetching form submissions:", error);
  }
}

fetchFormSubmissions();
