from typing import Any, Dict, Iterator, List

from doccano_client.models.example import Example
from doccano_client.repositories.example import ExampleRepository


class ExampleUseCase:
    def __init__(self, repository: ExampleRepository):
        self._repository = repository

    def find_by_id(self, project_id: int, example_id: int) -> Example:
        """Find a example by id

        Args:
            project_id (int): The id of the project to find
            example_id (int): The id of the example to find

        Returns:
            Example: The found example
        """
        return self._repository.find_by_id(project_id, example_id)

    def list(self, project_id: int) -> Iterator[Example]:
        """Return all examples

        Args:
            project_id (int): The id of the project

        Yields:
            Example: The examples in the project.
        """
        yield from self._repository.list(project_id)

    def create(
        self,
        project_id: int,
        text: str,
        meta: Dict[str, Any] = None,
    ) -> Example:
        """Create a new example

        Args:
            project_id (int): The id of the project
            text (str): The text of the example
            meta (Dict[str, Any]): The meta data of the example

        Returns:
            Example: The created example
        """
        if meta is None:
            meta = {}
        example = Example(text=text, meta=meta)
        return self._repository.create(project_id, example)

    def update(
        self,
        project_id: int,
        example_id: int,
        text: str = None,
        meta: Dict[str, Any] = None,
    ) -> Example:
        """Update a example

        Args:
            project_id (int): The id of the project
            example_id (int): The id of the example
            text (str): The text of the example
            meta (Dict[str, Any]): The meta data of the example

        Returns:
            Example: The updated example
        """
        example = self.find_by_id(project_id, example_id)
        example = Example(
            id=example_id,
            text=text if text is not None else example.text,
            meta=meta if meta is not None else example.meta,
        )
        return self._repository.update(project_id, example)

    def delete(self, project_id: int, example_id: int):
        """Delete a example.

        Args:
            project_id (int): The project id.
            example_id (int): The example id.
        """
        self._repository.delete(project_id, example_id)

    def bulk_delete(self, project_id: int, example_ids: List[int]):
        """Bulk delete examples

        Args:
            project_id (int): The id of the project
            example_ids (List[int]): The list of example ids to delete
        """
        self._repository.bulk_delete(project_id, example_ids)

    def delete_all(self, project_id: int):
        """Delete all examples

        Args:
            project_id (int): The id of the project
        """
        self._repository.delete_all(project_id)

    def update_state(self, project_id: int, example_id: int):
        """Update completed state of example

        Args:
            project_id (int): The id of the project
            example_id (int): The example id
        """
        self._repository.update_state(project_id, example_id)
