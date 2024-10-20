import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression


# Sample data for testing
sample_data = {
    'entryDate': [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(30)],  # Last 30 days
    'total': np.random.randint(1000, 5000, size=30).tolist(),  # Random total expenditure values
    'expenditure': np.random.randint(100, 1000, size=30).tolist()  # Random monthly expenditures
}

requireds = sample_data

#=======================================================================================================Predictive Analytics (Linear Regression)
def predict_future_expenditure(pool):
    if 'entryDate' not in pool or 'total' not in pool:
        print("Missing required columns in pool.")
        return

    try:
        entry_dates = [datetime.strptime(date, '%Y-%m-%d') for date in pool['entryDate']]
    except ValueError as e:
        print(f"Error parsing entryDate: {e}")
        return

    total = pool['total']
    if not isinstance(total, list) or not all(isinstance(x, (int, float)) for x in total):
        print("Invalid total values. Ensure all values are numeric.")
        return
    
    if len(entry_dates) != len(total):
        print("Mismatch in lengths of entryDate and total.")
        return

    X = np.array([i for i in range(len(entry_dates))]).reshape(-1, 1)
    y = np.array(total)

    model = LinearRegression().fit(X, y)

    # Predict for the next 30 days
    future_dates = np.array([i for i in range(len(entry_dates), len(entry_dates) + 30)]).reshape(-1, 1)
    future_predictions = model.predict(future_dates)

    # Plotting
    plt.figure(figsize=(10, 5))
    future_dates_list = [entry_dates[-1] + timedelta(days=i) for i in range(1, 31)]
    plt.plot(entry_dates, y, label="Past Data")
    plt.plot(future_dates_list, future_predictions, label="Predicted", color='red')
    plt.legend()
    plt.title("Future Expenditure Prediction")
    plt.xlabel("Date")
    plt.ylabel("Expenditure")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#=======================================================================================================Monthly Comparison
def monthly_comparison(pool):
    if 'entryDate' not in pool or 'expenditure' not in pool:
        print("Missing required columns in pool.")
        return

    try:
        entry_dates = pd.to_datetime(pool['entryDate'])
    except ValueError as e:
        print(f"Error parsing entryDate: {e}")
        return

    expenditure = pool['expenditure']
    if not isinstance(expenditure, list) or not all(isinstance(x, (int, float)) for x in expenditure):
        print("Invalid expenditure values. Ensure all values are numeric.")
        return

    if len(entry_dates) != len(expenditure):
        print("Mismatch in lengths of entryDate and expenditure.")
        return

    df = pd.DataFrame({'entryDate': entry_dates, 'expenditure': expenditure})

    df['month'] = df['entryDate'].dt.to_period('M')  
    monthly_data = df.groupby('month')['expenditure'].sum()  

    # Plotting
    plt.figure(figsize=(10, 6))
    monthly_data.plot(kind='bar', color='skyblue')
    plt.title("Monthly Expenditure Comparison")
    plt.xlabel("Month")
    plt.ylabel("Total Expenditure")
    plt.xticks(rotation=45)  
    plt.tight_layout()  
    plt.show()



print("Running Monthly Comparison...")
monthly_comparison(requireds) 

print("\nRunning Future Expenditure Prediction...")
predict_future_expenditure(requireds)  
