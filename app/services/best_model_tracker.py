class BestModelTracker:

    def __init__(self):

        self.best_accuracy = 0

    def is_best(
        self,
        accuracy
    ):

        if accuracy > self.best_accuracy:

            self.best_accuracy = accuracy

            return True

        return False