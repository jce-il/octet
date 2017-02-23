import csv
import sys
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


def read_csv_file_for_classifier(csv_file):
    """ Read a csv file - the file is needed for creating the classifier"""
    x = []
    y = []
    z = []
    with open(csv_file, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            x.append(float(row[0]))  # insert into x first column values
            y.append(float(row[1]))  # insert into y second column values
            z.append(row[2])  # insert into z third column, the known classification

    coordinates = zip(x, y)  # return a list of tuples [(x0, y0), (x1, y1), ..., (xn, yn)]
    input_data = {coordinates[i]: z[i] for i in xrange(len(coordinates))}  # format the input-data to be a list of:
    # {(x0, y0): z0, (x1, y1): z1, ...}
    return input_data


def read_csv_file_for_tester(csv_file):
    """Read csv file - the file contains the data that needs to be classify"""
    x = []
    y = []
    with open(csv_file, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            x.append(float(row[0]))  # insert into x first column values
            y.append(float(row[1]))  # insert into y second column values

    coordinates = zip(x, y)  # return a list of tuples [(x0, y0), (x1, y1), ..., (xn, yn)]
    return coordinates


def get_num_of_classifier_possibilities(input_data):
    """Get the amount of possible classifiers"""
    classifiers = input_data.values()
    classifiers = list(set(classifiers))
    print(len(classifiers))
    return len(classifiers)


def get_legends(input_data, colors):
    """Return a dictionary for legends"""
    classifiers = input_data.values()
    classifiers = list(set(classifiers))
    return dict(zip(classifiers, colors))


def euclidean_distance(x, y):
    """Return Euclidean distance between 2 points """
    if len(x) != len(y):
        return "Error: try equal length vectors"
    else:
        return np.sqrt(sum([(x[i] - y[i]) ** 2 for i in xrange(len(y))]))


def neighbors(k, trained_points, new_point):
    """ Find the k nearest neighbors at point p and return theirs indices"""

    neighbor_distances = {}

    for point in trained_points:
        if point not in neighbor_distances:
            neighbor_distances[point] = euclidean_distance(point, new_point)

    # sort the results and slice off the first K elements
    least_common = sorted(neighbor_distances.items(), key=lambda x: x[1])
    # least_common = np.argsort(neighbor_distances)
    k_nearest_neighbors = zip(*least_common[:k])
    print("List of k nearest neighbors of new point %s" % (new_point,) + ": ")
    print('[%s]' % ', '.join(map(str, list(k_nearest_neighbors[0]))))
    return list(k_nearest_neighbors[0])


def knn_classifier(neighbors, input_data):
    """Classify the data by relying on the neighbors"""
    knn = [input_data[i] for i in neighbors]
    knn = Counter(knn)
    classifier, _ = knn.most_common(1)[0]
    print("Classifier " + classifier)
    return classifier


def plot_classified_data(colors_reader, marker_input, marker_output, data_reader, data_tester, output_filename):
    """Plot data"""
    if len(colors_reader) != get_num_of_classifier_possibilities(data_reader):
        sys.stderr.write("You must enter amount of colors as number of possible classifiers")
    plt.figure()
    (coordinates_reader, classifiers_reader) = (data_reader.keys(), data_reader.values())
    (coordinates_tester, classifiers_tester) = (data_tester.keys(), data_tester.values())
    list_classifiers_reader = list(set(classifiers_reader)) # convert a set into list
    list_classifiers_tester = list(set(classifiers_tester))  # convert a set into list
    list_classifiers_reader.sort()
    list_classifiers_tester.sort()
    for c in coordinates_tester:
        output_points = plt.scatter(c[0], c[1], s=50,
                                    c=colors_reader[list_classifiers_tester.index(data_tester.get(c))],
                                    marker=marker_output)
        # plt.plot(c[0], c[1], colors_reader[list_classifiers_tester.index(data_tester.get(c))]+point_result_type)
    for c in coordinates_reader:
        print(colors_reader[list_classifiers_reader.index(data_reader.get(c))])
        # plt.plot(c[0], c[1], colors_reader[list_classifiers_reader.index(data_reader.get(c))]+point_input_type)
        input_points = plt.scatter(c[0], c[1], s=20, c=colors_reader[list_classifiers_reader.index(data_reader.get(c))], marker=marker_input)

    print(coordinates_tester)
    plt.xlabel('Variable 1')
    plt.ylabel('Variable 2')
    legend = get_legends(data_reader, colors_reader)
    markers = [plt.Line2D([0, 0], [0, 0], color=color, marker='o', linestyle='') for color in legend.values()]
    plt.legend(markers, legend.keys(), numpoints=1)
    plt.savefig(output_filename)
    plt.show()


def main():
    # Read data from csv file
    input_data = read_csv_file_for_classifier("data-reader.csv")
    test_coordinates = read_csv_file_for_tester("data-tester.csv")
    results = {}
    print ("Results: ")
    # Run knn Classifier for each point from the tester file
    for item in test_coordinates:
        results[item] = knn_classifier(neighbors(1, input_data.keys(), item), input_data)
    print(results)
    # Plot results
    plot_classified_data(["g", "b", "r", "m", "y", "c"], "o", "s", input_data, results, "results1.pdf")


main()


#b: blue
#g: green
#r: red
#c: cyan
#m: magenta
#y: yellow
#k: black
#w: white