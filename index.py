import tkinter as tk
import markdown

def convert_markdown():
    markdown_text = text_input.get("1.0", "end-1c")
    html = markdown.markdown(markdown_text)
    text_output.delete("1.0", "end")
    text_output.insert("1.0", html)

# GUI setup
root = tk.Tk()
root.title("Markdown to HTML Converter")

label_input = tk.Label(root, text="Enter Markdown Text:")
label_input.pack()

text_input = tk.Text(root, height=10, width=50)
text_input.pack()

button_convert = tk.Button(root, text="Convert to HTML", command=convert_markdown)
button_convert.pack()

label_output = tk.Label(root, text="Generated HTML:")
label_output.pack()

text_output = tk.Text(root, height=10, width=50)
text_output.pack()

root.mainloop()