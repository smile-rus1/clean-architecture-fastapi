from src.domain.common.constants.empty import Empty


def data_filter(**kwargs):
    filtering = {}

    for name, value in kwargs.items():
        if isinstance(value, Empty) or value is None:
            continue
        filtering[name] = value

    return filtering
