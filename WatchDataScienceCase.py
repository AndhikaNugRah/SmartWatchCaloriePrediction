#Import Library & Data
import pandas as pd
import numpy as np
data = pd.read_csv('WatchDataCase.csv',header=0,sep=",")
print(data.describe())
print(data)

#Data Cleaning (wrongly and unregistered values)
data.dropna(axis=0,inplace=True)
print(data.info())

#convert data type object into float64
data['Max_Pulse'] = data ['Max_Pulse'].astype(float)
print(data.info())
print(data.describe())

#watch out data that potentially lead to wrong results
print(data)
print(data['Hours_Work'].mean())
print(data['Hours_Work'].median())

data.loc[data['Hours_Work']==0, 'Hours_Work']=data['Hours_Work'].median()
print(data)

#plotting data
import matplotlib.pyplot as plt

#using heatmap for better understanding
import seaborn as sns 

#Find out Correlation Matrix
Cor_max=round(data.corr(),2)
print(Cor_max)

correlation_data = data.corr()
axis_corr = sns.heatmap(
correlation_data,
vmin=-1, vmax=1, center=0,
cmap=sns.diverging_palette(50, 500, n=500),
square=True
)
axis_corr.set_title("Data Correlation Matrix")
plt.show()

#Plotting to better visualization data corrrelations
data.plot(x='Average_Pulse',y='Calorie_Burnage',kind='line')
plt.xlabel='Average Pulse'
plt.ylabel='Calorie Burnage'
plt.title('Relation between Average Pulse and Calorie')

#min is taken based on information on describe 
plt.xlim(xmin=80)
plt.ylim(ymin=240)
plt.show()

#Second Plotting
data.plot(x='Max_Pulse',y='Calorie_Burnage',kind='line')
plt.xlabel='Max Pulse'
plt.ylabel='Calorie Burnage'
plt.xlim(xmin=120,xmax=150)
plt.ylim(ymin=240,ymax=330)
plt.title('Relation between Max Pulse and Calorie')
plt.show()

#Third Plotting
data.plot(x='Hours_Sleep',y='Calorie_Burnage',kind='line')
plt.xlabel='Hours Sleep'
plt.ylabel='Calorie Burnage'
plt.xlim(xmin=7,xmax=8)
plt.ylim(ymin=240,ymax=330)
plt.title('Relation between Hours Sleep and Calorie')
plt.show()

#We can conclude that the most factor affect the calorie burnage based on data is average_pulse

#find out slope and intercept to find out formula to find calorie burnage based on average pulse input
x=data['Average_Pulse']
y=data['Calorie_Burnage']
slope_intercept = np.polyfit(x,y,1)
print(slope_intercept)
#got 2 for slope and 80 for intercept 

#function for prediction :
import tkinter as tk
from tkinter import messagebox
def predict(x):
    return 2*x+80

def calculate():
    try:
        x_value = int(entry.get())
        prediction = predict(x_value)
        result_label.config(text=f"We can understand the calorie burnage will be: {prediction}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a whole number.")

def quit_program():
    messagebox.showinfo(f"Exit","Thanks for using our service! -Dhika")
    print("Thanks for Using our Service! -Dhika")
    window.destroy()

window = tk.Tk()
window.title("Calorie Burnage Calculator")

label = tk.Label(window, text="Input your average pulses:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Calculate", command=calculate)
button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

quit_button = tk.Button(window, text="Quit", command=quit_program)
quit_button.pack()

window.mainloop()