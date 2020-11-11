from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()

    total_vals = int(input('Cuantos valores vas a graficar? '))
    x_vals = list(range(total_vals))
    y_vals = [(i ** 2 - (3 * i) - 100) for i in range(total_vals)]

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
