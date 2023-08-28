from json import dumps

import torch

from deepproblog.dataset import DataLoader
from deepproblog.engines import ApproximateEngine, ExactEngine
from deepproblog.evaluate import get_confusion_matrix
from deepproblog.examples.MNIST.network import MNIST_Net
from deepproblog.puzzle_solver_test2.toy_dataset import toy_problem, ToyDataset
from deepproblog.model import Model
from deepproblog.network import Network
from deepproblog.train import train_model
from deepproblog.utils.standard_networks import SmallNet

method = "exact"

name = "toyProblem_{}".format(method)

train_data = ToyDataset(size=1000)
test_data = ToyDataset(size=100)

train_set = toy_problem(train_data, "train")
test_set = toy_problem(test_data, "test")

network = SmallNet(num_classes=5)
net = Network(network, "toy_net", batching=True)
net.optimizer = torch.optim.Adam(network.parameters(), lr=1e-3)

model = Model("toy_problem.pl", [net])
if method == "exact":
    model.set_engine(ExactEngine(model), cache=True)
elif method == "geometric_mean":
    model.set_engine(
        ApproximateEngine(model, 1, ApproximateEngine.geometric_mean, exploration=False)
    )

model.add_tensor_source("train", train_data)
model.add_tensor_source("test", test_data)

loader = DataLoader(train_set, 10, True)
train = train_model(model, loader, 3, log_iter=10, profile=0)
print('oi')
# model.save_state("snapshot/" + name + ".pth")
train.logger.comment(dumps(model.get_hyperparameters()))
train.logger.comment(
    "Accuracy {}".format(get_confusion_matrix(model, test_set, verbose=1).accuracy())
)
train.logger.write_to_file("log/" + name)
