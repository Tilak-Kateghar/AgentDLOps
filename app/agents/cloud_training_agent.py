class CloudTrainingAgent:

    def create_job(
        self,
        intake_report,
        training_plan
    ):

        return {

            "job_id":
                "JOB_001",

            "provider":
                "AWS",

            "instance":
                "g4dn.xlarge",

            "gpu":
                "NVIDIA T4",

            "status":
                "Queued",

            "dataset":
                intake_report[
                    "dataset_type"
                ],

            "model":
                training_plan[
                    "selected_model"
                ]
        }