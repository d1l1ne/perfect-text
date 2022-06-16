from time import perf_counter
import func_module
import tkinter as tk
from tkinter import ttk
import pyperclip
import requests
from bs4 import BeautifulSoup
import webbrowser
from tkinter import messagebox as mb
from tkinter import filedialog as fid
from tkinter.filedialog import asksaveasfilename


root = tk.Tk()


#adapting window size to user's configuration
if int(root.winfo_screenheight())<720 or int(root.winfo_screenwidth())<1280:
    screen_width = int(root.winfo_screenwidth()*0.66)
    screen_height = int(root.winfo_screenheight()*0.66)
else:
    screen_width = 1267
    screen_height = 713
root.geometry(f'{screen_width}x{screen_height}')
root.title('PerfectText')
root.iconbitmap('perfecttext.ico')
root.resizable(False, False)


w = ttk.Frame(root, padding='10 10 10 10')
w.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))



fp = tk.IntVar()
fb = tk.IntVar()
fs = tk.IntVar()
fd = tk.IntVar()
ba = tk.IntVar()
sa = tk.IntVar()
sa.set(0)
output_text=''
input_text=''
radio_var=tk.IntVar()

input_label = ttk.Label(w, text='Your text:', font=('arial', 20, 'bold'))
input_field = tk.Text(w, font='arial')
output_label = ttk.Label(w, text='Result:', font=('arial', 20, 'bold'))
output_field = tk.Text(w, font='arial')
start_button = ttk.Button(w, text="Start!")
copy_button = ttk.Button(w, text='COPY')
paste_button = ttk.Button(w, text='PASTE')
clear_input = ttk.Button(w, text='CLEAR')
clear_output = ttk.Button(w, text='CLEAR')
fix_punc = ttk.Checkbutton(w, text='Fix punctuation spaces', variable=fp, state='DISABLED')
fix_brac = ttk.Checkbutton(w, text='Fix brackets', variable=fb, state='DISABLED')
fix_sep = ttk.Checkbutton(w, text='Fix sentence separation', variable=fs, state='DISABLED')
fix_dash = ttk.Checkbutton(w, text='Fix dashes', variable=fd, state='DISABLED')
select_all = ttk.Button(w, text='SELECT ALL')
console_label = ttk.Label(w, text='Console:', font=('arial', 10, 'bold'))
console_field = tk.Listbox(w, width=25)
version_button = ttk.Button(w, text='Version 1.1')
domains_check_true = ttk.Radiobutton(w, text='My text contains web-addresses or emails', variable=radio_var, value=1)
domains_check_false = ttk.Radiobutton(w, text="My text doesn't contain web-addresses or emails", variable=radio_var, value=0)
save_as=ttk.Button(w, text="Save as TXT")

input_label.grid(column=1, row=0, padx=(0, 90))
input_field.grid(column=0, row=1, columnspan=3, rowspan=3)
output_label.grid(column=5, row=0)
output_field.grid(column=4, row=1, columnspan=3, rowspan=3)
start_button.grid(column=3, row=2, ipadx=5, padx=10)
copy_button.grid(column=6, row=0, sticky='e')
paste_button.grid(column=0, row=0, sticky='w')
clear_input.grid(column=2, row=0, sticky='e')
clear_output.grid(column=4, row=0, sticky='w')
fix_punc.grid(column=0, row=4, sticky='w')
fix_brac.grid(column=1, row=4, sticky='w')
fix_sep.grid(column=0, row=5, sticky='w')
fix_dash.grid(column=1, row=5, sticky='w')
select_all.grid(column=0, row=6, sticky='nw')
console_label.grid(column=4, row=5, sticky='w')
console_field.grid(column=4, row=6, columnspan=2, rowspan=2, sticky='w')
version_button.place(relx=0.94, rely=0.97)
domains_check_true.place(relx=0.001, rely=0.8)
domains_check_false.place(relx=0.001, rely=0.83)
save_as.place(relx=0.94, rely=0.7)

