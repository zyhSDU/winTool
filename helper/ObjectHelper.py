def print_object(self, file=None):
    print(
        f"{type(self).__name__}("
        f"{', '.join('%s=%s' % item for item in vars(self).items())}"
        f")",
        file=file,
    )
