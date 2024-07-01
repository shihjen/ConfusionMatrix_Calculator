# import required dependencies
import tkinter as tk
from tkinter import ttk
from tkinter import *

# create root window
root = Tk()
root.title('Confusion Matrix Calculator')
root.geometry('1000x800')

# define styles
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12), padding=5)
style.configure('Title.TLabel', font=('Arial', 18, 'bold'), padding=10)
style.configure('TButton', font=('Arial', 12), padding=5)
style.configure('TEntry', font=('Arial', 12), padding=5)

title_label = ttk.Label(root, text='Confusion Matrix Calculator', style='Title.TLabel')
title_label.pack(pady=(10,0))

# create frames
## input frame
input_frame = ttk.Frame(root, padding="10 10 10 10")
input_frame.pack(expand=True)

## result frame
result_frame = ttk.Frame(root, padding="10 10 10 10")
result_frame.pack(expand=True)

## button frame
button_frame = ttk.Frame(root, padding="10 10 10 10")
button_frame.pack(expand=True)

tp_var = IntVar()
fp_var = IntVar()
tn_var = IntVar()
fn_var = IntVar()

# define a function to compute accuracy
def submit():
    tp = tp_var.get()
    fp = fp_var.get()
    tn = tn_var.get()
    fn = fn_var.get()

    # accuracy formula
    if tp + fp + tn + fn != 0:
        accuracy = (tp + tn) / (tp + fp + tn + fn)
        accuracy_text = f'Accuracy: {accuracy: .2f}'
    else:
        accuracy_text = 'Accuracy: Undefined (no inputs)'

    # precision formula
    if tp + fp != 0:
        precision = (tp) / (tp + fp)
        precision_text = f'Precision: {precision: .2f}'
    else:
        precision_text = 'Precision: Undefined (no inputs)'

    # recall formula
    if tp + fn != 0:
        recall = (tp) / (tp + fn)
        recall_text = f'Recall: {recall: .2f}'
    else:
        recall_text = 'Recall: Undefined (no inputs)'

    # F1 score formula
    if tp + (0.5*(fp + fn)) != 0:
        f1 = tp / (tp + (0.5*(fp + fn)))
        f1_text = f'F1 Score: {f1: .2f}'
    else:
        f1_text = 'F1 Score: Undefined (no inputs)'

    result_label.config(text='Result:')
    accuracy_label.config(text=accuracy_text)
    precision_label.config(text=precision_text)
    recall_label.config(text=recall_text)
    f1_label.config(text=f1_text)

# GUI - input frame
## true positive input
ttk.Label(input_frame, text='True Positive', background='lightblue').grid(row=0, column=0, padx=5, pady=5)
ttk.Entry(input_frame, textvariable=tp_var).grid(row=0, column=1, padx=5, pady=5)

## false positive input
ttk.Label(input_frame, text='False Positive', background='lightblue').grid(row=1, column=0, padx=5, pady=5)
ttk.Entry(input_frame, textvariable=fp_var).grid(row=1, column=1, padx=5, pady=5)

## true negative input
ttk.Label(input_frame, text='True Negative', background='lightblue').grid(row=2, column=0, padx=5, pady=5)
ttk.Entry(input_frame, textvariable=tn_var).grid(row=2, column=1, padx=5, pady=5)

## false negative input
ttk.Label(input_frame, text='False Negative', background='lightblue').grid(row=3, column=0, padx=5, pady=5)
ttk.Entry(input_frame, textvariable=fn_var).grid(row=3, column=1, padx=5, pady=5)

## submit button
ttk.Button(button_frame, text='Submit', command=submit).grid(row=4, column=0)

## GUI - result frame
result_label = ttk.Label(result_frame, text='', style='Title.TLabel')
result_label.grid(row=0, column=0, columnspan=3)

accuracy_label = ttk.Label(result_frame, text='')
accuracy_label.grid(row=1, column=0, pady=10)

precision_label = ttk.Label(result_frame, text='')
precision_label.grid(row=1, column=1, pady=10)

recall_label = ttk.Label(result_frame, text='')
recall_label.grid(row=2, column=0, pady=10)

f1_label = ttk.Label(result_frame, text='')
f1_label.grid(row=2, column=1, pady=10)


input_frame.pack(anchor='center')
result_frame.pack(anchor='center')
button_frame.pack(anchor='center')

root.mainloop()

