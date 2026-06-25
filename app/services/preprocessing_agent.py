class PreprocessingAgent:

    def recommend(
        self,
        quality_report
    ):

        status = quality_report[
            "quality_status"
        ]

        if status == "low_data":

            return {

                "augmentation":
                    True,

                "normalization":
                    True,

                "strategy":
                    "heavy_augmentation"
            }

        return {

            "augmentation":
                False,

            "normalization":
                True,

            "strategy":
                "standard"
        }