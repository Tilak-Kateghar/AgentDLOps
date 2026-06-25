class ProjectIntakeAgent:

    def collect_requirements(
        self,
        problem_type,
        problem_statement,
        expected_outcome,
        dataset_type,
        deployment_target,
        optimization_priority
    ):

        return {

            "problem_type":
                problem_type,

            "problem_statement":
                problem_statement,

            "expected_outcome":
                expected_outcome,

            "dataset_type":
                dataset_type,

            "deployment_target":
                deployment_target,

            "optimization_priority":
                optimization_priority
        }