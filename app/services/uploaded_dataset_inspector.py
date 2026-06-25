import os


class UploadedDatasetInspector:

    def inspect(
        self,
        file_path
    ):

        extension = (
            os.path.splitext(
                file_path
            )[1].lower()
        )

        if extension == ".csv":

            return {

                "dataset_type":
                    "tabular",

                "format":
                    "csv"
            }

        elif extension == ".zip":

            return {

                "dataset_type":
                    "image",

                "format":
                    "zip"
            }

        return {

            "dataset_type":
                "unknown",

            "format":
                extension
        }