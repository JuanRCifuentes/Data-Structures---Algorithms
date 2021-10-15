from bokeh.plotting import figure
from bokeh.models import Range1d
from bokeh.io import export_svg
import math

if __name__ == "__main__":
    # ------------------------- SUPPORT FUNCTIONS -------------------------

    def setPlotStyle(plot):
        plot.x_range = Range1d(0, 200)
        plot.y_range = Range1d(0, 500)

        plot.title.text_font_size = '25pt'

        plot.xaxis.major_tick_line_color = None  # turn off x-axis major ticks
        plot.xaxis.minor_tick_line_color = None  # turn off x-axis minor ticks

        plot.yaxis.major_tick_line_color = None  # turn off y-axis major ticks
        plot.yaxis.minor_tick_line_color = None  # turn off y-axis minor ticks

        plot.xaxis.major_label_text_font_size = '0pt'  # turn off x-axis tick labels
        plot.yaxis.major_label_text_font_size = '0pt'  # turn off y-axis tick labels

        plot.xaxis.major_label_text_color = None  # turn off x-axis tick labels leaving space
        plot.yaxis.major_label_text_color = None  # turn off y-axis tick labels leaving space

        plot.yaxis.axis_label = '# Operations'
        plot.yaxis.axis_label_text_font_size = '25px'
        plot.xaxis.axis_label = 'Input size'
        plot.xaxis.axis_label_text_font_size = '25px'

    def setONotationStyle(plot):
        plot.x_range = Range1d(0, 500)
        plot.y_range = Range1d(0, 500)

        plot.xaxis.major_tick_line_color = 'black'  # turn off x-axis major ticks
        plot.yaxis.major_tick_line_color = 'black'  # turn off y-axis major ticks

        plot.xaxis.major_label_text_font_size = '20pt'  # turn off x-axis tick labels
        plot.yaxis.major_label_text_font_size = '20pt'  # turn off y-axis tick labels

        plot.xaxis.major_label_text_color = 'black'  # turn off x-axis tick labels leaving space
        plot.yaxis.major_label_text_color = 'black'  # turn off y-axis tick labels leaving space

    def drawLines(fig, lines, x_vals):
        for currentLine in lines:
            fig.line( x_vals, 
                currentLine["values"], 
                line_width=3, 
                line_color=currentLine["color"], 
                legend_label=currentLine["label"]
            )

    # ------------------------- PLOT FUNCTIONS -------------------------

    # FIRST PLOT - BIG O NOTATION
    def bigOPlot(total_vals = 500):
        fig = figure(plot_width=total_vals, plot_height=total_vals, title="Big O Notation")
        setPlotStyle(fig)
        fig.y_range = Range1d(-3, 500)

        x_vals = list(range(0, total_vals))

        # Each element is a line, which is a function representing a bigO complexity, it has three values:
        # 1. label: The bigO notation as a String.
        # 2. values: List of y-values to plt the line. The lists are being populated by comprehensions around x_values list.
        # 3. color: The color of the line in the plot as a String.
        lines = [
            { "label": "O(1)",          "values": [-1 for val in x_vals],                         "color": "blue"     },
            { "label": "O(log(n))",     "values": [2 * math.log(val+0.01) for val in x_vals],     "color": "#639754"  },
            { "label": "O(n)",          "values": [val for val in x_vals],                        "color": "#FFD301"  },
            { "label": "O(n log(n))",   "values": [val * math.log(val+0.01) for val in x_vals],   "color": "orange"   },
            { "label": "O(n^2)",        "values": [val**2 for val in x_vals],                     "color": "#E03C32"  },
            { "label": "O(n!)",         "values": [math.factorial(val) for val in x_vals],        "color": "black"    },
            # { "label": "O(n^n)",        "values": [val**val for val in x_vals],                   "color": "red"      }
        ]

        # Adds the lines to the plot with it's properties (defined above)
        drawLines(fig, lines, x_vals)

        export_svg(fig, filename="BIG O/Images/bigO-notation.svg")

    # SECOND PLOT - O(n)
    def bigOnPlot(total_vals=500):
    
        fig = figure(plot_width=500, plot_height=500, title="O(n) - findNemo()")
        
        setPlotStyle(fig)
        setONotationStyle(fig)

        x_vals = list(range(0, total_vals))

        lines = [
            { "label": "O(n)", "values": [val for val in x_vals], "color": "black" }
        ]

        drawLines(fig, lines, x_vals)

        points = {
            "x_values": [50, 150, 250, 450],
            "y_values": [50, 150, 250, 450]
        }

        fig.circle(points["x_values"], points["y_values"], size=20, color="navy")

        fig.legend.location = 'top_left'

        export_svg(fig, filename="BIG O/Images/o(n).svg")
    
    # THIRD PLOT - O(1)
    def bigO1Plot(total_vals=500):
    
        fig = figure(plot_width=500, plot_height=500, title="O(1) - print1Name()")
        
        setPlotStyle(fig)
        setONotationStyle(fig)
        fig.y_range = Range1d(0, 5)

        x_vals = list(range(0, total_vals))
        
        lines = [
            { "label": "O(1)", "values": [1 for val in x_vals], "color": "black" }
        ]

        drawLines(fig, lines, x_vals)

        points = {
            "x_values": [50, 150, 250, 450],
            "y_values": [1, 1, 1, 1]
        }

        fig.circle(points["x_values"], points["y_values"], size=20, color="navy")

        export_svg(fig, filename="BIG O/Images/o(1).svg")

    # DRAW EVERY PLOT ON A COLUMN
    c = [bigOPlot(), bigOnPlot(), bigO1Plot()]