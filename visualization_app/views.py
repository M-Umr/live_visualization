#from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gc

def read_dataset(num):
    dataset = pd.read_csv('https://media.githubusercontent.com/media/M-Umr1/datasets/master/Processed_BigDataset_for_Visualization.csv', nrows=int(num))
    is_read = 1
    number_of_rows_read = num
    return dataset, is_read, number_of_rows_read


def home(request):
    #return HttpResponse("Hello, Django!")
    var = None
    if request.method == 'POST':
        var = request.POST.get('number_of_rows','')
    # df = pd.DataFrame()
    try:
        if var is not None:
            df, is_read, number_of_rows_read = read_dataset(int(var))

            print(df.head(5))
    except Exception as e:
        print(str(e))
    return render(request, 'index.html')