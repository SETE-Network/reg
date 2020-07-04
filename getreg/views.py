from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from glob import glob
import pandas as pd
import os
import wget

from django.core.files.storage import FileSystemStorage


class Home(TemplateView):
    template_name = "home.html"

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')

def button(request):

    return render(request,'home.html')

def output(request):


    #df = pd.read_csv('pythonses.csv')

    for f in glob('media/*.csv'):
        df = pd.read_csv(f)

    #print(df['Username'])

    #df['disucssion total'] = df.iloc[:, 10:15].mean(axis=1)

    df['disucssion total'] = df.loc[:, (df.columns.str.startswith('Discussion 1')) + 
                            (df.columns.str.startswith('Discussion 2')) + 
                            (df.columns.str.startswith('Discussion 3')) + 
                            (df.columns.str.startswith('Discussion 4')) + 
                            (df.columns.str.startswith('Discussion 5'))].mean(axis=1)

    #selected_column = df[["Username", "disucssion total", "Username", "Annotated Bibliography [Total Pts: 100 Score] |353516","Username", "Research Introduction and background [Total Pts: 100 Score] |353517"]]

    selected_column = df.loc[:, (df.columns.str.startswith('Username')) + 
                            (df.columns.str.startswith('disucssion total')) + 
                            (df.columns.str.startswith('Research Introduction and background')) + 
                            (df.columns.str.startswith('Research Finding (Body)')) + 
                            (df.columns.str.startswith('Research Paper Final Draft')) +  
                            (df.columns.str.startswith('Research Presentation')) + 
                            (df.columns.str.startswith('participation'))]

    #df.loc[:, df.columns.str.startswith('Annotated Bibliography')],
    #df.loc[:, df.columns.str.startswith('Research Finding')],
    #df.loc[:, df.columns.str.startswith('Research Paper Final Draft')],
    #df.loc[:, df.columns.str.startswith('Research Presentation')],
    #df.loc[:, df.columns.str.startswith('participation')]

    new_df = selected_column.copy()


    #new_df[new_df.columns[5]] = selected_column.copy()
    new_df.insert(2, 'Username2', new_df['Username'])
    new_df.insert(4, 'Username3', new_df['Username'])
    new_df.insert(6, 'Username4', new_df['Username'])
    new_df.insert(8, 'Username5', new_df['Username'])
    new_df.insert(10, 'Username6', new_df['Username'])

    print(new_df)

    new_df.to_csv('output/rg-ready.csv', index=False)

    


    print('Beginning file download with wget module')

    url = 'output/rg-ready.csv'
    wget.download(url, '/Users/peterc/Downloads/reg-ready.csv')



    for f in glob('media/*.csv'):
      os.remove(f)


    # In[ ]:

    
    return render(request,'upload.html')

    