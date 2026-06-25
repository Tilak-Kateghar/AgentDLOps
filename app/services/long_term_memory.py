from app.services.vector_memory import (
    VectorMemory
)


class LongTermMemory:

    def __init__(self):

        self.architecture_memory = (
            VectorMemory(
                "architecture_memory"
            )
        )

        self.experiment_memory = (
            VectorMemory(
                "experiment_memory"
            )
        )

        self.deployment_memory = (
            VectorMemory(
                "deployment_memory"
            )
        )

        self.failure_memory = (
            VectorMemory(
                "failure_memory"
            )
        )

    def store(
        self,
        category,
        doc_id,
        text
    ):

        if category == "architecture":

            self.architecture_memory.store(
                doc_id,
                text
            )

        elif category == "experiment":

            self.experiment_memory.store(
                doc_id,
                text
            )

        elif category == "deployment":

            self.deployment_memory.store(
                doc_id,
                text
            )

        elif category == "failure":

            self.failure_memory.store(
                doc_id,
                text
            )

    def search(
        self,
        category,
        query
    ):

        if category == "architecture":

            return (
                self.architecture_memory.search(
                    query
                )
            )

        elif category == "experiment":

            return (
                self.experiment_memory.search(
                    query
                )
            )

        elif category == "deployment":

            return (
                self.deployment_memory.search(
                    query
                )
            )

        elif category == "failure":

            return (
                self.failure_memory.search(
                    query
                )
            )

        return {}