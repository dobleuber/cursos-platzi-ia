from random import randint
from bokeh.plotting import figure, show

plot = figure()


def distance(point_1, point_2, size=4):
    '''
    Get euclidean distance between two points
    :param point_1:
    :param point_2:
    :return: the distance
    '''
    return ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)**0.5


def get_mid_point(point_1, point_2):
    return (point_1[0] + point_2[0]) // 2, (point_1[1] + point_2[1]) // 2


def draw_plot(points, color='blue', size=4):
    for point in points:
        plot.circle_dot(point[0], point[1], fill_color=color, size=size)


def generate_data():
    points = []
    for _ in range(100):
        points.append((randint(0, 100), randint(0, 100)))

    draw_plot(points)

    return points


def clustering(data):
    nearest_points = []
    clusters = 0
    while clusters < 10:
        i = 0
        while len(data) > 0 and i < len(data):
            min_diff = 10000
            j = i + 1
            nearest_index = -1
            while j < len(data) and len(data) > 0:
                dis = distance(data[i], data[j])
                if dis < min_diff:
                    min_diff = dis
                    nearest_index = j
                    try:
                        nearest_points[clusters] = [data[i], data[j]]
                        print(f'cluster: {clusters}, point 1: {data[i]}, point 2: {data[j]}')
                    except IndexError as e:
                        print(e)
                        print(f'Index: {clusters}, len: {len(nearest_points)}')
                        nearest_points.append([data[i], data[j]])

                j += 1
            if min_diff < 1000:
                new_point = get_mid_point(nearest_points[clusters][0], nearest_points[clusters][1])
                # print(f'len: {len(data)} nearest item: {nearest_index}, index: {i}')
                del data[nearest_index]
                del data[i]
                data.append(new_point)
            i += 1

        clusters += 1

    print(nearest_points)

    for points in nearest_points:
        print(points)
        draw_plot(points, 'red', 10)


if __name__ == '__main__':
    data = generate_data()
    clustering(data)

    show(plot)
