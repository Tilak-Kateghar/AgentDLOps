class SageMakerAgent:

    def create_training_job(
        self,
        model_name,
        dataset
    ):

        return {

            "job_name":
                f"{model_name}_training",

            "service":
                "AWS SageMaker",

            "instance_type":
                "ml.g4dn.xlarge",

            "dataset":
                dataset,

            "status":
                "InProgress"
        }

    def register_model(
        self,
        model_name
    ):

        return {

            "model":
                model_name,

            "registry":
                "SageMaker Model Registry",

            "status":
                "Registered"
        }

    def deploy_endpoint(
        self,
        model_name
    ):

        return {

            "model":
                model_name,

            "endpoint":
                f"{model_name}-endpoint",

            "status":
                "InService"
        }