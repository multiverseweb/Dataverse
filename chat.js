document.querySelector('.chat-header').addEventListener('click', () => {
    const chatBody = document.querySelector('.chat-body');
    const chatInput = document.querySelector('.chat-input');
    const isOpen = chatBody.style.display === 'block';

    // Toggle visibility
    chatBody.style.display = isOpen ? 'none' : 'block';
    chatInput.style.display = isOpen ? 'none' : 'flex';
});

function toggleChatbot() {
    const chatbot = document.getElementById('chatbot');
    chatbot.style.display = chatbot.style.display === 'block' ? 'none' : 'block';
}

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    // Display user message
    displayMessage(userInput, 'user-message');

    // Clear input field
    document.getElementById('user-input').value = '';

    // Simulate bot response
    setTimeout(() => {
        let botResponse = generateBotResponse(userInput);
        displayMessage(botResponse, 'bot-message');
    }, 500);
}

function displayMessage(message, className) {
    const chatBody = document.getElementById('chat-body');
    const messageElement = document.createElement('div');
    messageElement.className = className;
    messageElement.textContent = message;
    chatBody.appendChild(messageElement);
    chatBody.scrollTop = chatBody.scrollHeight;
}

function generateBotResponse(userInput) {
    userInput = userInput.toLowerCase();

    // Data visualization related responses
    if (userInput.includes('dataverse') || userInput.includes('dataverse')) {
        return 'An Open-Source Software (OSS) that integrates database management, data visualization and data wrangling';
    } else if (userInput.includes('bar chart') || userInput.includes('line chart')) {
        return 'Bar charts and line charts are great for showing trends over time. Do you want help with creating one or interpreting data?';
    } else if (userInput.includes('pie chart')) {
        return 'Pie charts are useful for displaying proportions or percentages. Would you like help with creating one or using a specific tool?';
    } else if (userInput.includes('dashboard')) {
        return 'Dashboards are essential for summarizing key metrics. I can provide guidance on tools like Tableau, Power BI, or custom solutions using JavaScript libraries. What data do you need to visualize?';
    } else if (userInput.includes('heatmap')) {
        return 'Heatmaps are ideal for visualizing data density or intensity. Are you looking to create a heatmap for geographic data, correlation matrices, or something else?';
    } else if (userInput.includes('scatter plot')) {
        return 'Scatter plots are useful for visualizing relationships between variables. Do you need help plotting data points or understanding correlation patterns?';
    }
    else if (userInput.includes('software features')) {
        return 'This software enables data visualization in basic and advanced forms, supports Excel inputs, allows chart downloads, functions as a finance tracker, securely stores data and passwords using encryption, and offers data storage for future use.';
    }
    else if (userInput.includes('contribute')) {
        return 'Yes you can contribute to this project, pls click on github repo link mentioned in website';
    }

    // Personal finance related responses
    else if (userInput.includes('budget') || userInput.includes('budgeting')) {
        return 'Effective budgeting involves tracking income and expenses. Do you need help with budgeting strategies, tools, or automating expense tracking?';
    } else if (userInput.includes('expense') || userInput.includes('track expenses')) {
        return 'Tracking expenses can help identify areas to save. I can suggest tools for manual tracking, or automated solutions like connecting bank accounts. Would you like recommendations?';
    } else if (userInput.includes('investment') || userInput.includes('investing')) {
        return 'Investing involves risks, but can help grow wealth over time. Are you interested in stocks, bonds, mutual funds, or cryptocurrencies?';
    } else if (userInput.includes('savings') || userInput.includes('save money')) {
        return 'Saving money is essential for financial stability. I can share tips on setting savings goals, automating savings, or high-yield savings accounts. What are you saving for?';
    } else if (userInput.includes('debt') || userInput.includes('loan')) {
        return 'Managing debt is important for financial health. Would you like advice on debt repayment strategies, consolidating loans, or understanding interest rates?';
    } else if (userInput.includes('retirement')) {
        return 'Planning for retirement requires setting long-term financial goals. I can help with understanding retirement accounts, investments, and savings plans. How far along are you in your planning?';
    } else if (userInput.includes('insurance')) {
        return 'Insurance is crucial for risk management. Are you looking for help with life, health, auto, or home insurance? I can provide general advice or suggest tools for comparison.';
    } else if (userInput.includes('cryptocurrency') || userInput.includes('crypto')) {
        return 'Cryptocurrency can be a volatile investment. Are you interested in trading, understanding blockchain, or exploring different coins?';

    // General fallback response for unrecognized inputs
    } else {
        return 'I am here to help with data visualization and personal finance tracking. Please specify your query or ask about a specific topic!';
    }
}
