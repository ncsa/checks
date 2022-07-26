#!/usr/bin/env python

import importlib
import json
import os
import time


# ----------------------------------------------------------------------
# MAIN FUNCTION
# ----------------------------------------------------------------------
def main():
    """
    Based on environment variables calls functions to check different
    services
    """
    tries = int(os.getenv("TRIES", 0))
    checks = json.load(open("checks.json"))

    for exit_code, check in enumerate(checks, start=1):
        args = dict()
        for env, key in check['parameters'].items():
            v = os.getenv(env)
            if v:
                args[key] = v

        if args:
            if "." in check['function']:
                mod_name, func_name = check['function'].rsplit('.', 1)
                mod = importlib.import_module(mod_name)
                func = getattr(mod, func_name)
            else:
                func = globals()[check['function']]
            check_func(tries, exit_code, func, **args)


def check_func(tries, exit_code, func, **kwargs):
    """
    Simple wrapper to call function. Tries to call the given function until
    the number of tries is done. If no more tries are left, it will exit the
    program with the given exit code.

    :param func: actual function to call
    :param exit_code: exit with exit_code
    :param tries: number of attempts before exiting
    :param kwargs: arguments for function
    :return:
    """
    while tries >= 0:
        try:
            if func(**kwargs):
                return
        except Exception as error:
            print('Error:', error.__class__.__name__, error)
        time.sleep(1)
        if tries == 1:
            break
        if tries > 0:
            tries = tries - 1
    exit(exit_code)


# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
