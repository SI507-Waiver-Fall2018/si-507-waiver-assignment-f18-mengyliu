# Mengyao Liu
# mengyliu
# Imports -- you may add others but do not need to
import plotly.plotly as py
import plotly.graph_objs as go
import plotly


# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets
plotly.tools.set_credentials_file(username='junedull', api_key='jP3YKkAzpniXfJTFXXs3')
data=[]
nouns=[]
frequencys = []
with open('noun_data.csv', 'rb') as csvfile:
	lines = [x.decode('utf8').strip() for x in csvfile.readlines()]
	
for line in lines[1:]:
    noun, frequency = line.split(",")
    nouns.append(noun)
    frequencys.append(int(frequency))
	

data = [go.Bar(x = nouns,y = frequencys)]
# py.iplot(fig, filename='part4_viz_image.png')
py.image.save_as(data, filename='part4_viz_image.png')
csvfile.close()