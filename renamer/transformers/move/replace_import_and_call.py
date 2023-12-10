from typing import Union

import libcst as cst
from libcst import BaseExpression, Call, FlattenSentinel, ImportAlias, RemovalSentinel


class ReplaceImportAndCallTransformer(cst.CSTTransformer):
    def __init__(self, name: str, from_file_path: str, to_file_path: str) -> None:
        super().__init__()
        self._name = name
        self._from_file_path = from_file_path
        self._to_file_path = to_file_path
        self.need_to_replace = True

    def leave_ImportAlias(
        self, original_node: "ImportAlias", updated_node: "ImportAlias",
    ) -> Union["ImportAlias", FlattenSentinel["ImportAlias"], RemovalSentinel]:
        """Rename function definition."""
        if updated_node.name.value == self._from_file_path:
            return updated_node.with_changes(name=cst.Name(value=self._to_file_path))
        return updated_node

    def leave_Call(self, original_node: "Call", updated_node: "Call") -> "BaseExpression":
        """Rename function call."""
        if updated_node.func.value.value == self._from_file_path:
            return updated_node.with_changes(func=self._create_function_call().deep_clone())
        return updated_node

    def _create_function_call(self) -> cst.Attribute:
        return cst.Attribute(value=cst.Name(value=self._to_file_path), attr=cst.Name(value=self._name))
