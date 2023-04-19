import pandas as pd
from torch.utils.data import Dataset as TorchDataset
from deepproblog.dataset import Dataset
from deepproblog.query import Query
import os
from PIL import Image
import csv

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
            img = Image.open(img_path)
            l=cut_puzzle(img)

            top_left_name='puzzle_' + str(i) + '_tl.png'
            l[0].save(os.path.join(path_cut_images,top_left_name))

            top_middle_name = 'puzzle_' + str(i) + '_tm.png'
            l[1].save(os.path.join(path_cut_images, top_middle_name))

            top_right_name = 'puzzle_' + str(i) + '_tr.png'
            l[2].save(os.path.join(path_cut_images, top_right_name))

            middle_left_name = 'puzzle_' + str(i) + '_ml.png'
            l[3].save(os.path.join(path_cut_images, middle_left_name))

            middle_middle_name = 'puzzle_' + str(i) + '_mm.png'
            l[4].save(os.path.join(path_cut_images, middle_middle_name))

            middle_right_name = 'puzzle_' + str(i) + '_mr.png'
            l[5].save(os.path.join(path_cut_images, middle_right_name))

            bottom_left_name = 'puzzle_' + str(i) + '_bl.png'
            l[6].save(os.path.join(path_cut_images, bottom_left_name))

            bottom_middle_name = 'puzzle_' + str(i) + '_bm.png'
            l[7].save(os.path.join(path_cut_images, bottom_middle_name))

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
    def __init__(self,  csv_file, imagedir, transform=None):
        self.labels=pd.read_csv(csv_file)
        self.transform= transform
        self.imagedir=imagedir
    def __len__(self):
        return len(self.labels)
    def __getitem__(self,index):
        img_path = os.path.join(self.imagedir,self.labels.iloc[index,0])
        with open(img_path,'rb') as f:
                img=Image.open(f)
        l = cut_puzzle(img)
        shape = self.labels.iloc[index, 1]
        if self.transform:
            for x in l:
                self.transform(l[x])
        #l.append(shape)
        return l, shape
    def to_query(self, i: int) -> Query:
        pass

if __name__ == '__main__':
    print(os.path.join(os.path.expanduser('~') , 'PycharmProjects' , 'deepproblog_pieter' , 'src','deepproblog','Puzzle_solver_v1'))
    print(os.getcwd())
    create_cut_dataset()
