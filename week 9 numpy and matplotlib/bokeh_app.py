from bokeh.layouts import column
from bokeh.models import Slider, ColumnDataSource
from bokeh.plotting import curdoc, figure,show
import numpy as np

# Set up initial data and plot
x = np.linspace(0, 10, 500)
y = np.sin(x)
source = ColumnDataSource(data={'x': x, 'y': y})
plot = figure()
plot.line('x', 'y', source=source)

# Define the callback function
def update_data(attrname, old, new):
    freq = frequency_slider.value
    new_data = {'x': x, 'y': np.sin(freq * x)}
    source.data = new_data

# Create a slider and link it to the callback
frequency_slider = Slider(start=0.1, end=5, value=1, step=0.1, title="Frequency")
frequency_slider.on_change('value', update_data)

# Create a layout
layout = column(plot, frequency_slider)

# Add the layout to the current document
curdoc().add_root(layout)
show(plot)
