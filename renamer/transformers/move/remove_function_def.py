import libcst as cst
from libcst import BaseExpression, BaseStatement, Call, FunctionDef, RemovalSentinel


class RemoveFunctionDefTransformer(cst.CSTTransformer):
    def __init__(self, name: str, to_file_path: str) -> None:
        super().__init__()
        self._name = name
        self._to_file_path = to_file_path
        self.function_def = None

    def leave_FunctionDef(self, original_node: "FunctionDef", updated_node: "FunctionDef") -> "BaseStatement":
        """Rename function definition."""
        if updated_node.name.value == self._name:
            self.function_def = updated_node
            return RemovalSentinel.REMOVE
        return updated_node

    def leave_Call(self, original_node: "Call", updated_node: "Call") -> "BaseExpression":
        """Rename function call."""
        if updated_node.func.value == self._name:
            return updated_node.with_changes(func=self._create_function_call().deep_clone())
        return updated_node

    def _create_function_call(self) -> cst.Attribute:
        return cst.Attribute(value=cst.Name(value=self._to_file_path), attr=cst.Name(value=self._name))
