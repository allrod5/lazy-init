from lazy_init import util


class LazyProxy:
    lazy_instances = {}
    class_attributes = (
        '__lazy_proxy__provider__',
        '__lazy_proxy__instance__',
    )

    def __init__(self, provider: function):
        """
        LazyProxy behaves as a transparent proxy to another object
        except that the real object will only be initialized when
        actually used.

        :param provider: function that takes no mandatory arguments
                         and provides an instance of the real object
        """
        util.check_provider(provider)
        LazyProxy.lazy_instances[self] = {
            '__lazy_proxy__provider__': provider,
            '__lazy_proxy__instance__': None,
        }

    def __getattribute__(self, item):
        self_attributes = LazyProxy.lazy_instances[self]
        if self_attributes['__lazy_proxy__instance__'] is None:
            self_attributes['__lazy_proxy__instance__'] = (
                self_attributes['__lazy_proxy__provider__'].__call__())

        instance = self_attributes['__lazy_proxy__instance__']
        return instance.__getattribute__(item)
