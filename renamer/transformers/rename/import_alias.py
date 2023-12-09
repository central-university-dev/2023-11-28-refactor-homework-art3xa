from typing import Union

import libcst as cst
from libcst import FlattenSentinel, ImportAlias, RemovalSentinel

from renamer.transformers.rename.base import BaseRenameTransformer


class RenameImportAliasTransformer(BaseRenameTransformer, cst.CSTTransformer):
    def leave_ImportAlias(  # noqa: N802
        self, original_node: "ImportAlias", updated_node: "ImportAlias",
    ) -> Union["ImportAlias", FlattenSentinel["ImportAlias"], RemovalSentinel]:
        """Rename import alias."""
        if original_node.name.value == self._old_name:
            return updated_node.with_changes(name=updated_node.name.with_changes(value=self._target_name))
        return original_node
