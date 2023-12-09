import libcst as cst
from libcst import BaseExpression, Call

from renamer.transformers.rename.base import BaseRenameTransformer


class RenameCallTransformer(BaseRenameTransformer, cst.CSTTransformer):
    def leave_Call(self, original_node: "Call", updated_node: "Call") -> "BaseExpression":  # noqa: N802
        """Rename call."""
        if original_node.func.value == self._old_name:
            return updated_node.with_changes(func=updated_node.func.with_changes(value=self._target_name))
        return original_node
