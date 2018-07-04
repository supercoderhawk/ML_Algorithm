# -*- coding: UTF-8 -*-


class BaseModel:
  def __init__(self):
    pass

  def fit(self):
    raise Exception('Not implementation fit function')

  def predict(self, data):
    raise Exception('Not implementation predict function')