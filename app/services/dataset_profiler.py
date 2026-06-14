from pathlib import Path


class DatasetProfiler:
    """
    DatasetProfiler analyzes image datasets and
    generates basic statistics.
    """

    def __init__(self, dataset_path):
        self.dataset_path = Path(dataset_path)

    def count_classes(self):
        """
        Counts the number of class folders.
        """
        class_folders = [
            folder
            for folder in self.dataset_path.iterdir()
            if folder.is_dir()
        ]

        return len(class_folders)

    def count_images(self):
        """
        Counts all image files.
        """
        image_extensions = [".jpg", ".jpeg", ".png"]

        total_images = 0

        for class_folder in self.dataset_path.iterdir():

            if class_folder.is_dir():

                for image_file in class_folder.iterdir():

                    if image_file.suffix.lower() in image_extensions:
                        total_images += 1

        return total_images
    
    def class_distribution(self):
        """
        Counts images per class.
        """

        image_extensions = [".jpg", ".jpeg", ".png"]

        distribution = {}

        for class_folder in self.dataset_path.iterdir():

            if class_folder.is_dir():

                count = 0

                for image_file in class_folder.iterdir():

                    if image_file.suffix.lower() in image_extensions:
                        count += 1

                distribution[class_folder.name] = count

        return distribution

    def generate_report(self):
        """
        Generates dataset summary report.
        """
        report = {
            "dataset_path": str(self.dataset_path),
            "num_classes": self.count_classes(),
            "total_images": self.count_images(),
            "class_distribution": self.class_distribution()
        }

        return report