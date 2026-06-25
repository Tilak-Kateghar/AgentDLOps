class MemoryAgent:

    def create_memory_record(

        self,

        project_type,

        dataset_type,

        deployment_target,

        optimization_priority,

        architecture,

        learning_rate,

        accuracy
    ):

        return f"""
Project Type:
{project_type}

Dataset Type:
{dataset_type}

Deployment Target:
{deployment_target}

Optimization Priority:
{optimization_priority}

Architecture:
{architecture}

Learning Rate:
{learning_rate}

Accuracy:
{accuracy}
"""