
import torch
import torchvision.transforms as transforms
from deepproblog.Puzzle_solver_v1.dataset import shape_dataset

transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
)

shape_dataset("./dataset/labels.csv", "./dataset/images", transform)

