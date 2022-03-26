import PIL
import torch
import numpy as np
import matplotlib.pyplot as plt
from torch.autograd import Variable
from torchvision import transforms
from tkinter import *
from PIL import ImageDraw, Image
import os.path
import cv2
import datetime

from CNN import CNNModel

# CNN model
CNNmodel = CNNModel()
CNNmodel.load_state_dict(torch.load('models/CNN_model.pt', map_location='cpu'))
CNNmodel.eval()

path = 'image.jpg'


def recognizeCNN(path, model):
    """
    ensure that the image.jpg is correctly configured for the model to read the model then tries to correctly predict image
    :param path: image.jpg that was drawn on
    :param model: EMNIST saved trained and tested model
    :return: the predicted image from the CNN model
    """
    inputimg = cv2.imread(path)
    inputimg = cv2.resize(inputimg, (28, 28))
    inputimg = cv2.cvtColor(inputimg, cv2.COLOR_BGR2GRAY)
    inputimg = np.fliplr(inputimg)  # flip left/right
    inputimg = np.rot90(inputimg)  # rotate 90 degree
    trans = transforms.ToTensor()  # to tensor transform
    inputimg = trans(inputimg)  # use the transform
    inputimg.unsqueeze_(0)  # add a dimension
    # read model
    output = model(inputimg)
    pred_1 = output.argmax(dim=1, keepdim=True)
    _ = output.topk(5, dim=1)
    return pred_1.item()


def readCNN():
    """
    save and recognizes the most resent image
    :return: the predicted image for the CNN model
    """

    image.save(path)

    # recognize the character in the image
    top1= recognizeCNN(path, CNNmodel)
    mapping = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'd', 'e', 'f', 'g', 'h', 'n', 'q', 'r',
     't']

    top1 = int(top1)

    text_1.insert(END, str(mapping[top1]))


def error_to_file():
    """Display the path error message"""
    print("This is an error file")

def deleteCNN():
    """Delete the character on demand"""
    text_1.delete('end-2c')


def exitt():
    """exit/end the program/window"""
    exit()

def InstrucButton():
    """Help window"""
    top = Toplevel()
    top.title("Instructions")
    Instrucs = 'In the grey box draw a single number or letter from the English alphabet.\n' \
           'Only one number or letter can be written at a time.\n' \
           'Press the \'all read\' button for the character in the grey box to be recognized by both CNN and ANN.\n' \
           'The result will be presented box bellow.\n' \
           '\'read CNN\' and \'read ANN\' button makes that singular model recognizes the drawing\n' \

    label_6 = Label(top, width=90, height=15, text=Instrucs,
                    font=("Arial Bold", 20), justify=LEFT)
    label_6.grid(row=0, column=0)



def onlyCNN():
    # call CNN model and clears
    readCNN()
    clear_image()




def clear_image():
    # clears
    can.delete('all')  # clear canvas
    image = Image.new('RGB', (width, height), (0, 0, 0))
    image.save(path)


