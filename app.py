import tkinter as tk
from tkinter import scrolledtext
from textblob import TextBlob

# Function to correct grammar
def correct_text():
    original_text = input_text.get("1.0", tk.END)
    blob = TextBlob(original_text)
    corrected = blob.correct()
    
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, str(corrected))
    result_label.config(text="✅ Grammar and spelling corrected.")

# Debug print
print("Starting Grammar Checker...")

# Setup GUI
root = tk.Tk()
root.title("Grammar and Spelling Checker (TextBlob)")
root.geometry("700x500")

# Input label and text area
tk.Label(root, text="Enter your text:", font=("Helvetica", 14)).pack(pady=10)
input_text = scrolledtext.ScrolledText(root, height=10, width=80)
input_text.pack()

# Button to trigger correction
tk.Button(root, text="Correct Grammar", command=correct_text).pack(pady=10)

# Label to show status messages
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

# Label and text area for corrected text
tk.Label(root, text="Corrected Text:", font=("Helvetica", 14)).pack(pady=5)
result_text = scrolledtext.ScrolledText(root, height=10, width=80)
result_text.pack()

# Start the GUI event loop
root.mainloop()
