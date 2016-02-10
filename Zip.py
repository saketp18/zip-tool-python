from Tkinter import *
import Tkinter as tk
from tkFileDialog import askdirectory
import ttk
import os 
import zipfile
import tarfile


def center_window(width, height):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

	
def open_file_dialog():
	filename = askdirectory()
	e1.delete(0,END)
	e1.insert(0,filename)
	
def ziping_file():
	outputFileName = e1.get()+'.zip'
	zipf = zipfile.ZipFile(outputFileName, 'w')
	zipdir(e1.get(),zipf)
	zipf.close()
	e2.delete(0,END)
	e2.insert(0,outputFileName)
		
def zipdir(path, ziph):
	for root, dirs, files in os.walk(path):
		for file in files:
			ziph.write(os.path.join(root,file))
			
def extract_file():
	outputFileName = e1.get()
	zfile = zipfile.ZipFile(e1.get())
	zfile.extractall("\\")
	e2.delete(0,END)
	e2.insert(0,outputFileName.replace('.zip', ''))

def tar_zipper():
	outputFileName = e1.get()+".tar.gz"
	tar = tarfile.open(outputFileName, "w:gz")
	tar.add(e1.get(), arcname="TarName")
	tar.close()
	e2.delete(0,END)
	e2.insert(0,outputFileName)
		
	
if __name__ == '__main__':
	
	
	root = tk.Tk()
	center_window(800,260)
	root.title("File Zipper")
	root.resizable(width=False, height=False)
	
	Label(root, text="File").grid(row=0)
	Label(root, text="Output Location").grid(row=1)

	e1 = Entry(root, width =80)
	e2 = Entry(root,width =80)
	e1.pack(expand=True)
	e2.pack(expand=True)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	
	browseButton = Button(root,width=10, height=1,text='Browse', command=open_file_dialog).grid(row=0, column=4, sticky=W, pady=4)
	zipButton = Button(root, width=10, height=1, text='.zip Format', command=ziping_file).grid(row=2, column=0, sticky=W, pady=4)
	unzipButton = Button(root, width=10, height=1, text='.zip Extract', command=extract_file).grid(row=2, column=1, sticky=W, pady=4)
	tarzipButton = Button(root, width=10, height=1, text='.gz/tar Format', command=tar_zipper).grid(row=3, column=0, sticky=W, pady=4)
	quitButton = Button(root, width=10, height=1, text='Quit', command=root.quit).grid(row=1, column=4, sticky=W, pady=4)	
	root.mainloop()