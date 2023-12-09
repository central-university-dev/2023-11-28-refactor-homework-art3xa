from typing import Union

import libcst as cst
from libcst import BaseStatement, FlattenSentinel, FunctionDef, RemovalSentinel

from renamer.transformers.rename.base import BaseRenameTransformer


class RenameFunctionDefTransformer(BaseRenameTransformer, cst.CSTTransformer):
    def leave_FunctionDef(  # noqa: N802
        self, original_node: "FunctionDef", updated_node: "FunctionDef",
    ) -> Union["BaseStatement", FlattenSentinel["BaseStatement"], RemovalSentinel]:
        """Rename function definition."""
        if original_node.name and original_node.name.value == self._old_name:
            return updated_node.with_changes(name=updated_node.name.with_changes(value=self._target_name))
        return original_node
