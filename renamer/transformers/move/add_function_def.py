import libcst as cst
from libcst import BaseExpression, BaseStatement, Call, FunctionDef


class AddFunctionDefTransformer(cst.CSTTransformer):
    def __init__(self, name: str, function_def: cst.FunctionDef) -> None:
        super().__init__()
        self._name = name
        self.function_def = function_def

    def leave_Module(self, original_node: "FunctionDef", updated_node: "FunctionDef") -> "BaseStatement":
        """Rename function definition."""
        new_body = []
        if self.function_def:
            new_body.append(self.function_def)
        new_body.extend(updated_node.body)
        return updated_node.with_changes(body=new_body)

    def leave_Call(self, original_node: "Call", updated_node: "Call") -> "BaseExpression":
        """Rename function call."""
        if self.function_def and self._name in (updated_node.func.value, updated_node.func.attr.value):
            return updated_node.with_changes(func=self._create_function_call().deep_clone())
        return updated_node

    def _create_function_call(self) -> cst.Name:
        return cst.Name(value=self._name)
