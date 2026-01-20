from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    async def generate(self, prompt: str, model: str, parameters: dict, state: dict = None):
        pass
