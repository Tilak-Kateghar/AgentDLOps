from app.agents.architecture_benchmark_agent import (
    ArchitectureBenchmarkAgent
)

from app.services.benchmark_selector import (
    BenchmarkSelector
)

from app.agents.hyperparameter_agent import (
    HyperparameterAgent
)

from app.agents.hyperparameter_benchmark_agent import (
    HyperparameterBenchmarkAgent
)

from app.services.hyperparameter_selector import (
    HyperparameterSelector
)


class OptimizationAgent:

    def optimize(
        self,
        candidate_models
    ):

        architecture_benchmark_agent = (
            ArchitectureBenchmarkAgent()
        )

        benchmark_results = (
            architecture_benchmark_agent.benchmark(
                candidate_models
            )
        )

        benchmark_selector = (
            BenchmarkSelector()
        )

        best_architecture = (
            benchmark_selector.select_best(
                benchmark_results
            )
        )

        hyper_agent = (
            HyperparameterAgent()
        )

        trials = (
            hyper_agent.generate_trials(
                best_architecture[
                    "model"
                ]
            )
        )

        hyper_benchmark_agent = (
            HyperparameterBenchmarkAgent()
        )

        trial_results = (
            hyper_benchmark_agent.benchmark(
                best_architecture[
                    "model"
                ],
                trials
            )
        )

        selector = (
            HyperparameterSelector()
        )

        best_trial = (
            selector.select_best_trial(
                trial_results
            )
        )

        return {

            "best_architecture":
                best_architecture,

            "best_hyperparameter":
                best_trial,

            "architecture_results":
                benchmark_results,

            "hyperparameter_results":
                trial_results
        }