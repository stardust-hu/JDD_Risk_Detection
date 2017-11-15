# coding: utf8

def score(precision, recall, beta=0.1):
    beta_square = beta**2
    F_beta = (1 + beta_square) * (precision * recall) / (beta_square * precision + recall)
    return F_beta
