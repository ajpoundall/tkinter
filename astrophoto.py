from hashlib import new
from tkinter import * #imports modules
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime
import shutil
import os

#function used to find initial photo location
def first_dir():
    dir_name = filedialog.askdirectory()
    new_dir.set(dir_name)

def second_dir():
    dir_name = filedialog.askdirectory()
    data_dir.set(dir_name)


#This function looks at the list of files and works out what the earliest date is, this will be utilised to create the next file
#in the folder structure
def obs_date(data): 
    string_dates = []
    for x in data:
        if x [:2] == "L_":
            cleaned_date = x[2:12]
            string_dates.append(cleaned_date)
        else:
            pass
    list_of_dates= [datetime.strptime(date,"%Y-%m-%d") for date in string_dates]
    start_date = min(list_of_dates).strftime("%Y-%m-%d")
    return str(start_date)
    
def clean_data():
    data = data_dir.get() #get data from variables below
    list_of_files =[]
    for x in os.listdir(data):
        observing_date= ""   
        filename = os.fsdecode(x)
        if filename.endswith(".fit"):
            list_of_files.append(filename)           
        else: 
            os.remove(data+"/"+x)
    return list_of_files

def create_folders(date):
    folders = ["Lights", "Flats", "Dark Flats", "Darks", "Bias"]
    date_folder = date
    print(date_folder)
    new_folder_location = new_dir.get()
    #check to see if any folders are in directory, if empty create folder
    if len(os.listdir(new_folder_location) ) == 0: 
        os.mkdir(new_folder_location+"/"+date_folder)
        for folder_names in folders:
            os.mkdir(new_folder_location+"/"+date_folder+"/"+folder_names)
    #If folder is not empty, check all folder titles to confirm if folder already exists
    else:
        for x in os.listdir(new_folder_location):
            if x == date_folder:
                print ("error")
            else:
                os.mkdir(new_folder_location+"/"+date_folder)
                for folder_names in folders:
                    os.mkdir(new_folder_location+"/"+date_folder+"/"+folder_names)

def copy_files(clean_data, date):
    file_list = clean_data
    date_folder = date
    new_folder_location = new_dir.get()
    source = data_dir.get()
    for file in file_list:
        print (file)
        if file[:2] == "L_":
            print (file)
            shutil.copy(source+"/"+file, new_folder_location+"/"+date_folder+"/Lights")
        #else:
         #   return



def main_function():
    #clean the data files
    cleaned_data = clean_data()
    #find the date of observation
    date_of_observing = obs_date(cleaned_data)
    #create folder strucutre and check for duplicates
    create_folders(date_of_observing)
    #copy files over
    copy_files(cleaned_data, date_of_observing)

#start of tkinter
root = Tk()
root.title("Astro Photo File")
root.option_add('*tearOff', FALSE)
frm = ttk.Frame(root, padding="3 3 12 12")
frm.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#variables
new_dir =  StringVar()
data_dir = StringVar()

#buttons and forms
ttk.Button(frm, text="Create New Data Set", command=first_dir).grid(column=2, row=1, sticky=W)
ttk.Label(frm, textvariable=new_dir).grid(column=4, row=1, sticky=E)
ttk.Button(frm, text="Confirm Data to Sort", command=second_dir).grid(column=2, row=2, sticky=W)
ttk.Label(frm, textvariable=data_dir).grid(column=4, row=2, sticky=E)
ttk.Button(frm, text="Organise Files", command=main_function).grid(column=2, row=3, sticky=W)






root.mainloop() #end of programme
