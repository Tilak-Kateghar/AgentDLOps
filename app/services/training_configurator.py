class TrainingConfigurator:

    def generate_config(
        self,
        dataset_report,
        selected_model
    ):

        dataset_size = dataset_report[
            "dataset_size"
        ]

        config = {}

        # ---------------------
        # Epochs
        # ---------------------

        if dataset_size == "small":
            config["epochs"] = 2

        elif dataset_size == "medium":
            config["epochs"] = 2

        else:
            config["epochs"] = 2

        # ---------------------
        # Batch Size
        # ---------------------

        if selected_model == "MobileNetV3":
            config["batch_size"] = 64

        elif selected_model == "EfficientNetB0":
            config["batch_size"] = 32

        else:
            config["batch_size"] = 16

        config["optimizer"] = "Adam"

        return config