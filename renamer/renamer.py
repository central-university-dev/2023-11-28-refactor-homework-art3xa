import libcst as cst

from renamer.base.file import File
from renamer.base.project import Project
from renamer.transformers.rename.call import RenameCallTransformer
from renamer.transformers.rename.class_def import RenameClassDefTransformer
from renamer.transformers.rename.function_def import RenameFunctionDefTransformer
from renamer.transformers.rename.import_alias import RenameImportAliasTransformer
from renamer.transformers.rename.name import RenameNameTransformer


class Renamer:
    def __init__(self, project: Project, file: File) -> None:
        """Initialize Renamer."""
        self.project = project
        self.file = file

    def rename_function(self, old_name: str, target_name: str) -> list[str]:
        """Rename function definition."""
        rename_function_def_transformer = RenameFunctionDefTransformer(old_name, target_name)
        return self._rename_define(old_name, target_name, rename_function_def_transformer)

    def rename_class(self, old_name: str, target_name: str) -> list[str]:
        """Rename class definition."""
        rename_class_def_transformer = RenameClassDefTransformer(old_name, target_name)
        return self._rename_define(old_name, target_name, rename_class_def_transformer)

    def _rename_define(
        self, old_name: str, target_name: str, rename_define_transformer: cst.CSTTransformer,
    ) -> list[str]:
        rename_call_transformer = RenameCallTransformer(old_name, target_name)
        rename_import_alias_transformer = RenameImportAliasTransformer(old_name, target_name)
        result = []
        for file in self.project.get_python_files():
            original_tree = cst.parse_module(file.read())
            renamed_tree = original_tree.visit(rename_define_transformer)
            renamed_tree = renamed_tree.visit(rename_call_transformer)
            renamed_tree = renamed_tree.visit(rename_import_alias_transformer)
            result.append(renamed_tree.code)
        return result

    def rename_variable(self, old_name: str, target_name: str) -> list[str]:
        """Rename variable."""
        rename_name_transformer = RenameNameTransformer(old_name, target_name)
        result = []
        for file in self.project.get_python_files():
            original_tree = cst.parse_module(file.read())
            renamed_tree = original_tree.visit(rename_name_transformer)
            result.append(renamed_tree.code)
        return result
