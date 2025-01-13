import mysql.connector
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
            host="localhost",
            user="root",
            password="ananyavastare2345",
            database="finance_data",
        )
        cursor = connection.cursor(dictionary=True)

        # Fetch user data
        cursor.execute("SELECT user_id FROM user WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user:
            user_id = user["user_id"]

            # Ensure all results are fetched or cleared before running the next query
            cursor.fetchall()  # Add this to avoid unread results

            # Fetch income data for the user
            cursor.execute(
                """
                SELECT income_source, amount, date_received 
                FROM income 
                WHERE user_id = %s
            """,
                (user_id,),
            )
            income_data = cursor.fetchall()

            # Organize data by income source
            data_by_source = {}
            for row in income_data:
                source = row["income_source"]
                if source not in data_by_source:
                    data_by_source[source] = {"dates": [], "amounts": []}
                data_by_source[source]["dates"].append(row["date_received"])
                data_by_source[source]["amounts"].append(row["amount"])

            return data_by_source
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

    # Create Line chart to show income amounts over time
    for label, values in income_data.items():
        axs[1].plot(
            values["dates"],
            values["amounts"],
            marker="o",
            linestyle="-",
            linewidth=2,
            label=label,
        )
    axs[1].set_title("Income Sources Over Time")
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
