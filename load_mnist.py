import numpy as np
import pandas as pd
import os
from matplotlib import pyplot as plt
import cv2
from skimage.filters import threshold_otsu
from PIL import Image
from pylab import contour

def flat_to_one_hot(labels):
    num_classes = np.unique(labels).shape[0]
    num_labels = labels.shape[0]
    index_offset = np.arange(num_labels) * num_classes
    labels_one_hot = np.zeros((num_labels,num_classes))
    labels_one_hot.flat[index_offset + labels.ravel()] = 1
    return labels_one_hot


validation_size=2000
data = pd.read_csv('MLDM_Project/train.csv')
images = data.iloc[:,1:].values
labels = data[['label']].values.ravel()
# Convert the images from uint8 to double:
images = np.multiply(images,1.0/255.0)
# Convert the labels to one hot encoding:
labels = flat_to_one_hot(labels)
# Split the data into validation and training data:
validation_images = images[:validation_size]
validation_labels = labels[:validation_size]
train_images = images[validation_size:]
train_labels = labels[validation_size:]
# Convert the images from flat to matrix form:
train_images = train_images.reshape(train_images.shape[0],1,28,28)
validation_images = validation_images.reshape(validation_images.shape[0],1,28,28)
	# Return the data:
     #return (train_images,train_labels),(validation_images,validation_labels)
#%%
A = train_images[0,0];
plt.imshow(A);
#ret2,th2 = cv2.threshold(A,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
thresh = threshold_otsu(A);
binary = A > thresh
plt.imshow(binary)
contour_image = contour(A, levels = [245], colors='black', origin='image')
c_i = np.array(contour_image).astype('int32')
CS = plt.contour(binary)


