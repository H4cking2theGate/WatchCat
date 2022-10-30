from .rules import RuleManager
from .code import CodeManager


class WatchCat:

    def __init__(self, rule_path: str):
        self.rule: RuleManager = RuleManager()
        self.manager: CodeManager

        self.rule.load_yaml_rules(path=rule_path)

    def run(self, mode: int) -> None:
        """
        程序入口。
        """
        pass
