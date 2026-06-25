class ArchitectureSwitcher:

    def switch(
        self,
        architecture_review,
        training_plan
    ):

        new_plan = (
            training_plan.copy()
        )

        new_model = (
            architecture_review[
                "selected_model"
            ]
        )

        new_plan[
            "selected_model"
        ] = new_model

        if new_model == "ResNet50":

            new_plan[
                "batch_size"
            ] = 16

        elif new_model == "EfficientNetB0":

            new_plan[
                "batch_size"
            ] = 32

        else:

            new_plan[
                "batch_size"
            ] = 64

        return new_plan