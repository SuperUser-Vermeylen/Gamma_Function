import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

DX = 0.01
INITIAL_N = 3.0
INITIAL_AREA = 10.0


def gamma_curve(x, n):
    return x ** n * np.exp(-x)


def approximate_area(n, limit):
    x = np.arange(0, limit, DX)
    y = gamma_curve(x, n)
    return np.trapz(y, dx=DX), x, y


def update(_):
    n_value = round(s_n.val, 2)
    area_limit = s_area.val

    area_value, area_x, area_y = approximate_area(n_value, area_limit)
    ax.set_title(f"Approximate Factorial {n_value:.2f}! = {area_value:.2f}")

    if factorial_fill[0] is not None:
        factorial_fill[0].remove()
    factorial_fill[0] = ax.fill_between(area_x, area_y, color="#b953cd", label="factorial")

    line.set_ydata(gamma_curve(t, n_value))
    fig.canvas.draw_idle()


if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.set_ylim(top=500000)
    fig.subplots_adjust(left=0.15, bottom=0.25)
    ax.margins(x=0)

    ax.text(
        80,
        450000,
        r'$\Gamma(\mathscr{t})$ = $\int_0^\infty \mathscr{x}^{\mathscr{t}-1} e^{-\mathscr{x}}$',
        fontsize=15,
    )

    t = np.arange(0, 100, DX)
    line, = ax.plot(t, gamma_curve(t, INITIAL_N), lw=2, color="k")

    initial_area_value, x, y = approximate_area(INITIAL_N, INITIAL_AREA)
    ax.set_title(f"Approximate Factorial {INITIAL_N:.2f}! = {initial_area_value:.2f}")
    factorial_fill = [ax.fill_between(x, y, color="#b953cd", label="factorial")]

    ax_n = plt.axes([0.15, 0.1, 0.75, 0.03], facecolor="#cd5353")
    ax_area = plt.axes([0.15, 0.15, 0.75, 0.03], facecolor="#cd5353")

    s_n = Slider(ax_n, "n", 0, 20, valinit=INITIAL_N, valstep=0.01)
    s_area = Slider(ax_area, "Area", 0, 100, valinit=INITIAL_AREA, valstep=0.01)

    s_n.on_changed(update)
    s_area.on_changed(update)

    resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, "Reset", color="#55cd53", hovercolor="#cd5353")

    def reset(_):
        s_n.reset()
        s_area.reset()

    button.on_clicked(reset)

    plt.show()
