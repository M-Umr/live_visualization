#from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gc
import os.path
import os



def read_dataset(num):
    dataset = pd.read_csv('https://media.githubusercontent.com/media/M-Umr1/datasets/master/Processed_BigDataset_for_Visualization.csv', nrows=int(num))

    return dataset

def prepare_dateset(df):
    df['time_stamp'] = pd.to_datetime(df['time_stamp'])
    df.set_index(['time_stamp'],inplace=True)

    return df

def visualize_df(df):
    path = './visualization_app_templates/image/image.svg'
    if os.path.isfile(path):
        os.remove("./visualization_app_templates/image/image.svg")
    
    unique_function = df.Function.unique()
    length_functions = len(unique_function)
    if length_functions%2 == 0:
        figure_col_size = 10*(length_functions//2)
        plt.figure(figsize=(22, figure_col_size+80))
    elif length_functions%2 != 0:
        figure_col_size = 10*(length_functions//2)
        plt.figure(figsize=(22, figure_col_size+90))

    ncols = 3
    # calculate number of rows
    nrows = length_functions-1

    for n, each_function in enumerate(unique_function):
    
        # add a new subplot iteratively
        ax = plt.subplot(nrows, ncols, n+1)
        # filter df and plot ticker on the new subplot axis
        df[df["Function"] == each_function].plot(ax=ax)
            # chart formatting
        ax.set_title(each_function, fontsize=15)
        ax.set_xlabel('time_stamp', fontsize=10)
        ax.set_ylabel('Time', fontsize=10)

        plt.xticks(rotation=45)
        plt.savefig('./visualization_app_templates/image/image.svg', 
                    bbox_inches = 'tight', pad_inches = 0)



def home(request):
    #return HttpResponse("Hello, Django!")
    var = None
    if request.method == 'POST':
        var = request.POST.get('number_of_rows','')
    # df = pd.DataFrame()
    try:
        if var is not None:
            df = read_dataset(int(var))
            df = prepare_dateset(df)
            visualize_df(df)
    except Exception as e:
        print(str(e))
    
    return render(request, 'index.html')

def main_home(requests):
    