import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import Title
# Source https://bokeh.pydata.org/en/latest/docs/gallery/color_scatter.html

cardata = pd.read_csv('cars-sample.csv')

TOOLS = "hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"
colors = {'bmw': '#F8766D', 'ford': '#A3A500', 'honda': '#00BF7D',
          'mercedes': '#00B0F6', 'toyota': '#E76BF3'}


plot = figure(tools=TOOLS, title = "Weight vs MPG")
plot.add_layout(Title(text="Weight", align="center"), "below")
plot.add_layout(Title(text="MPG", align="center"), "left")

plot.scatter(cardata['Weight'], cardata['MPG'], radius=(cardata['Weight'] / 400) ** 2,
                      fill_alpha=0.5,
                      #color=cardata['Manufacturer'].apply(lambda x: colors[x])
                      #legend = colors.get([cardata['Manufacturer']]),
                      color=cardata['Color']
                      )
output_file("car-plot.html", title="Bokeh-Plot Example")
#legend1 = Legend(items=[("bmw", [plot.circle(x=0, y = 0, fill_color = '#F8766D')])], location = (0,0), orientation="vertical")

show(plot)
