from typing import Dict, List, Set


class ReverseIndex:
    """
    A class that implements a reverse index for a collection of documents.
    """

    def __init__(self) -> None:
        """
        Initialize an empty reverse index.
        """
        self.index: Dict[str, Set[int]] = {}

    def add_document(self, doc_id: int, content: str) -> None:
        """
        Add a document to the reverse index.

        Args:
            doc_id (int): The unique identifier of the document.
            content (str): The content of the document.
        """
        words = content.lower().split()
        for word in words:
            if word not in self.index:
                self.index[word] = set()
            self.index[word].add(doc_id)

    def search(self, query: str) -> List[int]:
        """
        Search for documents containing all words in the query.

        Args:
            query (str): The search query.

        Returns:
            List[int]: A list of document IDs that contain all words in the query.
        """
        query_words = query.lower().split()
        if not query_words:
            return []

        result_sets = [self.index.get(word, set()) for word in query_words]
        return list(set.intersection(*result_sets))
