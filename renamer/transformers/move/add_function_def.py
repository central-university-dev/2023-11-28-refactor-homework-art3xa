import libcst as cst
from libcst import BaseExpression, BaseStatement, Call, FunctionDef


class AddCallAndDefTransformer(cst.CSTTransformer):
    def __init__(self, name: str, func_or_class_def: cst.FunctionDef) -> None:
        super().__init__()
        self._name = name
        self.func_or_class_def = func_or_class_def

    def leave_Module(self, original_node: "FunctionDef", updated_node: "FunctionDef") -> "BaseStatement":  # noqa: N802
        """Rename function definition."""
        new_body = []
        if self.func_or_class_def:
            new_body.append(self.func_or_class_def)
        new_body.extend(updated_node.body)
        return updated_node.with_changes(body=new_body)

    def leave_Call(self, original_node: "Call", updated_node: "Call") -> "BaseExpression":  # noqa: N802
        """Rename function call."""
        if self.func_or_class_def and self._name in (updated_node.func.value, updated_node.func.attr.value):
            return updated_node.with_changes(func=cst.Name(value=self._name))
        return updated_node

