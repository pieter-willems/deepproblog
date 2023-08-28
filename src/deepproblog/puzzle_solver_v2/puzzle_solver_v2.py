import torch
from deepproblog.evaluate import get_confusion_matrix
from deepproblog.evaluate_logic_puzzle import  get_double_confusion_matrix
from deepproblog.dataset import DataLoader
from deepproblog.puzzle_solver_v2.dataset import test_dataset, train_dataset
from deepproblog.network import Network
from deepproblog.utils.standard_networks import smallnet
from deepproblog.model import Model
from deepproblog.engines import ApproximateEngine, ExactEngine
from deepproblog.train import train_model

batch_size = 10
loader = DataLoader(train_dataset, batch_size)


puzzle_net = smallnet(num_classes=9, pretrained=True)
net = Network(puzzle_net, "puzzle_net", batching=True)
net.optimizer = torch.optim.Adam(puzzle_net.parameters(), lr=1e-4)
#net.optimizer =torch.optim.SGD(puzzle_net.parameters(), lr=1e-3)

colour_net=smallnet(num_classes=6, pretrained= True)
net2 = Network(colour_net, "colour_net",batching=True)
net2.optimizer = torch.optim.Adam(colour_net.parameters(), lr=1e-4)


model = Model("puzzle_solver_simplified_v2.pl", [net, net2])

model.add_tensor_source("train", train_dataset)
model.add_tensor_source("test", test_dataset)

#model.set_engine(
#        ApproximateEngine(model, 1, ApproximateEngine.geometric_mean, exploration=False)
#    )
model.set_engine(ExactEngine(model), cache=True)

train = train_model(model, loader, 1, log_iter=1, profile=0)
#print("Accuracy {}".format(get_confusion_matrix(model, test_dataset, verbose=1).accuracy()))
get_double_confusion_matrix(model, test_dataset, verbose=1)