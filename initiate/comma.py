import pandas as pd
import csv

data = pd.read_csv('250imdbtool.txt', sep=";", encoding = "ISO-8859-1")
#data=data.fillna(0)

columnsList = ['country', 'genre', 'director','title','imdbVotes', 'language', 'poster','actors'] 

for col in columnsList:

    data[col] =  data[col].apply(lambda x: "\"" + str(x) + "\"" )


#data["runtime"]=data["runtime"].replace(" min","")

data.to_csv('temp.txt', sep=';', index=False, quoting=csv.QUOTE_NONE, encoding = "ISO-8859-1")


