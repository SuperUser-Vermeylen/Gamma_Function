import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
# from matplotlib import rc


def height(a, n):
    return a**n*np.exp(-a)


def update(val):
    plt.sca(ax)
    n_value = np.around(s_n.val, 2)
    area = s_area.val
    area_x = np.arange(0, area, 0.01)
    area_y = height(area_x, n_value)
    calculateArea = np.trapz(area_y, dx=0.01)
    plt.title('Approximate Factorial {:.2f}! = '.format(n_value) + str(np.around(calculateArea, decimals=2)))
    for collection in ax.collections:
        if str(collection.get_label()) == "factorial":
            collection.remove()
    plt.fill_between(area_x, area_y, color='#b953cd', label="factorial")
    l.set_ydata(t**n_value*np.exp(-t))
    fig.canvas.draw_idle()
    

if __name__ == "__main__":

    fig, ax = plt.subplots()
    plt.ylim(top=500000)
    plt.subplots_adjust(left=0.15, bottom=0.25)
    plt.margins(x=0)
    # rc('font', **{'family': 'serif', 'serif': ['Palatino']})
    # rc('$\Gamma(\mathscr{t})$ = $\int_0^\infty \mathscr{x}^{\mathscr{t}-1} e^{-\mathscr{x}}$', usetex=True)
    ax.text(80, 450000, r'$\Gamma(\mathscr{t})$ = $\int_0^\infty \mathscr{x}^{\mathscr{t}-1} e^{-\mathscr{x}}$',
            fontsize=15)

    t = np.arange(0, 100, 0.01)
    print(t)
    s = t**3*np.exp(-t)
    l, = plt.plot(t, s, lw=2, color='k')

    x = np.arange(0, 10.00, 0.01)
    y = height(x, 3.00)

    calculate_Area_initial = np.trapz(y, dx=0.01)
    plt.title('Approximate Factorial {:.2f}! = '.format(3.00) + str(np.around(calculate_Area_initial, decimals=2)))
    plt.fill_between(x, y, color='#b953cd', label="factorial")

    ax_nColor = '#cd5353'
    ax_areaColor = '#cd5353'

    ax_n = plt.axes([0.15, 0.1, 0.75, 0.03], facecolor=ax_nColor)
    ax_area = plt.axes([0.15, 0.15, 0.75, 0.03], facecolor=ax_areaColor)

    s_n = Slider(ax_n, 'n', 0, 20, valinit=3.00, valstep=0.01)
    s_area = Slider(ax_area, 'Area', 0, 100, valinit=10.00, valstep=0.01)

    s_n.on_changed(update)
    s_area.on_changed(update)

    resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', color='#55cd53', hovercolor='#cd5353')

    def reset(event):
        s_n.reset()
        s_area.reset()


    button.on_clicked(reset)

    plt.show()
