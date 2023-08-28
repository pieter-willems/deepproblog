import pandas as pd
import os
from PIL import Image
import torchvision.transforms as transforms


from problog.logic import Term, Constant
from torch.utils.data import Dataset as TorchDataset
from deepproblog.dataset import Dataset
from deepproblog.query import Query

puzzle_solver_path=os.path.join(os.path.expanduser('~') , 'PycharmProjects' , 'deepproblog_pieter' , 'src','deepproblog','puzzle_solver_simple_test')
path_simple_dataset=os.path.join(puzzle_solver_path,'simple_puzzle_dataset_test')
path_simple_images=os.path.join(puzzle_solver_path,'simple_puzzle_dataset_test','images')


class shape_dataset(Dataset,TorchDataset):
    def __init__(self, subset):
        self.labels=pd.read_csv(os.path.join(str(path_simple_dataset), (subset+".csv")))
        self.subset=subset
        self.data=[]
        self.transform= transforms.Compose(
             [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]
)
        i=0
        while i<len(self.labels):
                self.data.append((self.labels.iloc[i,0], self.labels.iloc[i,1], self.labels.iloc[i,2],
                                 self.labels.iloc[i,3],self.labels.iloc[i,4],self.labels.iloc[i,5]))
                i+=1
    def __len__(self):
        return len(self.labels)
    def __getitem__(self,index):
        if type(index) is tuple:
            index=index[0]
        img_path= os.path.join(str(path_simple_images), (str(index)+".png"))

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
        while j < 3:
            t = Term(f"p_{j}")
            subs[t] = Term("tensor",
                     Term(
                         self.subset,
                         Constant(self.data[i][j])))
            tensor_vars.append(t)
            j += 1
        return Query(Term("solution", *(x for x in tensor_vars),
                    Constant(self.data[i][3]),
                          Constant(self.data[i][4]),Constant(self.data[i][5]))
                          , subs,output_ind=(-1,-2,-3))


train_dataset = shape_dataset("train")
test_dataset = shape_dataset("test")


if __name__ == '__main__':
    train_dataset = shape_dataset("train")
    test_dataset = shape_dataset("test")
    print(train_dataset.data[0][3])
    print(train_dataset.data[0][4])
    print(train_dataset.data[0][5])
