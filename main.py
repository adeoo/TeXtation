import tkinter as tk
from dotenv import load_dotenv
from api import get_latex_equation
from settings import initialize_settings
from tkinter import messagebox


def convert_prompt(text_input_widget, text_output_widget):
    # Extract the input prompt from the Text widget
    prompt = text_input_widget.get("1.0", tk.END).strip()

    # Get the LaTeX equation using the extracted prompt
    latex_equation = get_latex_equation(prompt)

    # Clear the output Text widget and insert the LaTeX equation
    text_output_widget.delete("1.0", tk.END)
    text_output_widget.insert(tk.END, latex_equation)

def copy_to_clipboard(output_widget, root):
    try:
        root.clipboard_clear()  # Clear the clipboard
        text_to_copy = output_widget.get("1.0", tk.END).strip()  # Get text from output
        root.clipboard_append(text_to_copy)  # Append text to the clipboard
        messagebox.showinfo("Success", "Output copied to clipboard!")  # Optional: show a confirmation message
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy: {e}")

def set_api_key(root):
    # This function will be called when the user selects the option to set the API key
    api_key = simpledialog.askstring("API Key", "Enter your API key:", parent=root)
    if api_key:
        # Here you would normally save this API key to a file or an environment variable
        print(api_key)  # For demonstration purposes, we're just printing it
        # For example, you might use: openai.api_key = api_key


def main():
    load_dotenv()  # Load environment variables from a .env file
    initialize_settings()  # Load non-sensitive settings from a config file

    root = tk.Tk()
    root.title("Equation Converter")

    # Input text widget
    label_input = tk.Label(root, text="Enter your prompt:")
    label_input.pack()
    text_input = tk.Text(root, height=5, width=50)
    text_input.pack()

    # Output text widget
    label_output = tk.Label(root, text="LaTeX Output:")
    label_output.pack()
    text_output = tk.Text(root, height=5, width=50)
    text_output.pack()

    # Button to trigger conversion
    convert_button = tk.Button(root, text="Convert", command=lambda: convert_prompt(text_input, text_output))
    convert_button.pack()

    # Button to copy output to clipboard
    copy_button = tk.Button(root, text="Copy to Clipboard", command=lambda: copy_to_clipboard(text_output, root))
    copy_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
