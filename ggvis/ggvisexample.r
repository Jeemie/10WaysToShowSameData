library(ggvis)
cardata <- read.csv(file="cars-sample.csv", header=TRUE)


cardata %>%
  ggvis(~Weight, ~MPG) %>% 
   layer_points(size := ~factor(Weight/10),fill = ~factor(Manufacturer), opacity:=1/2) %>%
  scale_nominal("fill", range = c('#F8766D','#A3A500','#00BF7D','#00B0F6','#E76BF3'))