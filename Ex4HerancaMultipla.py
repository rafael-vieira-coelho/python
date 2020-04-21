class Foo(object):
    foo = 'attr foo of Foo'


class Bar(object):
    foo = 'attr foo of Bar'  # we won't see this. bar = 'attr bar of Bar'


class FooBar(Foo, Bar):
    foobar = 'attr foobar of FooBar'


if __name__ == '__main__':
    # Now if we instantiate FooBar, if we look up the foo attribute,
    # we see that Foo's attribute is found first
    fb = FooBar()
    print(fb.foo)
    print(FooBar.mro())
