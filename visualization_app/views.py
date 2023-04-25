#from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import gc
import os.path
import os
import math
from django.conf import settings


def delete_image():
    try:
        path = os.path.join(settings.MEDIA_ROOT, 'image/image.svg')
        if os.path.isfile(path):
            os.remove(os.path.join(settings.MEDIA_ROOT, 'image/image.svg'))
            print('old image deleted')
    except Exception as e:
        print(str(e), ' \nerror in delete_image')

def read_dataset(num):
    print('dataset read start')
    dataset = pd.read_csv('https://media.githubusercontent.com/media/M-Umr1/datasets/master/Processed_BigDataset_for_Visualization.csv', nrows=num)
    print('Dataset read end\n')
    return dataset

def prepare_dateset(df):
    df['time_stamp'] = pd.to_datetime(df['time_stamp'])
    # df.set_index(['time_stamp'],inplace=True)
    print('Dataset is prepared\n')
    return df

def visualize_df(df):
    print('visualization starts')
    unique_function = df.Function.unique()
    
    # Define the number of rows and columns for the subplots
    num_plots = len(unique_function)
    cols = 3
    rows = math.ceil(num_plots / cols)

    # Calculate the figure size based on the number of rows and columns
    fig_width = 22
    fig_height = rows * 6
    fig_size = (fig_width, fig_height)

    # Create the figure and subplots
    fig, axes = plt.subplots(rows, cols, figsize=fig_size)

    # Iterate over the unique functions and plot on the corresponding subplot
    for i, func in enumerate(unique_function):
        subset = df[df["Function"] == func]
        row = i // cols
        col = i % cols
        axes[row, col].plot(subset["time_stamp"], subset["Time"])
        axes[row, col].set_title(func, fontsize=15)
        axes[row, col].set_xlabel('time_stamp', fontsize=10)
        axes[row, col].set_ylabel('Time', fontsize=10)

    # Hide any extra subplots that aren't being used
    for i in range(num_plots, cols * rows):
        row = i // cols
        col = i % cols
        axes[row, col].set_visible(False)

    # Adjust the spacing and layout of the subplots
    # plt.tight_layout()

    # Adjust the spacing between the subplots
    fig.subplots_adjust(hspace=0.5)

    # Rotate the xticks by 45 degrees
    for ax in axes.flat:
        for label in ax.get_xticklabels():
            label.set_rotation(45)

    # plt.savefig('./visualization_app/templates/image/image.svg', bbox_inches = 'tight', pad_inches = 0)
    plt.savefig(os.path.join(settings.MEDIA_ROOT, 'image/image.svg'), bbox_inches = 'tight', pad_inches = 0)

    # Close the plot and release memory
    plt.close()
    print('visualization end')



def home(request):
    num_of_rows = None
    if request.method == 'POST':
        num_of_rows = request.POST.get('number_of_rows','')
        print('you have enter number of rows: ',num_of_rows)
    # df = pd.DataFrame()
    try:
        if num_of_rows is not None:
            delete_image()
            df = read_dataset(int(num_of_rows))
            df = prepare_dateset(df)
            visualize_df(df)
    except Exception as e:
        print(str(e))
    
    # return render(request, 'index.html')
    # image_path = './visualization_app/templates/image/image.svg'
    image_path = os.path.join(settings.MEDIA_ROOT, 'image/image.svg')
    print(image_path)
    image_exists = os.path.isfile(image_path)
    print(type(image_exists), '     ', image_exists)
    
    return render(request, 'index.html', {'image_exists': image_exists})
    #return HttpResponse("Hello, Django!")
    # return render(request, 'index.html')

def main_home(request):
    pass