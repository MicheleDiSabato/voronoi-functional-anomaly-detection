import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
# !pip install tqdm
from tqdm import tqdm
import random

def pad(signal,spike):
  '''
  Function used to align the signals by padding.
  '''
  l = 400
  new_signal = np.zeros(400)
  if spike > 200:
      new_signal[:(200-spike)] = signal.values[(spike-200):]
  if spike < 200:
      new_signal[-(spike-200):] = signal.values[:spike+200]
  if spike == 200:
      new_signal[:] = signal.values[:]
  return new_signal

def find_spike(signals):
  '''
  Find the index of the spike for each signal.
  '''
  spikes = np.argmax(np.abs(signals.values), axis = 1)
  return spikes

print("loading the dataset")
df = pd.read_csv('LAsignals.csv')
# remove index column
df = df.iloc[:,-len(df.columns.values)+1:]
# tidy the dataset
coordinates = df.iloc[:,:3]
coordinates = coordinates.values
UAC = df.iloc[:,3:5]
IIR = df.iloc[:,5]
signals = df.iloc[:,6:]


spikes = find_spike(signals)
aligned_signals = np.zeros((signals.shape[0], signals.shape[1]))
print("aligning the signals")

with open("aligned_LAsignals.csv", "w") as f:
  for signal_index in tqdm(range(signals.shape[0])):
    aligned_signals[signal_index, :] = pad(signals.iloc[signal_index,:],spikes[signal_index])
    if(spikes[signal_index] < 200 and signal_index>1000):
      plt.plot(np.arange(400), signals.iloc[signal_index,:])
      plt.show()
      plt.plot(np.arange(400), aligned_signals[signal_index,:])
      plt.show()
      break
    for col in range(aligned_signals.shape[1]):
      if col == aligned_signals.shape[1] - 1:
        f.write(str(aligned_signals[signal_index, col]) + "\n")
      else:
        f.write(str(aligned_signals[signal_index, col]) + ",")
