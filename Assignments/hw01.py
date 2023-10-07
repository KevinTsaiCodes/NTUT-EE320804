import numpy as np
import matplotlib.pyplot as plt


def get_predictions(prob_class1, prob_class2, prob_class3):
    predicted_class = np.argmax([prob_class1, prob_class2, prob_class3])
    print(f"Class predictions: {predicted_class}")


def make_probability(data_x, data_y, predict_x, predict_y):
    EuclideanThreshold = 1.0
    EuclideanDistance = np.sqrt((data_x - predict_x)**2 + (data_y - predict_y)**2)
    weighted_probability = 1 / (1 + EuclideanDistance)
    weighted_probability_sum = np.sum(weighted_probability)
    return weighted_probability_sum / len(data_x)


def generate_data():
    # class 0
    data_x1 = np.random.uniform(0.5, 1.0, 100)
    data_y1 = np.random.uniform(0.5, 1.0, 100)
    # class 1
    data_x2 = np.random.uniform(1.0, 1.5, 100)
    data_y2 = np.random.uniform(1.0, 1.5, 100)
    # class 2
    data_x3 = np.random.uniform(1.0, 1.5, 100)
    data_y3 = np.random.uniform(0.0, 0.5, 100)
    # Prediction class
    predict_x = np.random.uniform(0.5, 2.0)
    predict_y = np.random.uniform(0.5, 2.0)
    # Plot the data
    plt.scatter(data_x1, data_y1, color='red', marker='1', label='Class 0')
    plt.scatter(data_x2, data_y2, color='blue', marker='x', label='Class 1')
    plt.scatter(data_x3, data_y3, color='green', marker='.', label='Class 2')
    plt.scatter(predict_x, predict_y, color='black', marker='^', label='Predict Value')
    plt.legend(loc='upper left')
    plt.title('NTUT-EE320804 Assignment I')
    plt.show()

    prob_class1 = make_probability(data_x1, data_y1, predict_x, predict_y)
    prob_class2 = make_probability(data_x2, data_y2, predict_x, predict_y)
    prob_class3 = make_probability(data_x3, data_y3, predict_x, predict_y)

    get_predictions(prob_class1, prob_class2, prob_class3)


if __name__ == '__main__':
    generate_data()
