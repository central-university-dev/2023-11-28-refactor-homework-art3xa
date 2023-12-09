import libcst as cst
from libcst import BaseExpression, Name

from renamer.transformers.rename.base import BaseRenameTransformer


class RenameNameTransformer(BaseRenameTransformer, cst.CSTTransformer):
    def leave_Name(self, original_node: "Name", updated_node: "Name") -> "BaseExpression":  # noqa: N802
        """Rename name."""
        if original_node.value == self._old_name:
            return updated_node.with_changes(value=self._target_name)
        return original_node
