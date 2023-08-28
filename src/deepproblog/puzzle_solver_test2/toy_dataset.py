import os
import random

import PIL
import torch
import torchvision.transforms

from deepproblog.dataset import Dataset
from problog.logic import Term, list2term, Constant
from torch.utils.data import Dataset as TorchDataset

from deepproblog.query import Query


class ToyDataset(TorchDataset):
    def __init__(self, size=1000):
        """
        """
        #base_dir = os.path.abspath(os.sep)
        base_dir = os.path.expanduser('~')
        #data_dir = os.path.join(base_dir, 'mnt', 'DataMorry', 'Work', 'Projects', 'MAThesis', 'deepproblog',
        #                         'src', 'deepproblog', 'laurent', 'data')
        data_dir = os.path.join(base_dir,'PycharmProjects' , 'deepproblog_pieter' , 'src','deepproblog', 'puzzle_solver_test2','data')
        white = os.path.join(data_dir, 'white.jpg')
        black = os.path.join(data_dir, 'black.jpg')
        red = os.path.join(data_dir, 'red.jpg')
        green = os.path.join(data_dir, 'green.jpg')
        blue = os.path.join(data_dir, 'blue.jpg')

        with open(white, 'rb') as fin:
            white = PIL.Image.open(fin).convert('RGB')
        with open(black, 'rb') as fin:
            black = PIL.Image.open(fin).convert('RGB')
        with open(red, 'rb') as fin:
            red = PIL.Image.open(fin).convert('RGB')
        with open(green, 'rb') as fin:
            green = PIL.Image.open(fin).convert('RGB')
        with open(blue, 'rb') as fin:
            blue = PIL.Image.open(fin).convert('RGB')

        self.white = torchvision.transforms.ToTensor()(white)
        self.black = torchvision.transforms.ToTensor()(black)
        self.red = torchvision.transforms.ToTensor()(red)
        self.green = torchvision.transforms.ToTensor()(green)
        self.blue = torchvision.transforms.ToTensor()(blue)
        self.size = size

    def __getitem__(self, item: int) -> (torch.Tensor, torch.Tensor):
        """
        Retrieves an item from the dataset.

        :param item: Item index.
        :return: Return item in the form (s, t, u, v), where s are the pre-computed ImageNet features,
         t are the pre-computed OIToFER features, u is the image path, and v is the target
        be predicted.
        """
        if isinstance(item, tuple):
            item = item[0].value
        if item > self.size:
            raise ValueError(f"Index out of bounds: {item}")
        idx = item%5
        if idx == 0:
            return self.white
        elif idx == 1:
            return self.black
        elif idx == 2:
            return self.red
        elif idx == 3:
            return self.green
        else:
            return self.blue

    def __len__(self) -> int:
        return self.size


def toy_problem(dataset: ToyDataset, dataset_name: str, seed=None):
    """Returns a dataset for binary addition"""
    return ToyOperator(
        dataset=dataset,
        dataset_name=dataset_name,
        function_name="check_color",
        seed=seed,
    )


class ToyOperator(Dataset, TorchDataset):
    def __init__(
        self,
        dataset: ToyDataset,
        dataset_name: str,
        function_name: str,
        seed=None,
    ):
        """Generic dataset for operator(img) style datasets.

        :param dataset_name: Dataset to use (train, val, test)
        :param function_name: Name of Problog function to query.
        :param size: Size of numbers (number of digits)
        :param seed: Seed for RNG
        """
        super().__init__()
        self.dataset = dataset
        self.dataset_name = dataset_name
        self.function_name = function_name
        self.seed = seed
        sample_indices = list(range(len(self.dataset)))
        if seed is not None:
            rng = random.Random(seed)
            rng.shuffle(sample_indices)
        dataset_iter = iter(sample_indices)
        # Build list of examples (mnist indices)
        self.data = []
        try:
            while dataset_iter:
                self.data.append(
                    [
                        next(dataset_iter)
                    ]
                )
        except StopIteration:
            pass

    def to_query(self, i: int) -> Query:
        """Generate queries"""
        sample_idx = i
        expected_result = self._get_label(i)

        # Build substitution dictionary for the arguments
        subs = dict()

        t = Term(f"p{i}")
        subs[t] = Term(
            "tensor",
            Term(
                self.dataset_name,
                Constant(sample_idx),
            ),
        )

        # Build query
        return Query(
            Term(
                self.function_name,
                t,
                Constant(expected_result),
            ),
            subs,
        )

    def _get_label(self, i: int):
        expected_result = i % 5
        return expected_result

    def __len__(self):
        return len(self.data)


if __name__ == '__main__':
    to = ToyOperator(dataset=ToyDataset(size=100),
                     dataset_name='train',
                     function_name='check_color',
                     seed=None)
    a = to.to_query(12)
    print(a)
