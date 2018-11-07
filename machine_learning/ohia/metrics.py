"""
File: metrics.py
Author: Matt Motoki
Description: Wrapper functions for common classification metrics.
"""

from keras import metrics

def top_1_accuracy(y_true, y_pred):
    return metrics.categorical_accuracy(y_true, y_pred)

def top_3_accuracy(y_true, y_pred):
    return metrics.top_k_categorical_accuracy(y_true, y_pred, k=3)

def top_5_accuracy(y_true, y_pred):
    return metrics.top_k_categorical_accuracy(y_true, y_pred, k=5)