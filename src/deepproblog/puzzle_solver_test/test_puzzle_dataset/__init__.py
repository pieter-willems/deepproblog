import pandas as pd
import os
from PIL import Image
import torchvision.transforms as transforms


from problog.logic import Term, Constant
from torch.utils.data import Dataset as TorchDataset
from deepproblog.dataset import Dataset
from deepproblog.query import Query



puzzle_solver_test_path=os.path.join(os.path.expanduser('~') , 'PycharmProjects' , 'deepproblog_pieter' , 'src','deepproblog','puzzle_solver_test')

path_test_dataset = os.path.join(puzzle_solver_test_path , 'test_puzzle_dataset')
path_test_images = os.path.join(puzzle_solver_test_path , 'test_puzzle_dataset', 'images')



class shape_dataset(Dataset,TorchDataset):
    def __init__(self, subset):
        self.labels=pd.read_csv(os.path.join(str(path_test_dataset), (subset+".csv")))
        self.subset=subset
        self.data=[]
        self.transform= transforms.Compose(
             [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]
)
        i=0
        while i<len(self.labels):
                self.data.append((self.labels.iloc[i,0], self.labels.iloc[i,1]))
                i+=1
    def __len__(self):
        return len(self.labels)
    def __getitem__(self,index):
        if type(index) is tuple:
            index=index[0]
        img_path= os.path.join(str(path_test_images), (str(index)+".png"))

        with open(img_path,'rb') as f:
                img=Image.open(f)
                img.convert("RGB")
                if self.transform:
                    img=self.transform(img)
        return img

    def to_query(self, i: int) -> Query:

        tensor_vars = []
        subs=dict()
        j = 0
        t = Term(f"p_{j}")
        subs[t] = Term("tensor",
            Term(
                             self.subset,
                             Constant(self.data[i][j])
            )
                       )
        tensor_vars.append(t)
        return Query(Term("solution", *(x for x in tensor_vars), Constant(self.data[i][1])), subs)

    def to_query2(self, i: int) -> Query:
        """Generate queries"""
        mnist_indices = self.data[i]
        expected_result = self._get_label(i)

        # Build substitution dictionary for the arguments
        subs = dict()
        var_names = []
        for i in range(self.arity):
            inner_vars = []
            for j in range(self.size):
                t = Term(f"p{i}_{j}")
                subs[t] = Term(
                    "tensor",
                    Term(
                        self.dataset_name,
                        Constant(mnist_indices[i][j]),
                    ),
                )
                inner_vars.append(t)
            var_names.append(inner_vars)

        # Build query
        if self.size == 1:
            return Query(
                Term(
                    self.function_name,
                    *(e[0] for e in var_names),
                    Constant(expected_result),
                ),
                subs,
            )
        else:
            return Query(
                Term(
                    self.function_name,
                    *(list2term(e) for e in var_names),
                    Constant(expected_result),
                ),
                subs,
            )


train_dataset = shape_dataset("train")
test_dataset = shape_dataset("test")

if __name__ == "__main__":
    pass