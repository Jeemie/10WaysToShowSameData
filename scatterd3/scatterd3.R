library(scatterD3)
carata <- read.csv(file="cars-sample.csv", header=TRUE, sep=",")

carata$names <- rownames(carata)
scatterD3(data = cardata, x = Weight, y = MPG,
          xlab = "Weight", ylab = "Mpg",
          col_lab = "Manufacturer",
          col_var = Manufacturer,
          size_var = Weight,
          size_lab = "Weight",
          colors = c('bmw'= '#F8766D', 'ford'= '#A3A500', 'honda'= '#00BF7D',
          'mercedes'= '#00B0F6', 'toyota'= '#E76BF3'),
          point_opacity = 0.5)
