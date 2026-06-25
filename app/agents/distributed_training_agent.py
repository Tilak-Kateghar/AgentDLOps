class DistributedTrainingAgent:

    def create_cluster(
        self,
        model_name,
        workers=4
    ):

        cluster = []

        for worker_id in range(
            workers
        ):

            cluster.append({

                "worker":

                    worker_id + 1,

                "status":
                    "Ready",

                "assigned_model":
                    model_name
            })

        return {

            "strategy":
                "Data Parallel",

            "workers":
                cluster,

            "total_workers":
                workers
        }