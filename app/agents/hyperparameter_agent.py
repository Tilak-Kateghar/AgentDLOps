class HyperparameterAgent:

    def generate_trials(
        self,
        model_name
    ):

        trials = [

            {
                "learning_rate":
                    0.001,

                "batch_size":
                    32
            },

            {
                "learning_rate":
                    0.0005,

                "batch_size":
                    32
            },

            {
                "learning_rate":
                    0.0001,

                "batch_size":
                    32
            }
        ]

        return trials