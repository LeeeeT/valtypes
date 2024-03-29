from valtypes.util import AutoCallSuper, super_endpoint


def test_automatically_calls_method_of_super_class_in_child_classes() -> None:
    class Base(AutoCallSuper):
        Base_received_args: tuple[tuple[object, ...], dict[str, object]]

        @super_endpoint
        def f(self, *args: object, **kwargs: object) -> None:
            self.Base_received_args = args, kwargs

    class A(Base):
        A_received_args: tuple[tuple[object, ...], dict[str, object]]

        def f(self, *args: object, **kwargs: object) -> None:
            self.A_received_args = args, kwargs

    class B(Base):
        B_received_args: tuple[tuple[object, ...], dict[str, object]]

        def f(self, *args: object, **kwargs: object) -> None:
            self.B_received_args = args, kwargs

    class C(B, A):
        C_received_args: tuple[tuple[object, ...], dict[str, object]]

        def f(self, *args: object, **kwargs: object) -> None:
            self.C_received_args = args, kwargs

    instance = C()
    instance.f(1, a=2)

    assert instance.Base_received_args == instance.A_received_args == instance.B_received_args == instance.C_received_args == ((1,), {"a": 2})


def test_supports_any_callables() -> None:
    class F:
        def __call__(self, a: int, /, *, b: int) -> None:
            pass

    class Base(AutoCallSuper):
        f = super_endpoint(F())

    class Derived(Base):
        f = F()

    Derived().f(1, b=2)


def test_calls_methods_of_each_class_in_hierarchy_exactly_once() -> None:
    class Base(AutoCallSuper):
        Base_count = 0

        @super_endpoint
        def f(self) -> None:
            self.Base_count += 1

    class A(Base):
        pass

    class B(Base):
        A_count = 0

        def f(self) -> None:
            self.A_count += 1

    class C(B, A):
        pass

    instance = C()
    instance.f()

    assert instance.Base_count == instance.A_count == 1
