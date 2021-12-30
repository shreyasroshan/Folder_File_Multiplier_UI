import tkinter
from tkinter import filedialog
from tkinter import messagebox
import os
import sys
import shutil
window = tkinter.Tk()
window.title("File_Multiplier")

# file count field

global total_files
total_files = tkinter.IntVar()
label1 = tkinter.Label(window, text = "File_Count").grid(row = 0)
entry1 = tkinter.Entry(window,width=40,textvariable=total_files)
entry1.grid(row = 0, column = 3)

# input_path field

def inputpath():
    global source
    source = filedialog.askdirectory()
    entry2.delete(0,tkinter.END)
    entry2.insert(tkinter.END,source)
    return source

def outputpath():
    global destination
    destination = filedialog.askdirectory()
    entry3.delete(0,tkinter.END)
    entry3.insert(tkinter.END,destination)
    messagebox.showinfo("Check","Make sure the folder selected in output path is empty before Generating")
    return destination 

label2 = tkinter.Label(window, text = "Input_Path").grid(row = 2)
browse1 = tkinter.Button(window,text="Browse",command=inputpath)
browse1.grid(row = 2, column = 5)
entry2 = tkinter.Entry(window,width=40)
entry2.grid(row = 2, column = 3)

# output_path field

label3 = tkinter.Label(window, text = "Output_Path").grid(row = 4)
browse2 = tkinter.Button(window,text="Browse",command=outputpath)
browse2.grid(row = 4, column = 5)
entry3=tkinter.Entry(window,width=40)
entry3.grid(row = 4, column = 3)

# generate button

def finalprocess():
   
    # file name checker
    
    input_path = os.listdir(source)
    input_path = [input_path[i].split('.')[0] for i in range(len(input_path))]
    for i in range(len(input_path)-1):
        if int(input_path[i+1])-int(input_path[i]) == 1 and i+1 < len(input_path):
            None
        else:
            print("Check file named "+input_path[i+1])
            sys.exit()
            
    # number of sets checker
    
    global total_files
    total_files = total_files.get()
    if (total_files % len(input_path) > 0): 
        number_of_sets = (total_files // len(input_path)) + 1
    else:
        number_of_sets = (total_files // len(input_path))
    set_nos = ["Set"+str(i) for i in range(2,number_of_sets+1)]
    
    # creating set folders inside the destination folder and pasting files in the folders created

    if os.path.exists(destination):
        shutil.rmtree(destination)
        os.makedirs(destination)
    else:
        os.makedirs(destination)
    global count   
    count = len(input_path)+1
    def createFolder(folder_name,path):
        global count
        try:
            if os.path.exists(path):
                os.makedirs(path+folder_name)
                if os.path.exists(path+folder_name):
                    for i in range(len(input_path)):
                        if count <= total_files:
                            shutil.copy(os.path.join(source,os.listdir(source)[i]),path+folder_name,follow_symlinks=True)
                            new_set_name = str(count)+'.'+(os.listdir(source)[i].split('.'))[1]
                            os.rename(path+folder_name+'\\'+os.listdir(source)[i],path+folder_name+'\\'+new_set_name)
                            count+=1                    
        except OSError:
            print ('Error: Creating directory. ' +  path)
    
    for i in range(len(set_nos)):
        set_name = "\\"+set_nos[i]
        createFolder(set_name,destination)
    
    # duplicating Set1 files from source to destination's Set1
    
    shutil.copytree(src=source,dst=destination+'\\Set1',copy_function=shutil.copy)
    
    messagebox.showinfo("Success","Process Done :)")

generate = tkinter.Button(window,text="Generate",command=finalprocess)
generate.grid(row = 6, column = 3)

tkinter.mainloop()