import os, shutil, random

import tensorflow as tf

from tensorflow.keras import utils

dir = "/tmp"; true = True

class Haunt:
    def __init__(self, origin, extract=true):
        self.origin  = origin
        self.extract = extract

    @property
    def Filer(self):
        result = {}

        utils.get_file(origin=self.origin, cache_dir=dir, extract=self.extract)

        for i in os.listdir("/tmp/datasets"):
            if os.path.isdir(os.path.join("/tmp/datasets", i)):
                path = os.path.join("/tmp/datasets", i)

        for p in os.listdir(path):
            if os.path.isdir(os.path.join(path, p)):
                result[p] = os.path.join(path, p)

        return result


    def Filter(self, base):
        i = 0
        for folder in os.listdir(base):
            filepath = os.path.join(base, folder)
            try:
                file_object = open(filepath, "rb")
                picture_obj = tf.compat.as_bytes("JFIF") in file_object.peek(10)
            finally:
                file_object.close()
            
            if not picture_obj:
                i += 1
                os.remove(filepath)

        return i

    @classmethod
    def Trainest(self, source, training, testing, train_split=0.9):
        shuffle_data = random.sample(os.listdir(source), len(os.listdir(source)))
        total_train = int(len(shuffle_data) * train_split)
        total_test = len(os.listdir(source)) - total_train
        total_image = 0; label = training

        for item in shuffle_data:
            item_root = os.path.join(source, item)
            if os.path.getsize(item_root) == 0:
                continue
            shutil.move(item_root, os.path.join(label, item))
            total_image += 1

            if total_image == total_train:
                label = testing

        return {"train":total_train, "test":total_test}
