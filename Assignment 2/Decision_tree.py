import numpy as np
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier


def classification_error(predictedlabels, testlabels):
    # to be completed
    return percentage_error


if __name__ == "__main__":
    train_samples = np.loadtxt(train_sam_file)  # load training dataset here. 
    train_labels = np.loadtxt(train_label_file)  # load training labels here

    test_samples = np.loadtxt(test_sam_file)  # load testing dataset here
    test_labels = np.loadtxt(test_label_file)  # load testing labels here
    no_of_runs = # specify number of runs
    error = np.zeros(no_of_runs)
    for inx in range(no_of_runs):

    	# complete decision tree code

    print(error) # array/list containing error for each run 
    print('Trees ERROR = ', avg_error) # average error across all iterations

    n_est = [5, 10, 15, 20, 25, 30] # number of estimators
    for n in n_est:
	for inx in range(no_of_runs):

        `	# complete random forest code

        print('Random forest no of esitmators = %d ERROR = %d' % (n, avg_error))


