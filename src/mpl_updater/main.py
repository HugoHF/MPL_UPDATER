import argparse
from importlib import reload
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def lu(name, interval):
    print(name, interval)
    mod = __import__(name)

    fig, ax = mod.Initialization()

    def animate(i):
        reload(mod)
        ax.clear()
        try:
            mod.Animation(i, ax)
        except Exception as e:
            xlim = ax.get_xlim()
            ylim = ax.get_ylim()
            props = dict(boxstyle='round', facecolor='wheat', alpha=1)

            t = plt.text((xlim[1]-xlim[0])/2, (ylim[1]-ylim[0])/2, e, fontsize=14, style='oblique', ha='center', va='top', wrap=True, bbox=props)

            r = fig.canvas.get_renderer()
            bb = t.get_window_extent(renderer=r)
            width = bb.width
            height = bb.height
            # ax.text(0.05, 0.95, e, transform=ax.transAxes, fontsize=14, horizontalalignment='center', verticalalignment='top', bbox=props)

    ani = FuncAnimation(fig, animate, interval=interval)
    plt.show()

    # EG DAS MIT "RED" FINDET ER NICHT HERAUS



parser = argparse.ArgumentParser(prog='lu',
    description='A live updating environment for visualisations via Matplotlib.', epilog='usage: Type \' lu <program name>\' to open the live updating graphing widget. Your program must contain two functions called \' Animation \' and HIER WEITERSCHRIEBEN')


parser.add_argument('program name', metavar='n', type=str, help='the name of the program you are working on (<example.py>)')
parser.add_argument('refresh rate', nargs='?', metavar='t', type=int, default=500, help='rate at which the widget refreshes')

parser.print_help()
args = vars(parser.parse_args())

lu(args['program name'], args['refresh rate'])
