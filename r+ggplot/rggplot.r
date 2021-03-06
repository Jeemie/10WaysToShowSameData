library(ggplot2)

#found on google. Yay google. Use this if you select 
#"Source on Save" 
#this.dir <- dirname(parent.frame(2)$ofile)
#setwd(this.dir)

#use this if you just "run" the script
#you use rstudioapi
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

cardata <- read.csv('cars-sample.csv', header=TRUE)
ggplot(cardata, aes(x=Weight, y=MPG)) + geom_point(aes(color=Manufacturer, size=Weight), alpha=0.5)



