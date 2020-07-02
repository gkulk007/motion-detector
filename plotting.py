from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool

p = figure(x_axis_type='datetime',height=200,width=500,title="Motion Graph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start: ","@Start"),("End: ","@End")])
p.add_tools(hover)

q = p.quad(left=df['Start'], right=df['End'],bottom=0,top=1,color='green')

output_file('Graph.html')
show(p)
