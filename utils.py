from numpy import *
import matplotlib
import matplotlib.pyplot as plt


def file2matrix(filename):
    data_file = open(filename)
    data_lines = data_file.readlines()
    number_of_lines = len(data_lines)

    data_matrix = zeros((number_of_lines, 1))

    for line_index in range(number_of_lines):
        line = data_lines[line_index].strip()
        data_matrix[line_index, :] = line[:]

    return data_matrix


def plot_points(x_matrix, y_matrix):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x_matrix[:], y_matrix[:])
    plt.xlabel('Age')
    plt.ylabel('Height')
    plt.show()

if __name__ == '__main__':
    x_matrix = file2matrix('ex2x.dat')
    y_matrix = file2matrix('ex2y.dat')

    plot_points(x_matrix, y_matrix)
