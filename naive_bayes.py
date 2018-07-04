# -*- coding: UTF-8 -*-
import numpy as np
from base import BaseModel


class NaiveBayes(BaseModel):
  def __init__(self, *, data=None, filename=None):
    '''
    使用numpy数组或者csv文件创建对象，只能选择一项进行初始化。
    数据格式：最后一列代表类别，其他列代表特征项
    :param data: numpy数组，必须二维
    :param filename: csv文件名
    '''
    BaseModel.__init__(self)
    if data and filename or not data and not filename:
      raise Exception('Input mode error')
    if filename:
      data = np.loadtxt(filename, delimiter=',')
    if not isinstance(data, np.ndarray) or len(data.shape) != 2 or data.shape[1] < 2:
      raise Exception('Data format error')

    self.features = []
    for col in data.T[:-1]:
      self.features.append({'count':dict(zip(*np.unique(col, return_counts=True)))})
    self.target = {'count':dict(zip(*np.unique(data[:,-1], return_counts=True)))}

  def fit(self):
    '''

    :return:
    '''
    target_count = self.target['count']
    for target_val in target_count:
      for feature in self.features:
        pass

  def predict(self, data):
    '''

    :param data:
    :return:
    '''
    pass