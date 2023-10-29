import tkinter as tk
def main():
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

    root.mainloop()

def convert_prompt(text_input, text_output):
    # Dummy function for now
    input_text = text_input.get("1.0", tk.END)
    output_text = f"Converted LaTeX: {input_text}"  # Placeholder for actual conversion logic
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, output_text)

if __name__ == "__main__":
    main()
