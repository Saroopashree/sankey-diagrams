console.log(data);

const dataSource = {
  chart: {
    caption: "Bilateral Trade Between Conutries, 2013",
    subcaption:
      "A Vertical Sankey diagram",
    theme: "fusion",
    orientation: "vertical",    // Try "horizontal"
    linkalpha: 25,              // Try different alpha values to change 
                                // the transparency of the links
    linkhoveralpha: 65,
    nodelabelposition: "start"
  },
  nodes: data.nodes,
  links: data.links,
};

FusionCharts.ready(function () {
  var myChart = new FusionCharts({
    type: "sankey",
    renderAt: "chart",
    width: "100%",
    height: "700",
    dataFormat: "json",
    dataSource
  }).render();
});
