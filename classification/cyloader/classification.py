import torch.utils.data as data
from PIL import Image
import os
import json
import numpy as np
from torch.utils.data import Dataset


class Chaoyang(Dataset):
    def __init__(self, root='', transform=None, is_train=True):
        self.transform = transform
        self.is_train = is_train

        if not self.is_train:
            imgs = []
            labels = []
            json_path = os.path.join(root, 'ori_json', 'test.json')
            with open(json_path, 'r') as f:
                load_list = json.load(f)
                for i in range(len(load_list)):
                    img_path = os.path.join(root, load_list[i]["name"])
                    imgs.append(img_path)
                    labels.append(load_list[i]["label"])
            self.test_data, self.test_labels = np.array(imgs), np.array(labels)
        else:  # is_train = True => Train.
            imgs = []
            labels = []
            json_path = os.path.join(root, 'ori_json', 'train.json')
            with open(json_path, 'r') as f:
                load_list = json.load(f)
                for i in range(len(load_list)):
                    img_path = os.path.join(root, load_list[i]["name"])
                    imgs.append(img_path)
                    labels.append(load_list[i]["label"])
            self.train_data, self.train_labels = np.array(imgs), np.array(labels)
            self.train_data = self.train_data
            self.noise_label = self.train_labels

    def __getitem__(self, idx):
        # In the function of building_dataset, the transform has been set following the is_train.
        if self.is_train:
            img, label = self.train_data[idx], self.noise_label[idx]
            img = Image.open(img).convert('RGB')
            img = self.transform(img)
            return img, label
        else:
            img, label = self.test_data[idx], self.test_labels[idx]
            img = Image.open(img).convert('RGB')
            img = self.transform(img)
            return img, label

    def __len__(self):
        if self.is_train:
            return len(self.train_data)
        else:
            return len(self.test_data)
