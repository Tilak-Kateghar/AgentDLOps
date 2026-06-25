import os


class DockerAgent:

    def generate(
        self,
        model_name
    ):

        os.makedirs(
            "deployment",
            exist_ok=True
        )

        dockerfile = f"""
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
"""

        path = (
            f"deployment/"
            f"Dockerfile_{model_name}"
        )

        with open(
            path,
            "w"
        ) as file:

            file.write(
                dockerfile
            )

        return path