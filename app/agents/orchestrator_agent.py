from app.services.optimization_pipeline import (
    OptimizationPipeline
)

from app.agents.memory_writer_agent import (
    MemoryWriterAgent
)

from app.agents.project_history_agent import (
    ProjectHistoryAgent
)

from app.agents.explainability_agent import (
    ExplainabilityAgent
)

from app.agents.experiment_tracking_agent import (
    ExperimentTrackingAgent
)

from app.services.global_status import (
    tracker
)

from app.agents.consensus_agent import (
    ConsensusAgent
)

class OrchestratorAgent:

    def run(
        self,
        intake_report
    ):

        pipeline = (
            OptimizationPipeline()
        )

        # ------------------------------
        # Architect + Optimization
        # ------------------------------

        tracker.update(
            "ArchitectAgent",
            "Running"
        )

        tracker.update(
            "OptimizationAgent",
            "Running"
        )

        optimization_result = (
            pipeline.execute(
                intake_report
            )
        )

        tracker.update(
            "ArchitectAgent",
            "Completed"
        )

        tracker.update(
            "OptimizationAgent",
            "Completed"
        )

        consensus_agent = (
            ConsensusAgent()
        )

        consensus_result = (
            consensus_agent.decide(

                llm_choice=
                    optimization_result[
                        "candidate_result"
                    ][
                        "candidates"
                    ][0],

                benchmark_choice=
                    optimization_result[
                        "best_architecture"
                    ][
                        "model"
                    ]
            )
        )

        # ------------------------------
        # Experiment Tracking
        # ------------------------------

        tracker.update(
            "ExperimentTrackingAgent",
            "Running"
        )

        experiment_tracker = (
            ExperimentTrackingAgent()
        )

        tracking_result = (
            experiment_tracker.track(
                intake_report,
                optimization_result
            )
        )

        tracker.update(
            "ExperimentTrackingAgent",
            "Completed"
        )

        # ------------------------------
        # Memory Writer
        # ------------------------------

        tracker.update(
            "MemoryAgent",
            "Running"
        )

        memory_writer = (
            MemoryWriterAgent()
        )

        memory_writer.save_project_memory(
            intake_report,
            optimization_result
        )

        tracker.update(
            "MemoryAgent",
            "Completed"
        )

        # ------------------------------
        # Project History
        # ------------------------------

        history_agent = (
            ProjectHistoryAgent()
        )

        history_agent.save_run(
            intake_report,
            optimization_result
        )

        # ------------------------------
        # Explainability
        # ------------------------------

        tracker.update(
            "ExplainabilityAgent",
            "Running"
        )

        explainability_agent = (
            ExplainabilityAgent()
        )

        explanation = (
            explainability_agent.explain(
                optimization_result
            )
        )

        tracker.update(
            "ExplainabilityAgent",
            "Completed"
        )

        return {
            "consensus":
                consensus_result,

            "tracking":
                tracking_result,

            "optimization":
                optimization_result,

            "explanation":
                explanation
        }