from app.services.vector_memory import (
    VectorMemory
)

import uuid


class MemoryWriterAgent:

    def save_project_memory(
        self,
        intake_report,
        optimization_result
    ):

        memory_text = f"""
Project Type:
{intake_report['problem_type']}

Dataset Type:
{intake_report['dataset_type']}

Deployment Target:
{intake_report['deployment_target']}

Optimization Priority:
{intake_report['optimization_priority']}

Selected Architecture:
{optimization_result['best_architecture']['model']}

Architecture Accuracy:
{optimization_result['best_architecture']['accuracy']}

Learning Rate:
{optimization_result['best_hyperparameter']['learning_rate']}

Hyperparameter Accuracy:
{optimization_result['best_hyperparameter']['accuracy']}
"""

        memory = VectorMemory()

        memory.store(
            str(uuid.uuid4()),
            memory_text
        )

        return memory_text