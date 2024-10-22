import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider

# Define allowed functions
allowed_functions = {
    'sin': np.sin,
    'cos': np.cos,
    'tan': np.tan,
    'sqrt': np.sqrt,
    'log': np.log,
    'exp': np.exp,
    'abs': np.abs,
    'pi': np.pi,
    'e': np.e
}

# Global variables
x_range = [-10, 10]
y_range = [-10, 10]
equation_rhs = ""

def calculate_y(x_vals):
    global equation_rhs
    try:
        return eval(equation_rhs, {"__builtins__": None}, {"x": x_vals, **allowed_functions})
    except Exception as e:
        print(f"Error evaluating the function: {e}")
        return np.zeros_like(x_vals)

def update_plot(val=None):
    global line, x_range, y_range
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    y_vals = calculate_y(x_vals)
    line.set_xdata(x_vals)
    line.set_ydata(y_vals)
    ax.set_xlim(x_range)
    ax.set_ylim(y_range)
    fig.canvas.draw_idle()

def update_x_range(val):
    global x_range
    x_range = [sxmin.val, sxmax.val]
    update_plot()

def update_y_range(val):
    global y_range
    y_range = [symin.val, symax.val]
    update_plot()

def reset(event):
    global x_range, y_range
    x_range = [-10, 10]
    y_range = [-10, 10]
    sxmin.reset()
    sxmax.reset()
    symin.reset()
    symax.reset()
    update_plot()

# Input equation
while True:
    equation = input("Enter an equation in the form y = f(x) (e.g., y = 2*x + 3 or y = sin(x)): ")
    try:
        lhs, equation_rhs = equation.replace(' ', '').split('=')
        if lhs != 'y':
            raise ValueError("Invalid equation format. Please use the format 'y = f(x)'.")
        break  
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

plt.ion()  
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.35)
x_vals = np.linspace(x_range[0], x_range[1], 400)
y_vals = calculate_y(x_vals)
line, = ax.plot(x_vals, y_vals, label=equation)
ax.set_xlim(x_range)
ax.set_ylim(y_range)
ax.legend()
ax.grid(True)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Create widgets
axcolor = 'lightgoldenrodyellow'
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
button.on_clicked(reset)

axxmin = plt.axes([0.1, 0.25, 0.65, 0.03], facecolor=axcolor)
sxmin = Slider(axxmin, 'X Min', -100.0, 0.0, valinit=x_range[0])
sxmin.on_changed(update_x_range)

axxmax = plt.axes([0.1, 0.2, 0.65, 0.03], facecolor=axcolor)
sxmax = Slider(axxmax, 'X Max', 0.0, 100.0, valinit=x_range[1])
sxmax.on_changed(update_x_range)

axymin = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor=axcolor)
symin = Slider(axymin, 'Y Min', -100.0, 0.0, valinit=y_range[0])
symin.on_changed(update_y_range)

axymax = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor=axcolor)
symax = Slider(axymax, 'Y Max', 0.0, 100.0, valinit=y_range[1])
symax.on_changed(update_y_range)

# Show plot and keep interactive mode active
plt.show()

while True:
    update_plot()
    plt.pause(0.1)