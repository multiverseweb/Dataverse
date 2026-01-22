import mysql.connector
import db_config
from fpdf import FPDF
import matplotlib.pyplot as plt
from datetime import date
import os
import seaborn as sns
import matplotlib.dates as mdates

# Function to fetch data from the database
def fetch_data_from_db(username):
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host=db_config.DB_HOST,
            user=db_config.DB_USER,
            password=db_config.DB_PASSWORD,
            database=db_config.DB_NAME,
        )
        cursor = connection.cursor(dictionary=True)

        # Fetch user data (align with app schema: table `user`, columns `u_id`, `u_name`)
        cursor.execute("SELECT u_id FROM user WHERE u_name = %s", (username,))
        user = cursor.fetchone()

        if user:
            user_id = user["u_id"]

            # Get finance breakdown for most recent date for pie, and timeline for line
            cursor.execute(
                "SELECT MAX(entryDate) AS last_date FROM finance WHERE u_id = %s",
                (user_id,)
            )
            last = cursor.fetchone()
            last_date = last["last_date"]

            # For pie: take latest row's categories
            cursor.execute(
                """
                SELECT salary, gold, stocks, commodity, sales, expenditure
                FROM finance
                WHERE u_id = %s AND entryDate = %s
                """,
                (user_id, last_date)
            )
            latest_row = cursor.fetchone()

            # For line: time series of total over dates
            cursor.execute(
                "SELECT entryDate, total FROM finance WHERE u_id = %s ORDER BY entryDate",
                (user_id,)
            )
            timeline_rows = cursor.fetchall()

            # Build a structure compatible with create_combined_chart
            # Map categories for pie
            income_data = {
                "Salary": {"dates": [last_date], "amounts": [latest_row["salary"]]},
                "Gold": {"dates": [last_date], "amounts": [latest_row["gold"]]},
                "Stocks": {"dates": [last_date], "amounts": [latest_row["stocks"]]},
                "Commodity": {"dates": [last_date], "amounts": [latest_row["commodity"]]},
                "Sales": {"dates": [last_date], "amounts": [latest_row["sales"]]},
                "Expenditure": {"dates": [last_date], "amounts": [latest_row["expenditure"]]},
                "Total Timeline": {
                    "dates": [row["entryDate"] for row in timeline_rows],
                    "amounts": [row["total"] for row in timeline_rows],
                },
            }

            return income_data
        else:
            print(f"User {username} not found.")
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

    finally:
        if cursor:
            cursor.close()  # Close the cursor
        if connection:
            connection.close()  # Close the connection


# Function to create a combined pie and line chart for the income data
def create_combined_chart(income_data, plot_path="combined_plot.png"):
    # Prepare labels and amounts for the pie chart
    labels = list(income_data.keys())
    amounts = [sum(data["amounts"]) for data in income_data.values()]
    colors = sns.color_palette("pastel", len(labels))

    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    # Create Pie chart to show income distribution
    axs[0].pie(
        amounts,
        labels=labels,
        autopct="%1.1f%%",
        startangle=140,
        colors=colors,
        shadow=True,
    )
    axs[0].set_title("Income Sources Distribution")
    axs[0].axis("equal")

    # Create Line chart to show total amount over time (from key 'Total Timeline')
    if "Total Timeline" in income_data:
        tt = income_data["Total Timeline"]
        axs[1].plot(
            tt["dates"],
            tt["amounts"],
            marker="o",
            linestyle="-",
            linewidth=2,
            label="Total",
        )
    axs[1].set_title("Total Over Time")
    axs[1].set_xlabel("Date")
    axs[1].set_ylabel("Amount ($)")
    axs[1].grid(True)
    axs[1].legend(loc="upper left")
    axs[1].xaxis.set_major_locator(mdates.MonthLocator())
    axs[1].xaxis.set_major_formatter(mdates.DateFormatter('%b %d, %Y'))
    plt.xticks(rotation=45)

    # Adjust layout and save the combined plot
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()


# Function to save the financial report as a PDF
def save_report(u_name, plot_path="combined_plot.png"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)

    # Add title and user details to the PDF
    pdf.cell(200, 10, txt="Dataverse Financial Report", ln=1, align="C")
    pdf.cell(200, 10, txt="Date: {}".format(date.today()), ln=1, align="L")
    pdf.cell(200, 10, txt="User: {}".format(u_name), ln=1, align="L")

    # Add the combined plot image if it exists
    if os.path.exists(plot_path):
        pdf.image(plot_path, x=10, y=40, w=190, h=120)

    # Save the PDF file with a dynamic name (username and current date)
    pdf_file_name = f"{u_name}-{date.today()}-Dataverse.pdf"
    pdf.output(pdf_file_name)
    print(f"PDF saved as: {pdf_file_name}")


# Main function to run the report generation
def main():
    username = input("Enter the username:")  # Get the username input from the user
    income_data = fetch_data_from_db(username)

    if income_data:
        # Create charts from the fetched income data
        create_combined_chart(income_data)

        # Generate and save the PDF report
        save_report(username)
    else:
        print(f"No income data found for {username}.")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
