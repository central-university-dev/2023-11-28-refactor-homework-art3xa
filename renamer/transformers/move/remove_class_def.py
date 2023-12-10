from libcst import BaseStatement, ClassDef, RemovalSentinel

from renamer.transformers.move.remove_def_base import RemoveDefBaseTransformer


class RemoveClassDefTransformer(RemoveDefBaseTransformer):
    def leave_ClassDef(self, original_node: "ClassDef", updated_node: "ClassDef") -> "BaseStatement":  # noqa: N802
        """Rename class definition."""
        if updated_node.name.value == self._name:
            self.define = updated_node
            return RemovalSentinel.REMOVE
        return updated_node
