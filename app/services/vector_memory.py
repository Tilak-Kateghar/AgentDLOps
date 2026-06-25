# import chromadb


# class VectorMemory:

#     def __init__(self):

#         self.client = chromadb.PersistentClient(
#             path="memory_db"
#         )

#         self.collection = (
#             self.client.get_or_create_collection(
#                 name="agentdlops_memory"
#             )
#         )

#     def store(
#         self,
#         doc_id,
#         text
#     ):

#         self.collection.add(
#             ids=[str(doc_id)],
#             documents=[text]
#         )

#     def add_document(
#         self,
#         doc_id,
#         text
#     ):

#         self.store(
#             doc_id,
#             text
#         )

#     def search(
#         self,
#         query,
#         n_results=3
#     ):

#         return self.collection.query(
#             query_texts=[query],
#             n_results=n_results
#         )

import chromadb


class VectorMemory:

    def __init__(
        self,
        collection_name="agentdlops_memory"
    ):

        self.client = (
            chromadb.PersistentClient(
                path="memory_db"
            )
        )

        self.collection = (
            self.client.get_or_create_collection(
                name=collection_name
            )
        )

    def store(
        self,
        doc_id,
        text
    ):

        self.collection.add(
            ids=[str(doc_id)],
            documents=[text]
        )

    def add_document(
        self,
        doc_id,
        text
    ):

        self.store(
            doc_id,
            text
        )

    def search(
        self,
        query,
        n_results=3
    ):

        return self.collection.query(
            query_texts=[query],
            n_results=n_results
        )