import fpdf
import matplotlib.pyplot as plt
from datetime import date, timedelta
import os
import seaborn as sns  # Seaborn for better color palettes


def create_combined_chart(income_data, plot_path="combined_plot.png"):
    # Prepare data for the pie chart
    labels = list(income_data.keys())
    amounts = [
        sum(data["amounts"]) for data in income_data.values()
    ]  # Total for each source

    # Define a beautiful color palette using Seaborn
    colors = sns.color_palette("pastel", len(labels))

    # Create a figure with subplots
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    # Create pie chart with shadow and better styling
    axs[0].pie(
        amounts,
        labels=labels,
        autopct="%1.1f%%",
        startangle=140,
        colors=colors,
        shadow=True,
        wedgeprops={"edgecolor": "black"},
    )
    axs[0].set_title("Income Sources Distribution", fontsize=16, fontweight="bold")
    axs[0].axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Create line graph with smoother lines and larger markers
    for label, values in income_data.items():
        axs[1].plot(
            values["dates"],
            values["amounts"],
            marker="o",
            markersize=8,
            linestyle="-",
            linewidth=2,
            label=label,
        )

    axs[1].set_title("Income Sources Over Time", fontsize=16, fontweight="bold")
    axs[1].set_xlabel("Date", fontsize=12)
    axs[1].set_ylabel("Amount ($)", fontsize=12)
    axs[1].grid(True, linestyle="--", alpha=0.7)
    axs[1].legend(loc="upper left", fontsize=10)  # Show legend to identify lines

    # Apply general style and save the combined plot as a PNG file
    plt.tight_layout()
    plt.savefig(plot_path, dpi=300)
    plt.close()


def save_report(u_name, total, plot_path="combined_plot.png"):
    # Create PDF
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)
    pdf.set_fill_color(0, 0, 0)
    pdf.set_text_color(255, 255, 255)

    # Add Title
    pdf.cell(
        200,
        10,
        txt="Personal Finance Tracker & Data Visualization Software",
        ln=1,
        align="C",
        fill=True,
    )
    pdf.cell(200, 10, txt="Date: {}".format(date.today()), ln=1, align="L", fill=True)
    pdf.cell(200, 10, txt="Total: ${:.2f}".format(total), ln=1, align="L", fill=True)

    # Add the combined plot image
    if os.path.exists(plot_path):
        pdf.image(plot_path, x=None, y=None, w=190, h=120)
    else:
        pdf.cell(
            200, 10, txt="Combined plot image not found.", ln=1, align="L", fill=True
        )

    # Closing line
    pdf.cell(200, 20, txt="-Tejas, Ojas & Nandana :)", ln=1, align="R", fill=True)

    # Save PDF
    pdf_file_name = "{}-{}.pdf".format(u_name.title(), date.today())
    pdf.output(pdf_file_name)
    print("File name: {}".format(pdf_file_name))


# Example income data
income_data = {
    "Salary": {
        "dates": [date.today() - timedelta(days=i) for i in range(5)],
        "amounts": [1000, 1200, 1300, 1100, 1400],  # Example salary over time
    },
    "Investments": {
        "dates": [date.today() - timedelta(days=i) for i in range(5)],
        "amounts": [200, 250, 300, 275, 325],  # Example investment returns over time
    },
    "Freelancing": {
        "dates": [date.today() - timedelta(days=i) for i in range(5)],
        "amounts": [150, 180, 160, 200, 210],  # Example freelancing income over time
    },
}

# Create the combined chart
create_combined_chart(income_data)

# Save the report with the generated plot
save_report("John Doe", 1500.00)
