class BaseRepoException(Exception):
    def message(self):
        raise NotImplementedError