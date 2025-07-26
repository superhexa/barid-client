from typing import Callable, TypeVar, ParamSpec, Coroutine, Any, get_origin, get_args
import functools

P = ParamSpec("P")
R = TypeVar("R")

def is_not_none(func: Callable[P, Coroutine[Any, Any, R]]) -> Callable[P, Coroutine[Any, Any, R]]:
    """
    Decorator to ensure that the decorated async function does not return None.

    Parameters
    ----------
    func : Callable
        The async function to decorate.

    Returns
    -------
    Callable
        Wrapped function that raises ValueError if result is None.
    """
    @functools.wraps(func)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        res = await func(*args, **kwargs)
        if res is None:
            raise ValueError(f"{func.__name__} returned None")
        return res
    return wrapper

def type_check(expected_type: type):
    """
    Decorator to ensure the decorated async function returns an instance of expected_type.
    Supports generics like List[Email].

    Parameters
    ----------
    expected_type : type
        The expected return type.

    Returns
    -------
    Callable
        Decorator that performs the type check.
    """
    def decorator(func: Callable[..., Coroutine[Any, Any, Any]]):
        @functools.wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            res = await func(*args, **kwargs)

            origin = get_origin(expected_type)
            args_ = get_args(expected_type)

            if origin is list and args_:
                if not isinstance(res, list) or not all(isinstance(i, args_[0]) for i in res):
                    raise TypeError(f"{func.__name__} must return List[{args_[0].__name__}]")
            elif origin is dict and args_:
                if not isinstance(res, dict) or not all(isinstance(k, args_[0]) and isinstance(v, args_[1]) for k, v in res.items()):
                    raise TypeError(f"{func.__name__} must return Dict[{args_[0].__name__}, {args_[1].__name__}]")
            elif origin is None:
                if not isinstance(res, expected_type):
                    raise TypeError(f"{func.__name__} must return {expected_type.__name__}")
            else:
                raise TypeError(f"{func.__name__}: Unsupported type {expected_type}")

            return res
        return wrapper
    return decorator

def trace_call(func: Callable[P, Coroutine[Any, Any, R]]) -> Callable[P, Coroutine[Any, Any, R]]:
    """
    Decorator to print trace messages when entering and exiting the async function.

    Parameters
    ----------
    func : Callable
        The async function to decorate.

    Returns
    -------
    Callable
        Wrapped function that logs entry and exit.
    """
    @functools.wraps(func)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        res = await func(*args, **kwargs)
        return res
    return wrapper
