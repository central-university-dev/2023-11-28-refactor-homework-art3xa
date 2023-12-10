import libcst as cst

from renamer.base.file import File
from renamer.base.project import Project
from renamer.transformers.move.add_function_def import (
    AddCallAndDefTransformer,
)
from renamer.transformers.move.replace_import_and_call import ReplaceImportAndCallTransformer
from renamer.transformers.move.add_import import AddImportTransformer
from renamer.transformers.move.remove_function_def import RemoveFunctionDefTransformer
from renamer.transformers.move.remove_class_def import RemoveClassDefTransformer


class Move:
    def __init__(self, project: Project, from_file: File, to_file: File) -> None:
        self.project = project
        self.from_file = from_file
        self.to_file = to_file

    def move_function(self, name: str) -> list[str]:
        """Move function definition."""
        removed_module, function_def = self.remove_function(name)
        added_module = self.add_function(name, function_def)
        result = []
        for file in self.project.get_python_files():
            if str(file.path) == str(self.from_file.path):
                result.append(removed_module.code)
            elif str(file.path) == str(self.to_file.path):
                result.append(added_module.code)
            else:
                original_tree = cst.parse_module(file.read())
                replace_import_transformer = ReplaceImportAndCallTransformer(
                    name, self._create_import_path(self.from_file.path), self._create_import_path(self.to_file.path)
                )
                updated_tree = original_tree.visit(replace_import_transformer)
                result.append(updated_tree.code)
        return result

    def remove_function(self, name: str) -> (cst.Module, cst.FunctionDef):
        """Remove function definition and add import."""
        import_path = self._create_import_path(self.to_file.path)
        move_function_def_transformer = RemoveFunctionDefTransformer(name, import_path)
        add_import_transformer = AddImportTransformer(name, import_path)
        original_tree = cst.parse_module(self.from_file.read())
        removed_tree = original_tree.visit(move_function_def_transformer)
        removed_tree = removed_tree.visit(add_import_transformer)
        return removed_tree, move_function_def_transformer.define

    def add_function(self, name: str, function_def: cst.FunctionDef) -> cst.Module:
        """Add function definition."""
        add_call_and_def_transformer = AddCallAndDefTransformer(name, function_def)
        original_tree = cst.parse_module(self.to_file.read())
        return original_tree.visit(add_call_and_def_transformer)

    def _create_import_path(self, path: str) -> str:
        return str(path)[len(str(self.project.path)) + 1 :].replace("/", ".").replace(".py", "")

    def remove_class(self, name: str) -> (cst.Module, cst.ClassDef):
        """Remove function definition and add import."""
        import_path = self._create_import_path(self.to_file.path)
        move_class_def_transformer = RemoveClassDefTransformer(name, import_path)
        add_import_transformer = AddImportTransformer(name, import_path)
        original_tree = cst.parse_module(self.from_file.read())
        removed_tree = original_tree.visit(move_class_def_transformer)
        removed_tree = removed_tree.visit(add_import_transformer)
        return removed_tree, move_class_def_transformer.define

    def add_class(self, name: str, class_def: cst.ClassDef) -> cst.Module:
        """Add function definition."""
        add_call_and_def_transformer = AddCallAndDefTransformer(name, class_def)
        original_tree = cst.parse_module(self.to_file.read())
        return original_tree.visit(add_call_and_def_transformer)

    def move_class(self, name: str) -> list[str]:
        """Move function definition."""
        removed_module, class_def = self.remove_class(name)
        added_module = self.add_class(name, class_def)
        result = []
        for file in self.project.get_python_files():
            if str(file.path) == str(self.from_file.path):
                result.append(removed_module.code)
            elif str(file.path) == str(self.to_file.path):
                result.append(added_module.code)
            else:
                original_tree = cst.parse_module(file.read())
                replace_import_transformer = ReplaceImportAndCallTransformer(
                    name, self._create_import_path(self.from_file.path), self._create_import_path(self.to_file.path)
                )
                updated_tree = original_tree.visit(replace_import_transformer)
                result.append(updated_tree.code)
        return result