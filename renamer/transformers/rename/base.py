import libcst as cst


class BaseRenameTransformer(cst.CSTTransformer):
    def __init__(self, old_name: str, target_name: str) -> None:
        super().__init__()
        self._old_name = old_name
        self._target_name = target_name