def process():
    output_field.delete(1.0, 'end')
    console_field.delete(0, 'end')
    input_text = input_field.get("1.0",'end-1c') + ' '
    if input_text!='':
        start_button['state']='disabled'
        start_time = perf_counter()
        input_text = func_module.del_multi_spaces(input_text)
        result = perf_counter()-start_time
        result = str("%.4f" % result) + 's'
        console_field.insert('end', f'Text preparing: {result}')
        if fp.get()==1:
            start_time = perf_counter()
            input_text = func_module.del_punctuation_spaces(input_text)
            result = perf_counter()-start_time
            result = str("%.4f" % result) + 's'
            console_field.insert('end', f'Fixing punctuation: {result}')
        if fb.get()==1:
            start_time = perf_counter()
            input_text = func_module.del_brackets_spaces(input_text)
            result = perf_counter()-start_time
            result = str("%.4f" % result) + 's'
            console_field.insert('end', f'Fixing brackets: {result}')
        if fs.get()==1:
            if radio_var.get()==0:
                start_time = perf_counter()
                input_text = func_module.fix_separation_of_sentences(input_text)
                result = perf_counter()-start_time
                result = str("%.4f" % result) + 's'
                console_field.insert('end', f'Fixing separation: {result}')
            elif radio_var.get()==1:
                start_time = perf_counter()
                input_text = func_module.fix_separation_wsites(input_text)
                result = perf_counter()-start_time
                result = str("%.4f" % result) + 's'
                console_field.insert('end', f'Fixing separation: {result}')
        if fd.get()==1:
            start_time = perf_counter()
            input_text = func_module.fix_dashes(input_text)
            result = perf_counter()-start_time
            result = str("%.4f" % result) + 's'
            console_field.insert('end', f'Fixing dashes: {result}')
        output_field.insert(1.0, input_text)
        start_button['state']='normal'

def delete_input():
    input_field.delete(1.0, 'end')
def delete_output():
    output_field.delete(1.0, 'end')

def sel_all():
    if sa.get()==0:
        fp.set(1)
        fb.set(1)
        fs.set(1)
        fd.set(1)
        select_all['text']='DESELECT ALL'
        sa.set(1)
    elif sa.get()==1:
        fp.set(0)
        fb.set(0)
        fs.set(0)
        fd.set(0)
        select_all['text']='SELECT ALL'
        sa.set(0)
        
def copying():
    pyperclip.copy(output_field.get("1.0",'end-1c'))
def pasting():
    input_field.delete(1.0, 'end')
    input_field.insert(1.0, pyperclip.paste())
    
def check_version():
    try:
        requests.head("http://www.google.com/", timeout=1)
        connection = True
    except requests.ConnectionError:
        showerror(title='Unable to check version', message='Unable to check version\nNo internet connection')
        connection = False
    if connection:
        response = requests.get('https://drive.google.com/drive/folders/1rxlP_r7VqY3scYGzdJpk3QADHxkLkpg7')
        soup = BeautifulSoup(response.text, 'html.parser')
        w=str(soup.find('title'))
        ok = w[7:21]
        if ok!='PerfectText1.1':
            answer = askyesno(title='Version 1.1', message='New version is available. Do you want to download it?')
            if answer:
                webbrowser.open('https://drive.google.com/drive/folders/1rxlP_r7VqY3scYGzdJpk3QADHxkLkpg7', new=2)
        elif ok=='PerfectText1.1':
            showinfo(title='Version 1.1', message='You\'re using the latest version!')

def save_as_txt():
    if output_field.get("1.0",'end-1c')=='':
        showerror(title='Error', message='No content in output field')
    else:
        file = asksaveasfilename(filetypes=[("TEXT FILE", ".txt")], defaultextension=".txt")
        saver = open(file, 'w')
        saver.write(output_field.get("1.0",'end-1c'))
        saver.close()

start_button['command']=process 
clear_input['command']=delete_input
clear_output['command']=delete_output
select_all['command']=sel_all
copy_button['command']=copying
paste_button['command']=pasting
version_button['command']=check_version
save_as['command']=save_as_txt
     
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

w.columnconfigure(0, weight=1)
w.columnconfigure(1, weight=1)
w.columnconfigure(2, weight=1)
w.columnconfigure(3, weight=1)
w.columnconfigure(4, weight=1)
w.columnconfigure(5, weight=1)
w.columnconfigure(6, weight=1)
w.rowconfigure(0, weight=1)
w.rowconfigure(1, weight=1)
w.rowconfigure(2, weight=1)
w.rowconfigure(3, weight=1)
w.rowconfigure(4, weight=1)
w.rowconfigure(5, weight=1)
w.rowconfigure(6, weight=1)
w.rowconfigure(7, weight=1)


root.mainloop()
