library(googleVis)

URL <- "https://cdn.rawgit.com/christophergandrud/networkD3/master/JSONdata/energy.json"
Energy <- jsonlite::fromJSON(URL)

from <- c()
for (entry in Energy$links$source) {
  from <- c(from, Energy$nodes$name[entry + 1])
}

to <- c()
for (entry in Energy$links$target) {
  to <- c(to, Energy$nodes$name[entry + 1])
}

energy_links <- data.frame(From = from, To = to, Weights = Energy$links$value)

SankeyChart <- gvisSankey(energy_links, from = "From", to = "To", weight = "Weights",
                          options = list(width = 1000, height = 800, 
                                         sankey="{link: {color: {fill: '#959e7e'}}}"))

plot(SankeyChart)

