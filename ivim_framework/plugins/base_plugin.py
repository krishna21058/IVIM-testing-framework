from abc import ABC, abstractmethod

class BasePlugin(ABC):
    @abstractmethod
    def run_test(self, config):
        """
        Run the test using provided configuration.
        Must return a dict with test results.
        """
        pass
