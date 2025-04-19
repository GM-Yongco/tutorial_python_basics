# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: A simple Tkinter app to reverse strings
# ========================================================================
# HEADERS
# ========================================================================
import tkinter as tk

# ========================================================================
# FUNCTIONS 01
# ========================================================================

def reverse_string(input_box: tk.Entry, output_box: tk.Text) -> None:
	# Reverses the input text and displays it in the output box
	input_text = input_box.get()
	reversed_text = input_text[::-1]
	
	output_box.config(state=tk.NORMAL)
	output_box.delete(1.0, tk.END)
	output_box.insert(tk.END, reversed_text)
	output_box.config(state=tk.DISABLED)

def select_all(event: tk.Event) -> str:
	# ctrl+a functionality
	event.widget.select_range(0, tk.END)
	return 'break'  # Prevent the default behavior

# ========================================================================
# FUNCTIONS 02
# ========================================================================

WINDOW_TITLE = "Reverse String Tool"
INPUT_LABEL_TEXT = "Input:"
OUTPUT_LABEL_TEXT = "Output:"
REVERSE_BUTTON_TEXT = "Reverse"

WORKING_TEXT = 50
TEXT_HEIGHT = 1

def setup_ui() -> tk.Tk:
	root = tk.Tk()
	root.title(WINDOW_TITLE)

	# input section
	input_label = tk.Label(root, text=INPUT_LABEL_TEXT)
	input_label.grid(row=0, column=0, padx=10, pady=5)
	input_box = tk.Entry(root, width=WORKING_TEXT)
	input_box.grid(row=0, column=1, padx=10, pady=5)

	# output section 
	output_label = tk.Label(root, text=OUTPUT_LABEL_TEXT)
	output_label.grid(row=1, column=0, padx=10, pady=5)
	output_box = tk.Text(root, height=TEXT_HEIGHT, width=WORKING_TEXT, wrap=tk.WORD, state=tk.DISABLED)
	output_box.grid(row=1, column=1, padx=10, pady=5)

	# reverse button
	reverse_button = tk.Button(root, text=REVERSE_BUTTON_TEXT, command=lambda: reverse_string(input_box, output_box))
	reverse_button.grid(row=2, columnspan=2, pady=10)

	# ctr+a and enter functionality
	input_box.bind(sequence="<Control-a>", func=select_all)
	input_box.bind(sequence="<Return>", func=lambda event: reverse_string(input_box, output_box))

	return root

def run_app() -> None:
	root = setup_ui()
	root.mainloop()

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	run_app()