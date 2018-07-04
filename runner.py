#-*- coding: UTF-8 -*-
from naive_bayes import NaiveBayes

def naive_bayes_runner():
  model = NaiveBayes(filename='dataset/pima-indians-diabetes.data.csv')

if __name__ == '__main__':
  naive_bayes_runner()