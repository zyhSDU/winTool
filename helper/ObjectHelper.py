def get_object_str(self):
    f"{type(self).__name__}("
    f"{', '.join('%s=%s' % item for item in vars(self).items())}"
    f")"


def print_object(self, file=None):
    print(
        get_object_str(self),
        file=file,
    )


class Object(object):
    def __str__(self):
        return get_object_str(self)
