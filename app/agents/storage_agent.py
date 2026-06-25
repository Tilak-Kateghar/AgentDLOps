import os

from supabase import (
    create_client,
    Client
)

from dotenv import (
    load_dotenv
)

load_dotenv()


class StorageAgent:

    def __init__(self):

        self.url = os.getenv(
            "SUPABASE_URL"
        )

        self.key = os.getenv(
            "SUPABASE_KEY"
        )

        self.client: Client = (
            create_client(
                self.url,
                self.key
            )
        )

    def upload_file(
        self,
        bucket,
        local_file_path,
        remote_file_name=None
    ):

        if remote_file_name is None:

            remote_file_name = os.path.basename(
                local_file_path
            )

        with open(
            local_file_path,
            "rb"
        ) as file:

            try:

                self.client.storage.from_(
                    bucket
                ).upload(
                    path=remote_file_name,
                    file=file
                )

            except Exception:

                file.seek(0)

                self.client.storage.from_(
                    bucket
                ).update(
                    path=remote_file_name,
                    file=file
                )

        return {

            "bucket": bucket,

            "file": remote_file_name,

            "status": "uploaded"
        }