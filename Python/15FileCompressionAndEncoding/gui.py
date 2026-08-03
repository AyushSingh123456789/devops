import tkinter as tk
from compressmodule import compress, decompress
from tkinter import filedialog 
#allows to open files on PC
def compression(i,o):
    compress(i,o)
    
def decompression(i,o):
    decompress(i,o)
    
def open_file():
    filename = filedialog.askopenfilename(initialdir='/',title="Select a file to compress: ") #filename gets the path  
    return filename

def open_file2():
    filename2 = filedialog.askopenfilename(initialdir='/',title="Select a file to decompress: ")
    return filename2
    
window = tk.Tk()
window.title("Compression Engine")
window.geometry("600x400")

# input_entry = tk.Entry(window)
# output_entry = tk.Entry(window)

# input_entry2 = tk.Entry(window)
# output_entry2 = tk.Entry(window)

# input_label = tk.Label(window,text="File to be compressed: ")
# output_label = tk.Label(window,text="The compressed file: ")

# input_label2 = tk.Label(window,text="The Compressed file: ")
# output_label2 = tk.Label(window,text="The Decompressed file: ")

# compress_button = tk.Button(window,text="Compress",command=lambda:compression(input_entry.get(),output_entry.get()))
compress_button = tk.Button(window,text="Compress",command=lambda:compression(open_file(),"compressed_output1.txt"))
# to fetch real-time values, we add the lambda function
decompress_button = tk.Button(window,text="Decompress",command=lambda:decompress(open_file2(),"decompressed_output1.txt"))

# input_label.grid(row=0,column=0)
# input_entry.grid(row=0,column=1)
# output_label.grid(row=1,column=0)
# output_entry.grid(row=1,column=1)
compress_button.grid(row=2,column=1)
# input_label2.grid(row=3,column=0)
# input_entry2.grid(row=3,column=1)
# output_label2.grid(row=4,column=0)
# output_entry2.grid(row=4,column=1)
decompress_button.grid(row=5,column=1)

window.mainloop()