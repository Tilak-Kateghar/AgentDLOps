from app.services.dataset_profiler import DatasetProfiler


def test_dataset_profiler():

    profiler = DatasetProfiler(
        "datasets/test_dataset"
    )

    report = profiler.generate_report()

    assert report["num_classes"] == 2
    assert report["total_images"] == 5

    print("DatasetProfiler Test Passed")


if __name__ == "__main__":
    test_dataset_profiler()