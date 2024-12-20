from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

compiler = Tk()
compiler.title('My Fantastic IDE')
file_path = ''

# Default theme colors (light mode)
light_bg = '#FFFFFF'
light_fg = '#000000'
dark_bg = '#2D2D2D'
dark_fg = '#FFFFFF'

current_theme = 'light'  # Default to light theme

def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    if path:
        with open(path, 'r') as file:
            code = file.read()
            editor.delete('1.0', END)
            editor.insert('1.0', code)
            set_file_path(path)


def save_as():
    global file_path
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        if path:
            with open(path, 'w') as file:
                code = editor.get('1.0', END)
                file.write(code)
                set_file_path(path)
    else:
        with open(file_path, 'w') as file:
            code = editor.get('1.0', END)
            file.write(code)


def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.delete('1.0', END)
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)


# Function to toggle between light and dark themes
def change_theme():
    global current_theme
    if current_theme == 'light':
        editor.config(bg=dark_bg, fg=dark_fg, insertbackground=dark_fg)
        code_output.config(bg=dark_bg, fg=dark_fg)
        compiler.config(bg=dark_bg)
        current_theme = 'dark'
    else:
        editor.config(bg=light_bg, fg=light_fg, insertbackground=light_fg)
        code_output.config(bg=light_bg, fg=light_fg)
        compiler.config(bg=light_bg)
        current_theme = 'light'


menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

theme_menu = Menu(menu_bar, tearoff=0)
theme_menu.add_command(label='Toggle Theme', command=change_theme)
menu_bar.add_cascade(label='Theme', menu=theme_menu)

compiler.config(menu=menu_bar)

# Editor Text widget
editor = Text(bg=light_bg, fg=light_fg, insertbackground=light_fg)
editor.pack()

# Output Text widget for running the code
code_output = Text(height=10, bg=light_bg, fg=light_fg, insertbackground=light_fg)
code_output.pack()

compiler.mainloop()
