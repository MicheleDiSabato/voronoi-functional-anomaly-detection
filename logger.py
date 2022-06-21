'''
Helper classes to save the result (classification matrix and logs) for all models.
'''

import faulthandler
import os
import numpy as np
from datetime import datetime
####################################################################
class logger:
  def __init__(self, folder_name, file_name = "log.txt", subfolder_name = None, read = False):
    if subfolder_name == None:
      now = datetime.now()
      dt_string = "LOG_" + now.strftime("%d%m%Y_%H%M%S")
    else:
      dt_string = subfolder_name
    if not os.path.exists(folder_name) and read == False:
        os.mkdir(folder_name)
    self.directory = os.path.join(folder_name, dt_string)
    if not os.path.exists(self.directory) and read == False:
        os.mkdir(self.directory)
    self.file_name = file_name
    if read == False:
      self.file_path = os.path.join(self.directory, file_name) # directory of the file
    else:
      self.file_path = os.path.join(folder_name, file_name)

  def get_directory(self):
    return self.directory
  
  def get_directory_string(self):
    return str(self.directory)

  def write(self, msg):
    if os.path.isfile(self.file_path):
        f = open(self.file_path, "a")
        f.write('\n' + msg) 
    else:
        f = open(self.file_path, "w")
        f.write(msg) 
    f.close() 
####################################################################
class VoronoiLogger(logger):
  def __init__(self, folder_name, file_name = "log.txt", subfolder_name = None, read = False, encoding = ["iteration_time", "dimensionality_reduction", "average_normalized_entropy", "distance_matrix_size", "number_of_nucei"]):
    super().__init__(folder_name, file_name, subfolder_name, read)
    self.encoding = encoding
    
  def __read_log(self, index):
    res = []
    with open(self.file_path,"r") as f:
        for i, line in enumerate(f): # line is a string
            name_end  = len(self.encoding[index])
            if line[:name_end] == self.encoding[index]:
                res.append(float(line[name_end:]))
    return np.array(res).reshape(-1,)

  def get_statistics(self, feature_name):
    assert feature_name in self.encoding, f"{feature_name} has not been saved. Supported features are {self.encoding}"
    for i, feat in enumerate(self.encoding):
        if feat == feature_name:
            index = i
    return self.__read_log(index)

  def get_encoding(self):
    return self.encoding
####################################################################
class StatisticalLogger(logger):
  def __init__(self, folder_name, file_name = "log.txt", subfolder_name = None, read = False, encoding = ["iteration_time", "dimensionality_reduction", "average_normalized_entropy", "distance_matrix_size", "number_of_nucei"]):
    super().__init__(folder_name, file_name, subfolder_name, read)
    self.encoding = encoding
    
  def __read_log(self, index):
    res = []
    with open(self.file_path,"r") as f:
        for i, line in enumerate(f): # line is a string
            name_end  = len(self.encoding[index])
            if line[:name_end] == self.encoding[index]:
                res.append(float(line[name_end:]))
    return np.array(res).reshape(-1,)

  def get_statistics(self, feature_name):
    assert feature_name in self.encoding, f"{feature_name} has not been saved. Supported features are {self.encoding}"
    for i, feat in enumerate(self.encoding):
        if feat == feature_name:
            index = i
    return self.__read_log(index)

  def get_encoding(self):
    return self.encoding
####################################################################
class TeseoLogger(logger):
  def __init__(self, folder_name, file_name = "log.txt", subfolder_name = None, read = False, encoding = ["threshold", "iteration_time", "dimensionality_reduction", "average_normalized_entropy", "distance_matrix_size", "number_of_nucei"]):
    super().__init__(folder_name, file_name, subfolder_name, read)
    self.encoding = encoding
  
  def __read_log(self, index):
    res = []
    with open(self.file_path,"r") as f:
        for i, line in enumerate(f): # line is a string
            name_end  = len(self.encoding[index])
            if line[:name_end] == self.encoding[index]:
                res.append(float(line[name_end:]))
    return np.array(res).reshape(-1,)

  def get_statistics(self, feature_name):
    assert feature_name in self.encoding, f"{feature_name} has not been saved. Supported features are {self.encoding}"
    for i, feat in enumerate(self.encoding):
        if feat == feature_name:
            index = i
    return self.__read_log(index)

  def get_encoding(self):
    return self.encoding


if __name__ == "__main__":
  print("File name: logger.py")
  
