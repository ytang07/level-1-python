from distutils.command.config import config


conf_matrix = {
    "tp": 8,
    "fp": 1,
    "fn": 2,
    "tn": 9
}

def accuracy(conf_matrix: dict):
    return (conf_matrix["tp"] + conf_matrix["tn"])/(sum(conf_matrix.values()))

def precision(conf_matrix: dict):
    return conf_matrix["tp"]/(conf_matrix["tp"] + conf_matrix["fp"])

def recall(conf_matrix: dict):
    return conf_matrix["tp"]/(conf_matrix["tp"] + conf_matrix["fn"])

def f1(conf_matrix: dict):
    p = precision(conf_matrix)
    r = recall(conf_matrix)
    return 2 * p * r / (p + r)

print(accuracy(conf_matrix))
print(precision(conf_matrix))
print(recall(conf_matrix))
print(f1(conf_matrix))