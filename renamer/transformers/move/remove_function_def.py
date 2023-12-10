from libcst import BaseStatement, FunctionDef, RemovalSentinel

from renamer.transformers.move.remove_def_base import RemoveDefBaseTransformer


class RemoveFunctionDefTransformer(RemoveDefBaseTransformer):
    def leave_FunctionDef(self, original_node: "FunctionDef", updated_node: "FunctionDef") -> "BaseStatement":
        """Rename function definition."""
        if updated_node.name.value == self._name:
            self.define = updated_node
            return RemovalSentinel.REMOVE
        return updated_node
