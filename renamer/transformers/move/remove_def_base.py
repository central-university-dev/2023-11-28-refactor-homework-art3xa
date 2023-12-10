import libcst as cst
from libcst import BaseExpression, Call


class RemoveDefBaseTransformer(cst.CSTTransformer):
    def __init__(self, name: str, to_file_path: str) -> None:
        super().__init__()
        self._name = name
        self._to_file_path = to_file_path
        self.define = None

    def leave_Call(self, original_node: "Call", updated_node: "Call") -> "BaseExpression":
        """Rename function call."""
        if updated_node.func.value == self._name:
            return updated_node.with_changes(func=self._create_new_call().deep_clone())
        return updated_node

    def _create_new_call(self) -> cst.Attribute:
        return cst.Attribute(value=cst.Name(value=self._to_file_path), attr=cst.Name(value=self._name))
