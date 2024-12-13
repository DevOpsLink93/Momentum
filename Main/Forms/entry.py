import tkinter as tk
from tkinter import messagebox

#start define saving task work
def save_task():
    task_title = task_title_entry.get()
    task_description = task_description_text.get("1.0", tk.END).strip()
    
    # Character limit on fields
    if len(task_title) > 50:
        messagebox.showwarning("Input Error", "Task Title cannot be longer than 50 characters.")
        return
    if len(task_description) > 2000:
        messagebox.showwarning("Input Error", "Task description cannot be longer than 2000 characters.")
        return
    
    #message box for debugging 
    messagebox.showinfo("Task Saved", "Your task has been saved successfully!")
    root.quit()

#have Description be a bulleted list 
def on_key_press(event):
    # bullet point when user presses Enter
    current_index = task_description_text.index(tk.INSERT)
    line_number = current_index.split('.')[0]
    line_start = f"{line_number}.0"
    
    # Only add a bullet point at the start of the new line
    if task_description_text.get(line_start, f"{line_number}.end") == '':
        task_description_text.insert(f"{line_number}.0", "• ")

# Create main window
root = tk.Tk()
root.title("Basic_Entry")

# Task Title Label and Entry (255 character limit)
task_title_label = tk.Label(root, text="Task Title (50 characters max):")
task_title_label.pack(pady=5)
task_title_entry = tk.Entry(root, width=50)
task_title_entry.pack(pady=5)

# Task description Label and Textbox (2000 character limit)
task_description_label = tk.Label(root, text="Task description (2000 characters max):")
task_description_label.pack(pady=5)
task_description_text = tk.Text(root, width=50, height=10)
task_description_text.pack(pady=5)

# Insert initial bullet point at the start
task_description_text.insert("1.0", "• ")

# Enter key to the on_key_press function for the task description textbox
task_description_text.bind("<Return>",on_key_press)

# Save Button
save_button = tk.Button(root, text="Save Task", command=save_task)
save_button.pack(pady=10)


# Run the main loop
root.mainloop()
