from bokeh.plotting import figure, output_file, show


def run():
    output_file('grafico.html')
    fig = figure()
    
    total_vals = int(input('Ingrese cuantos valores va a graficar: '))
    x_vals = list(range(total_vals))
    
    y_vals = []
    for i in x_vals:
        val = int(input(f'Ingrese el valor y para x{i}'))
        y_vals.append(val)
        
    fig.line(x_vals, y_vals, line_width=2)
    show(fig)


if __name__ == '__main__':
    run()