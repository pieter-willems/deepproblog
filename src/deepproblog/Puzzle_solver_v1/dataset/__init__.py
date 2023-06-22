import pandas as pd
import os
from PIL import Image
import csv
import torchvision.transforms as transforms


from problog.logic import Term, Constant
from torch.utils.data import Dataset as TorchDataset
from deepproblog.dataset import Dataset
from deepproblog.query import Query


puzzle_solver_path=os.path.join(os.path.expanduser('~') , 'PycharmProjects' , 'deepproblog_pieter' , 'src','deepproblog','Puzzle_solver_v1')
path_csv=os.path.join(puzzle_solver_path,'dataset','labels.csv')
path_images=os.path.join(puzzle_solver_path,'dataset','images')
path_cut_dataset=os.path.join(puzzle_solver_path,'cut_dataset')
path_cut_images=os.path.join(puzzle_solver_path,'cut_dataset','images')



def create_sub_dataset(name,itterations,itteration_starting_value,original_labels):
    csv_name=name + ".csv"
    with open(os.path.join(str(path_cut_dataset) ,csv_name), 'w') as csv_file:
        fieldnames = ["top_left","top_middle","top_right","middle_left","middle_middle","middle_right","bottom_left","bottom_middle", "shape"]

        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        i=itteration_starting_value
        while i<itterations:
        #use roughly 80 percent of the original dataset as the train dataset
            img_path=os.path.join(path_images,original_labels.iloc[i,0])
            with open(img_path,'rb') as f:
                img = Image.open(f)
                l=cut_puzzle(img)

            top_left_name='puzzle_' + str(i) + '_tl'
            l[0].save(os.path.join(path_cut_images,(top_left_name+".png")))

            top_middle_name = 'puzzle_' + str(i) + '_tm'
            l[1].save(os.path.join(path_cut_images, (top_middle_name+".png")))

            top_right_name = 'puzzle_' + str(i) + '_tr'
            l[2].save(os.path.join(path_cut_images, (top_right_name + ".png")))

            middle_left_name = 'puzzle_' + str(i) + '_ml'
            l[3].save(os.path.join(path_cut_images, (middle_left_name + ".png")))

            middle_middle_name = 'puzzle_' + str(i) + '_mm'
            l[4].save(os.path.join(path_cut_images, (middle_middle_name + ".png")))

            middle_right_name = 'puzzle_' + str(i) + '_mr'
            l[5].save(os.path.join(path_cut_images, (middle_right_name + ".png")))

            bottom_left_name = 'puzzle_' + str(i) + '_bl'
            l[6].save(os.path.join(path_cut_images, (bottom_left_name + ".png")))

            bottom_middle_name = 'puzzle_' + str(i) + '_bm'
            l[7].save(os.path.join(path_cut_images, (bottom_middle_name + ".png")))

            csv_writer.writerow({"top_left": top_left_name,"top_middle": top_middle_name, "top_right":top_right_name,
                                 "middle_left":middle_left_name,"middle_middle":middle_middle_name,
                                 "middle_right":middle_right_name, "bottom_left":bottom_left_name,
                                 "bottom_middle":bottom_middle_name,"shape":original_labels.iloc[i,1]} )
            i+=1
def create_cut_dataset ():
    original_labels=pd.read_csv(path_csv)
    csv_file_length=len(original_labels)
    create_sub_dataset("train",int((csv_file_length/100)*80),0,original_labels)
    create_sub_dataset("test",csv_file_length,int((csv_file_length/100)*80),original_labels)





def cut_puzzle(img):
    #using pillow as torchvison transforms accept pillow images
    top_left=img.crop(box=(0, 0, 200, 200))
    top_mid= img.crop(box=(200,0,400,200))
    top_right= img.crop(box=(400,0,600,200))

    mid_left=img.crop(box=(0, 200, 200, 400))
    mid_mid= img.crop(box=(200,200,400,400))
    mid_right= img.crop(box=(400,200,600,400))

    bot_left = img.crop(box=(0, 400, 200, 600))
    bot_mid = img.crop(box=(200, 400, 400, 600))

    return [top_left,top_mid,top_right,mid_left,mid_mid,mid_right,bot_left,bot_mid]

class shape_dataset(Dataset,TorchDataset):
    def __init__(self, subset):
        self.labels=pd.read_csv(os.path.join(str(path_cut_dataset), (subset+".csv")))
        self.subset=subset
        self.data=[]
        self.transform= transforms.Compose(
             [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]
)
        i=0
        while i<len(self.labels):
                self.data.append((self.labels.iloc[i,0], self.labels.iloc[i,1], self.labels.iloc[i,2],
                                 self.labels.iloc[i,3], self.labels.iloc[i,4], self.labels.iloc[i,5],
                                 self.labels.iloc[i,6], self.labels.iloc[i,7], self.labels.iloc[i,8]))
                i+=1
    def __len__(self):
        return len(self.labels)
    def __getitem__(self,index):
        if type(index) is tuple:
            index=index[0]
        img_path= os.path.join(str(path_cut_images), (str(index)+".png"))

        with open(img_path,'rb') as f:
                img=Image.open(f)
                img.convert("RGB")
                # img = img.resize((20,20))
                if self.transform:
                    img=self.transform(img)
        #print(type(img))
        # print(img.shape)
        return img

    def to_query(self, i: int) -> Query:
        tensor_vars = []
        subs=dict()
        j = 0
        while j < 8:
            t = Term(f"p_{j}")
            subs[t] = Term("tensor",
                     Term(
                         self.subset,
                         Constant(self.data[i][j])))
            tensor_vars.append(t)
            j += 1
        return Query(Term("solution", *(x for x in tensor_vars), Constant(self.data[i][8])), subs)

train_dataset=shape_dataset("train")
test_dataset=shape_dataset("test")


if __name__ == '__main__':
    create_cut_dataset()
