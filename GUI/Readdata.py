import tkinter as tk
import csv

# Function to read CSV data
def read_csv(filename):
  with open(filename, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
  return data

# Function to display data in a table
def show_data(data):
  # Create the main window (Tk instance)
  root = tk.Tk()
  root.title("CSV Data Viewer")

  # Create the table widget
  table = tk.Frame(root)
  table.pack()

  # Set up table headers
  for i, col in enumerate(data[0]):
    label = tk.Label(table, text=col, borderwidth=1, relief="solid")
    label.grid(row=0, column=i)

  # Display data in the table
  for i, row in enumerate(data[1:]):
    for j, value in enumerate(row):
      label = tk.Label(table, text=value, borderwidth=1, relief="solid")
      label.grid(row=i+1, column=j)

  # Start the event loop
  root.mainloop()

# Prompt user to select CSV file
filename = tk.filedialog.askopenfilename()
if not filename:
  exit()

# Read CSV data
data = read_csv(filename)

# Display data in the table
show_data(data)
