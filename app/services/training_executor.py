import torch

from app.services.training_state import (
    TrainingState
)

class TrainingExecutor:

    def forward_pass(
        self,
        model,
        train_loader
    ):

        model.eval()

        images, labels = next(
            iter(train_loader)
        )

        with torch.no_grad():

            outputs = model(images)

        return {
            "input_shape": tuple(images.shape),
            "output_shape": tuple(outputs.shape)
        }

    def train_one_epoch(
        self,
        model,
        train_loader,
        optimizer,
        criterion
    ):

        model.train()

        total_loss = 0
        batch_count = 0

        for images, labels in train_loader:

            outputs = model(images)

            loss = criterion(
                outputs,
                labels
            )

            optimizer.zero_grad()

            loss.backward()

            optimizer.step()

            total_loss += loss.item()

            batch_count += 1

            if batch_count >= 100:
                break

        average_loss = (
            total_loss / batch_count
        )

        return {
            "average_loss": average_loss,
            "batches_trained": batch_count
        }

    def train_multiple_epochs(
        self,
        model,
        train_loader,
        optimizer,
        criterion,
        epochs,
        model_name="UnknownModel"
    ):

        history = []

        training_tracker = (
            TrainingState()
        )

        for epoch in range(epochs):

            print(
                f"Starting Epoch {epoch + 1}"
            )

            result = self.train_one_epoch(
                model,
                train_loader,
                optimizer,
                criterion
            )

            loss = (
                result[
                    "average_loss"
                ]
            )

            history.append({

                "epoch":
                    epoch + 1,

                "loss":
                    loss
            })

            training_tracker.update(

                model=model_name,

                epoch=epoch + 1,

                loss=loss,

                accuracy=0,

                status="Training"
            )

            print(
                "TRAINING STATUS UPDATED:",
                model_name,
                epoch + 1,
                loss
            )

            print(
                f"Epoch {epoch+1}/{epochs} "
                f"- Loss: "
                f"{loss:.4f}"
            )

        training_tracker.update(

            model=model_name,

            epoch=epochs,

            loss=loss,

            accuracy=0,

            status="Completed"
        )

        return history

    def evaluate_accuracy(
        self,
        model,
        test_loader
    ):

        model.eval()

        correct = 0
        total = 0

        with torch.no_grad():

            for images, labels in test_loader:

                outputs = model(images)

                _, predicted = torch.max(
                    outputs,
                    1
                )

                total += labels.size(0)

                correct += (
                    predicted == labels
                ).sum().item()

        accuracy = (
            100 * correct / total
        )

        return {
            "accuracy": accuracy
        }

    def collect_predictions(
        self,
        model,
        test_loader
    ):

        model.eval()

        y_true = []
        y_pred = []

        with torch.no_grad():

            for images, labels in test_loader:

                outputs = model(images)

                _, predictions = torch.max(
                    outputs,
                    1
                )

                y_true.extend(
                    labels.tolist()
                )

                y_pred.extend(
                    predictions.tolist()
                )

        return {
            "y_true": y_true,
            "y_pred": y_pred
        }