library(plotly)

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

cardata <- read.csv('cars-sample.csv', header=TRUE)

plot_ly(cardata, x = ~Weight, y = ~MPG, text = ~Manufacturer, type = 'scatter', size=~Weight, 
        fillcolor = ~Manufacturer, mode = 'markers', 
             marker = list(color = ~Color, opacity = 0.5)) %>%
  layout(title = 'Weight vs MPG')