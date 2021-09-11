import tkinter as tk

fields = 'Expiry Date Title', 'Notification Days', 'Output Columns', 'Receiver Mail'

def fetch(entries):
    global data
    data = []
 
    for entry in entries:
        #field = entry[0]
        text  = entry[1].get()
        #print('%s: "%s"' % (field, text))
        data.append(text)   

def getdata():
    return data
    
        

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

def main_func():
    root = tk.Tk()
    root.title("Vehicle Access Card Notification Reminder")
    root.geometry("400x200")
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = tk.Button(root, text='Submit',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()




   
