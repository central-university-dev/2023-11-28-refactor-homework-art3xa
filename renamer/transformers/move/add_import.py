import libcst as cst
from libcst import BaseStatement, FunctionDef


class AddImportTransformer(cst.CSTTransformer):
    def __init__(self, name: str, to_file_path: str) -> None:
        super().__init__()
        self._name = name
        self._to_file_path = to_file_path

    def leave_Module(self, original_node: "FunctionDef", updated_node: "FunctionDef") -> "BaseStatement":  # noqa: N802
        """Rename function definition."""
        new_body = [self._create_import()]
        new_body.extend(updated_node.body)
        return updated_node.with_changes(body=new_body)

    def _create_import(self) -> cst.Import:
        import_alias = cst.ImportAlias(name=cst.Name(value=self._to_file_path), asname=None)
        import_statement = cst.Import(names=[import_alias])
        return cst.SimpleStatementLine(body=[import_statement])
