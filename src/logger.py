import functools
import logging
from datetime import datetime
from pathlib import Path
from typing import Union

import pytz
from rich.logging import RichHandler

LOG_DIRECTORY = Path(__file__).parent / "log"
LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)
KST_TZ = pytz.timezone("Asia/Seoul")


def get_logger():
    log = logging.getLogger("rich")
    log.setLevel(logging.DEBUG)

    rich_formatter = logging.Formatter("%(message)s")
    file_formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s",
        # datefmt="%Y-%m-%d %H:%M:%S",
    )

    rich_handler = RichHandler(
        level=logging.DEBUG,
        rich_tracebacks=True,
        markup=True,
        log_time_format="[%Y-%m-%d %X]",
    )
    rich_handler.setFormatter(rich_formatter)

    log_time = datetime.now(KST_TZ).strftime("%Y-%m-%d %H;%M")
    log_filepath = LOG_DIRECTORY / f"{log_time}.log"
    file_handler = logging.FileHandler(log_filepath, encoding="utf-8")
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)

    log.addHandler(rich_handler)
    log.addHandler(file_handler)

    return log


def log(_func=None, *, my_logger: Union[logging.Logger, None] = None):
    def decorator_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = get_logger() if my_logger is None else my_logger

            # args_repr = [repr(a) for a in args]
            args_type = [type(a) for a in args]
            # kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            kwargs_type = [type(k) for k, v in kwargs.items()]
            logger.debug("args_type:", type(args_type), args_type)
            logger.debug("kwargs_type:", type(kwargs_type), kwargs_type)
            signature = ", ".join(args_type + kwargs_type)
            # signature = ", ".join(args_repr + kwargs_repr)
            logger.debug(f"function {func.__name__} called with args {signature}")
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                logger.exception(
                    f"Exception raised in {func.__name__}. exception: {str(e)}"
                )
                raise e

        return wrapper

    return decorator_log if _func is None else decorator_log(_func)
