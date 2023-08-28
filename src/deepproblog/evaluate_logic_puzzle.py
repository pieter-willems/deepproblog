from collections import defaultdict
from statistics import mean
from typing import Optional

from deepproblog.dataset import Dataset
from deepproblog.model import Model
from deepproblog.utils.confusion_matrix import ConfusionMatrix


def get_double_confusion_matrix(
    model: Model, dataset: Dataset, verbose: int = 0, eps: Optional[float] = None
) -> (ConfusionMatrix, ConfusionMatrix):
    """

    :param model: The model to evaluate.
    :param dataset: The dataset to evaluate the model on.
    :param verbose: Set the verbosity. If verbose > 0, then print confusion matrix and accuracy.
    If verbose > 1, then print all wrong answers.
    :param eps: If set, then the answer will be treated as a float, and will be considered correct if
    the difference between the predicted and ground truth value is smaller than eps.
    :return: The confusion matrix when evaluating model on dataset.
    """
    confusion_matrix1 = ConfusionMatrix()
    confusion_matrix2 = ConfusionMatrix()
    model.eval()


    for i, gt_query in enumerate(dataset.to_queries()):
        print(f"At i={i}...")
        test_query = gt_query.variable_output()
        answer = model.solve([test_query])[0]
        actual = str(gt_query.output_values()[0])
        actual2 = str(gt_query.output_values()[1])
        if len(answer.result) == 0:
            predicted, predicted2 = "no_answer", "no_answer"
            if verbose > 1:
                print("no answer for query {}".format(gt_query))
        else:
            max_ans = max(answer.result, key=lambda x: answer.result[x])
            p = answer.result[max_ans]
            if eps is None:
                predicted = str(max_ans.args[gt_query.output_ind[0]])
                predicted2 = str(max_ans.args[gt_query.output_ind[1]])
            else:
                raise NotImplementedError
                # predicted = float(max_ans.args[gt_query.output_ind[0]])
                # actual = float(gt_query.output_values()[0])
                # if abs(actual - predicted) < eps:
                #     predicted = actual
            if verbose > 1 and actual != predicted:
                print(
                    "{} {} vs {}::{} for query {}".format(
                        i, actual, p, predicted, test_query
                    )
                )
        confusion_matrix1.add_item(predicted, actual)
        confusion_matrix2.add_item(predicted2, actual2)

    if verbose > 0:
        print(confusion_matrix1)
        print("Accuracy", confusion_matrix1.accuracy())

        print(confusion_matrix2)
        print("Accuracy", confusion_matrix2.accuracy())

    return [confusion_matrix1, confusion_matrix2]
