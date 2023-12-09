from typing import Union

import libcst as cst
from libcst import BaseStatement, ClassDef, FlattenSentinel, RemovalSentinel

from renamer.transformers.rename.base import BaseRenameTransformer


class RenameClassDefTransformer(BaseRenameTransformer, cst.CSTTransformer):
    def leave_ClassDef(  # noqa: N802
        self, original_node: "ClassDef", updated_node: "ClassDef",
    ) -> Union["BaseStatement", FlattenSentinel["BaseStatement"], RemovalSentinel]:
        """Rename class definition."""
        bases_list = []
        for base in original_node.bases:
            base_value = base.value.value
            if base_value == self._old_name:
                bases_list.append(base.with_changes(value=base.value.with_changes(value=self._target_name)))
            else:
                bases_list.append(base)
        updated_node = updated_node.with_changes(bases=bases_list)
        if original_node.name.value == self._old_name:
            updated_node = updated_node.with_changes(bases=bases_list)
            return updated_node.with_changes(name=updated_node.name.with_changes(value=self._target_name))
        return updated_node
