import sys
import os


def check_if_pipe():
    if not sys.stdin.isatty():
        # stdin is NOT a terminal → input is being piped in
        data = sys.stdin.read().strip()
        return {"Status":True, "Data":data}
    else:
        # stdin is a terminal → no pipe
        return {"Status":False, "Data":None}

