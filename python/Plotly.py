import requests
from plotly import graph_objs
import random 

results = requests.get("https://cdn.rawgit.com/christophergandrud/networkD3/master/JSONdata/energy.json")

data = results.json()

names = list()                      # Names of nodes present in the network
for entry in data['nodes'] :
  names.append(entry['name'])

source = list()                     # List to store Source Nodes id's
target = list()                     # List to store Target Nodes id's
weights = list()                    # Weights of links between nodes
for entry in data['links'] :
  source.append(entry['source'])
  target.append(entry['target'])
  weights.append(entry['value'])

colors = ["#"+
            ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
         for i in range(len(source))]                   # Generate random colors for the nodes

fig = graph_objs.Figure(data=[graph_objs.Sankey(
    node = dict(
      thickness = 15,
      line = dict(color = "black", width = 1.5),
      label = names,
      color = colors
    ),
    link = dict(
      source = source,
      target = target,
      value = weights
  ))],
  layout_title_text="Energy Flow Network")

fig.show(renderer="browser")