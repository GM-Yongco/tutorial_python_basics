# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: A simple Tkinter app to detect L = { anbncn / n ≥ 0 }:
# ========================================================================
# HEADERS
# ========================================================================
import tkinter as tk

# ========================================================================
# FUNCTIONS 01
# ========================================================================

def detect_abc(x:str = "") -> bool:
	count_a:int = 0
	count_b:int = 0
	count_c:int = 0
	x:list = list(x)
	ret_val = False

	word_len:int = len(x)
	i = 0
	while i < word_len and x[i] == 'a':
		count_a += 1
		i += 1
	while i < word_len and x[i] == 'b':
		count_b += 1
		i += 1
	while i < word_len and x[i] == 'c':
		count_c += 1
		i += 1
	if i == word_len and count_a == count_b == count_c:
		ret_val = True

	return ret_val

def button_function(input_box: tk.Entry, output_box: tk.Text) -> None:
	input_text = input_box.get()

	output_text = "YES" if detect_abc(input_text) else "NO"
	
	output_box.config(state=tk.NORMAL)
	output_box.delete(1.0, tk.END)
	output_box.insert(tk.END, output_text)
	output_box.config(state=tk.DISABLED)

# ctrl+a functionality
def select_all(event: tk.Event) -> str:
	event.widget.select_range(0, tk.END)
	return 'break'  # Prevent the default behavior

# ========================================================================
# FUNCTIONS 02
# ========================================================================

WINDOW_TITLE = "ABC Sequence"
INPUT_LABEL_TEXT = "Input:"
OUTPUT_LABEL_TEXT = "Output:"
BUTTON_TEXT = "Detect"

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

	# button functionality
	button = tk.Button(root, text=BUTTON_TEXT, command=lambda: button_function(input_box, output_box))
	button.grid(row=2, columnspan=2, pady=10)

	# ctr+a and enter functionality
	input_box.bind(sequence="<Control-a>", func=select_all)
	input_box.bind(sequence="<Return>", func=lambda event: button_function(input_box, output_box))

	return root

def run_app() -> None:
	root = setup_ui()
	root.mainloop()

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	run_app()