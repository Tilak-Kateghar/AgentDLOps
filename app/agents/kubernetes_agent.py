class KubernetesAgent:

    def generate_deployment(
        self,
        model_name,
        replicas=2
    ):

        deployment = {

            "apiVersion":
                "apps/v1",

            "kind":
                "Deployment",

            "metadata": {

                "name":
                    f"{model_name.lower()}-deployment"
            },

            "spec": {

                "replicas":
                    replicas,

                "selector": {

                    "matchLabels": {

                        "app":
                            model_name.lower()
                    }
                },

                "template": {

                    "metadata": {

                        "labels": {

                            "app":
                                model_name.lower()
                        }
                    },

                    "spec": {

                        "containers": [

                            {

                                "name":
                                    model_name.lower(),

                                "image":
                                    f"{model_name.lower()}:latest",

                                "ports": [

                                    {
                                        "containerPort":
                                            8000
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        }

        return deployment