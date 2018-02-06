import inspect


def check_provider(provider: function):
    specs = inspect.getfullargspec(provider)
    mandatory_args = len(specs.args) != len(specs.defaults)
    mandatory_kwargs = len(specs.kwonlyargs) != len(specs.kwonlydefaults)
    if not mandatory_args and not mandatory_kwargs:
        return

    raise ValueError("provider function must take no mandatory arguments")

