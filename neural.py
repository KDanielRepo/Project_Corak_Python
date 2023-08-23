import numpy


class Neural:
    Train = False
    def __init__(self):
        self.Train = True

    def start_train(self):
        if self.Train:
                #!python train.py --data ../data/yaml --weights yolov5s.pt \