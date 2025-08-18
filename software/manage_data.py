import tabulate
import db_config
from tkinter import messagebox
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
# import report
import datetime
from datetime import datetime, timedelta, date
from matplotlib.widgets import Cursor as lines
import mysql.connector as my
from mysql.connector import Error

# Plot colors
colors = [
	"#440154", "#3b528b", "#21918c", "#5ec962", "#fde725",
	"#f89540", "#e16462", "#b12a90", "#6a00a8", "#0d0887",
	"#3474eb", "#5ec962", "yellow", "#f89540", "tomato", "tan"
]

# Connect to MySQL and ensure database selection
try:
	mycon = my.connect(
		host=db_config.DB_HOST,
		user=db_config.DB_USER,
		passwd=db_config.DB_PASSWORD,
	)
	cursor = mycon.cursor()
	cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_config.DB_NAME}`;")
	cursor.execute(f"USE `{db_config.DB_NAME}`;")
except Error as e:
	print(f"Error connecting to MySQL: {e}")
	messagebox.showerror(
		"Database Error",
		(
			f"Failed to connect to the database: {e}\n\n"
			"Execute the following query in your MYSQL Workbench or MySQL Shell and then try again:\n\n"
			"CREATE DATABASE DATAVERSE;"
		),
	)
	raise SystemExit(1)

# Global variable to track failed login attempts
z = 0

# ============================== Data access helpers ==============================

def view_data(user_id: int) -> str:
	try:
		query = "SELECT * FROM finance WHERE u_id=%s"
		cursor.execute(query, (user_id,))
		result_set = cursor.fetchall()
		if len(result_set) == 0:
			result_message = "Your dataSet is empty."
		else:
			columns = [col[0] for col in cursor.description]
			result_table = tabulate.tabulate(result_set, headers=columns, tablefmt="pretty")
			result_message = result_table
	except Error as e:
		result_message = f"Error fetching data: {e}"
		print(f"Database error: {e}")
	return result_message

# ============================== Auth & crypto ==============================

def decrypt(encrypted_password: str) -> str:
	password_length = len(encrypted_password)
	decrypted_password = ""
	if password_length % 2 == 0:
		transformed_pwd = encrypted_password[int(password_length / 2):]
		transformed_pwd += encrypted_password[:int(password_length / 2)]
	else:
		transformed_pwd = encrypted_password[int(password_length / 2) + 1:]
		transformed_pwd += encrypted_password[:int(password_length / 2) + 1]
	for character in transformed_pwd:
		decrypted_password += chr(ord(character) // 2)
	return decrypted_password


def check_credentials(username: str, password: str) -> str:
	try:
		# Check existence
		query = "SELECT u_name FROM user"
		cursor.execute(query)
		user_list = cursor.fetchall()
		usernames = [user[0] for user in user_list]
		if str(username) not in usernames:
			message = "No account exists with that username."
		else:
			query = "SELECT pwd FROM user WHERE u_name=%s"
			cursor.execute(query, (username,))
			fetched_password = cursor.fetchall()
			decrypted_password = decrypt(fetched_password[0][0])
			if decrypted_password == password:
				query = "SELECT u_id FROM user WHERE u_name=%s"
				cursor.execute(query, (username,))
				user_id = cursor.fetchall()[0][0]
				message = f"Login Successful. ✓\nUser ID: {user_id}"
			else:
				message = "Incorrect password! ✖"
				global z
				z += 1
				if z >= 2:
					print("There have been more than 1 failed login attempts. Closing the system.")
	except Error as e:
		message = f"Error during login: {e}"
		print(f"Database error: {e}")
	return message

# ============================== Data fetch for plots ==============================

def fetch_data(user_id: int):
	try:
		query = "SELECT * FROM finance WHERE u_id=%s"
		cursor.execute(query, (user_id,))
		result_set = cursor.fetchall()
		if len(result_set) == 0:
			return None
		else:
			cursor.execute("DESCRIBE finance")
			schema = cursor.fetchall()
			column_names = [column[0] for column in schema]
			data_pool = {}
			for column_name in column_names:
				column_data = []
				query = f"SELECT {column_name} FROM finance WHERE u_id=%s"
				cursor.execute(query, (user_id,))
				values = cursor.fetchall()
				for value in values:
					column_data.append(value[0])
				data_pool[column_name] = column_data
			return [column_names, data_pool]
	except Error as e:
		print(f"Error fetching user data: {e}")
		return None

# ============================== Visualization ==============================

def plot_data(requireds, username: str):
	try:
		download_report = messagebox.askyesno(message="Do you want to download today's report?", icon="question")
		if download_report is True:
			plt.savefig("plot.png", dpi=150)
			# report.save(username, total_amount)
			messagebox.showinfo(message="Report downloaded. ✓")

		plt.style.use('dark_background')
		fig, ax = plt.subplots(2, 2, figsize=(10.7, 6.6))
		plt.subplots_adjust(left=0.08, bottom=0.043, right=0.805, top=0.895, wspace=0.148, hspace=0.374)
		gs = GridSpec(2, 2, width_ratios=[2, 2], height_ratios=[1.5, 1])

		# Create the subplots
		ax[0, 0] = plt.subplot(gs[0, :])  # Line chart
		ax[1, 0] = plt.subplot(gs[1, 0])  # Pie chart
		ax[1, 1] = plt.subplot(gs[1, 1])  # Scatter chart

		for subplot in fig.get_axes():
			subplot.tick_params(bottom=False, labelbottom=False, left=False, right=False, labelleft=False)

		columns = requireds[0]
		data_pool = requireds[1]

		# Generate time labels for x-axis
		time_range = np.arange(min(data_pool["entryDate"]), date.today() + timedelta(days=2), timedelta(days=1)).astype(datetime)
		formatted_dates = [x.date().isoformat() for x in time_range]
		time_labels = np.array(formatted_dates)
		date_entries = [x.strftime('%Y-%m-%d') for x in data_pool["entryDate"]]

		# Line Chart
		line_data = list(data_pool.values())
		for i in range(1, len(line_data) - 1):
			current_data = []
			index = 0
			for j in range(len(time_range)):
				if time_labels[j] not in date_entries:
					current_data.append((current_data[j - 1] if j > 0 else 0))  # Use previous value or 0
				else:
					current_data.append(data_pool[columns[i]][index])
					index += 1
			ax[0, 0].plot(time_range, current_data, label=columns[i].title(), color=colors[i], linewidth=0.7, marker=".", markersize=0.0)

		ax[0, 0].tick_params(bottom=True, labelbottom=True, left=True, right=True, labelleft=True)
		ax[0, 0].legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0)
		ax[0, 0].set_title(f"{username.title()}_{date.today()}\nLine Chart")
		ax[0, 0].set_xlabel("Time")
		ax[0, 0].set_ylabel("Amount (₹)")
		ax[0, 0].axvline(x=date.today(), color='lime', linewidth=0.6, linestyle="dashed", label="Today")
		ax[0, 0].grid(linestyle="dashed", linewidth=1, alpha=0.25)

		# Spines customization for the line chart
		ax[0, 0].spines['bottom'].set_color('teal')
		ax[0, 0].spines['top'].set_color('#ffffff40')
		ax[0, 0].spines['right'].set_color('#ffffff30')
		ax[0, 0].spines['left'].set_color('darkturquoise')

		# Pie Chart (latest values)
		total_amount = line_data[-2][-1]
		pie_data = [val[-1] for val in line_data[1:-2]]
		pie_explode = [0] * (len(pie_data) - 1) + [0.1]  # Explode the last slice

		ax[1, 0].pie(pie_data, explode=pie_explode, colors=colors[1:len(columns) + 1])
		ax[1, 0].set_title(f"Money Distribution - {date.today()}")
		ax[1, 0].legend(labels=columns[1:len(columns) - 2], bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0)

		# Spines customization for the pie chart
		ax[1, 0].spines['bottom'].set_color('black')
		ax[1, 0].spines['top'].set_color('black')
		ax[1, 0].spines['right'].set_color('black')
		ax[1, 0].spines['left'].set_color('black')

		# Scatter (Expenditure over time)
		expenditure_data = line_data[-3]
		max_expenditure = max(expenditure_data)
		max_index = expenditure_data.index(max_expenditure)

		ax[1, 1].scatter(line_data[-1], expenditure_data, color=colors[2], label=columns[-3].title())
		ax[1, 1].scatter(line_data[-1][max_index], expenditure_data[max_index], color="red", label="Max Expenditure")
		ax[1, 1].set_title("Expenditure Till Now")
		ax[1, 1].legend(bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0)
		ax[1, 1].set_xlabel("Time")
		ax[1, 1].set_ylabel("Expenditure")
		ax[1, 1].grid(linestyle="dashed", linewidth=1, alpha=0.25)

		# Spines customization for the scatter chart
		ax[1, 1].spines['bottom'].set_color('black')
		ax[1, 1].spines['top'].set_color('black')
		ax[1, 1].spines['right'].set_color('black')
		ax[1, 1].spines['left'].set_color('black')

		# Positioning the graph window
		move_figure(fig, 230, 120)
		plt.show()
		plt.tight_layout()

		return [total_amount, max_expenditure]
	except Exception as e:
		print(f"Error in plotting data: {e}")
		messagebox.showerror("Plot Error", f"Failed to plot data: {e}")
		return None


# ============================== Window positioning ==============================

def move_figure(fig, x, y):
	backend = matplotlib.get_backend().lower()

	if 'tkagg' in backend:
		fig.canvas.manager.window.wm_geometry(f"+{x}+{y}")
	elif 'wxagg' in backend:
		fig.canvas.manager.window.SetPosition((x, y))
	elif 'qt5agg' in backend or 'qtagg' in backend:
		fig.canvas.manager.window.move(x, y)
	else:
		raise NotImplementedError(f"Backend '{backend}' is not fully supported for moving the figure.")