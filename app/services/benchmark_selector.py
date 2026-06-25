class BenchmarkSelector:

    def select_best(
        self,
        benchmark_results
    ):

        return max(
            benchmark_results,
            key=lambda x: x["accuracy"]
        )