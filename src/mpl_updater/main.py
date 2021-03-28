import argparse
from importlib import reload
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

version = '0.0.1'
url = 'https://github.com/HugoHF/MPL_UPDATER'
help_lu = '''A live updating environment for visualisations via Matplotlib.

usage: live_update([name][t])

arguments:
  name        the name of the program you are working on (<example.py>)
  t           rate at which the widget refreshes in ms (default: 500)

For help, pass h as the program name.

All arguments must be passed as a string or variable.


Explanation: Type 'live_update(<program name>)' to run the updater on your project. Your progress working on that program will then automatically update as you go without having to restart your program.
Your program must contain two functions called 'Animation' and 'Initialization'.
Initialization:
This program is supposed to create the matplotlib.figure.Figure and matplotlib.figure.Axes objects as you would normally in your program. The function is required to return the 'fig' and 'ax' objects.
Animation:
This function has to take an iteration variable (even if unused) as first and the ax object as second argument. In this function you will do whatever you want to have live updated, usually the plotting.'''

help_flu = '''A live updating environment for visualisations via Matplotlib.

usage: fast_live_update([name][t])

arguments:
  name        the name of the program you are working on (<example.py>)
  t           rate at which the widget refreshes in ms (default: 500)

For help, pass h as the program name.

All arguments must be passed as a string or variable.


Explanation: Type 'fast_live_update(<program name>)' to run the updater on your project. Only the lines you changed are reexecuted in the process. Good for large base computations and small changes.

Your progress working on that program will then automatically update as you go without having to restart your program.
Your program must contain two functions called 'Animation' and 'Initialization'.
Initialization:
This program is supposed to create the matplotlib.figure.Figure and matplotlib.figure.Axes objects as you would normally in your program. The function is required to return the 'fig' and 'ax' objects.
Animation:
This function has to take an iteration variable (even if unused) as first and the ax object as second argument. In this function you will do whatever you want to have live updated, usually the plotting.
'''


def updater(name, interval=500):
    print(f"Running \"{name}\" at {interval}ms...")
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

            t = plt.text((xlim[1]-xlim[0])/2, (ylim[1]-ylim[0])/2, e, fontsize=14,
                         style='oblique', ha='center', va='top', wrap=True, bbox=props)

            r = fig.canvas.get_renderer()
            bb = t.get_window_extent(renderer=r)
            width = bb.width
            height = bb.height
            # ax.text(0.05, 0.95, e, transform=ax.transAxes, fontsize=14, horizontalalignment='center', verticalalignment='top', bbox=props)

    ani = FuncAnimation(fig, animate, interval=interval)
    plt.show()

    # EG DAS MIT "RED" FINDET ER NICHT HERAUS

# parser = argparse.ArgumentParser(prog='lu', formatter_class=argparse.RawDescriptionHelpFormatter, usage=argparse.SUPPRESS, description=('''A live updating environment for visualisations via Matplotlib.'''), epilog=('''Explanation: Type \' lu < program name >\' to run the updater on your project. Your progress working on that program will then automatically update as you go without having to restart your program. \nYour program must contain two functions called \'Animation\' and \'Initialization\'.
# Initialization:
# This program is supposed to create the matplotlib.figure.Figure and matplotlib.figure.Axes objects as you would normally in your program. The function is required to return the \'fig\' and \'ax\' objects.
# Animation:
# This function has to take an iteration variable (even if unused) as first and the ax object as second argument. In this function you will do whatever you want to have live updated, usually the plotting. '''))
#
# parser.add_argument('program name', nargs='?', metavar='name', type=str,
#                     help='the name of the program you are working on (<example.py>)')
# parser.add_argument('refresh rate', nargs='?', metavar='t', type=int,
#                     default=500, help='rate at which the widget refreshes')
# args = vars(parser.parse_args())
#
# if args['program name'] != None:
#     updater(args['program name'], args['refresh rate'])


print(
    f'Welcome to the live updater v.{version}.\nFor more information, type mpl_upater.lu(\'h\') or visit {url}')


# Most simple way. Just reload the module
def live_update(name=None, interval=500):
    if name == "h":
        print(help_lu)
    elif name != None:
        updater(name, interval)
        print("Live updater terminated.")
    else:
        print(
            f'usage: lu(program name[, refresh interval]). For help, type lu(\'h\').')


def quick_updater(name, interval=500):
    print(f"Running \"{name}\" at {interval}ms...")
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

            t = plt.text((xlim[1]-xlim[0])/2, (ylim[1]-ylim[0])/2, e, fontsize=14,
                         style='oblique', ha='center', va='top', wrap=True, bbox=props)

            r = fig.canvas.get_renderer()
            bb = t.get_window_extent(renderer=r)
            width = bb.width
            height = bb.height
            # ax.text(0.05, 0.95, e, transform=ax.transAxes, fontsize=14, horizontalalignment='center', verticalalignment='top', bbox=props)

    ani = FuncAnimation(fig, animate, interval=interval)
    plt.show()


def fast_live_update(name=None, interval=500):
    if name == "h":
        print(help_flu)
    elif name != None:
        updater(name, interval)
        print("Live updater terminated.")
    else:
        print(
            f'usage: flu(program name[, refresh interval]). For help, type flu(\'h\').')
