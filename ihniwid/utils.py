__all__ = ('chunks', 'last')


def chunks(it, size: int):
    """Group iterator items into chunks of given size.

    This is like https://doc.rust-lang.org/std/primitive.slice.html#method.chunks,
    or the grouper example from itertools.
    """

    l = []
    for item in it:
        l.append(item)
        if len(l) == size:
            yield l
            l = []
    if l:
        # The last chunk may be shorter than the other ones.
        yield l


def last(it, default=None):
    """Get the last value from an iterator."""
    value = default
    for value in it:
        pass
    return value
