import json
import os


class ArtifactRegistryAgent:

    def __init__(self):

        self.registry_file = (
            "artifacts/model_registry.json"
        )

        os.makedirs(
            "artifacts",
            exist_ok=True
        )

    def register(
        self,
        model_name,
        version,
        accuracy
    ):

        artifact = {

            "model":
                model_name,

            "version":
                version,

            "accuracy":
                accuracy
        }

        data = []

        if os.path.exists(
            self.registry_file
        ):

            with open(
                self.registry_file,
                "r"
            ) as file:

                data = json.load(
                    file
                )

        data.append(
            artifact
        )

        with open(
            self.registry_file,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        return artifact