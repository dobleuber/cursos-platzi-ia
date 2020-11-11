from bokeh.plotting import figure, show
from random import choice, randint

from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

path_x = []
path_y = []

draw = figure(title='Camino de borrachos', x_axis_label='Paso en x', y_axis_label='Paso en Y')


def walk(field, drunk, distance):
    start = field.get_coord(drunk)

    for _ in range(distance):
        new_coord = field.move_drunk(drunk)
        path_x.append(new_coord.x)
        path_y.append(new_coord.y)

    draw.line(path_x, path_y, legend_label=f'Camino en {distance} {randint(0, 100)}', line_color=choice(['blue', 'red', 'yellow', 'green', 'orange']))

    return start.distance(field.get_coord(drunk))


def simulate_walk(distance, attempts, drunk_type):
    drunk = drunk_type('David')
    origin = Coordenada(0, 0)
    distances = []
    for _ in range(attempts):
        campo = Campo()
        campo.add_drunk(drunk, origin)
        walk_simulate = walk(campo, drunk, distance)
        distances.append(round(walk_simulate, 1))

    return distances


def draw_walk():
    show(draw)


def main(distance, attempts, drunk_type):
    mean_distance_by_walk = []
    for d in distance:
        distances = simulate_walk(d, attempts, drunk_type)
        distance_mean = round(sum(distances) / len(distances), 4)
        distance_min = min(distances)
        distance_max = max(distances)
        mean_distance_by_walk.append(distance_mean)

        print(f'{drunk_type.__name__} had a walk of {d}')
        print(f'Mean: {distance_mean}')
        print(f'Min: {distance_min}')
        print(f'Max: {distance_max}')

    draw_walk()


if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 1

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)

