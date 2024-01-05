from time import sleep
from pynvim import attach, api
import sys
import traceback


class InterpreterError(Exception):
    pass


def exec_script(cmd, globals=None, locals=None):
    try:
        exec(cmd, globals, locals)
    except SyntaxError as err:
        error_class = err.__class__.__name__
        detail = err.args[0]
        line_number = err.lineno
    except Exception as err:
        error_class = err.__class__.__name__
        detail = err.args and err.args[0]
        cl, exc, tb = sys.exc_info()
        line_number = traceback.extract_tb(tb)[-1][1]
    else:
        return
    print("%s at line %d: %s" % (error_class, line_number, detail))


nvim = attach(session_type="tcp", address="127.0.0.1", port="6666")
#event = api.nvim.Nvim.from_nvim(nvim)  # use the loaded nvim session

prev = ""
prev_buf = ""
while True:
    cbuf = nvim.current.buffer
    if prev != cbuf:
        print(f"Running {cbuf.name}")
        prev = cbuf
    sleep(5)
    # read and print contents of the whole buffer
    program = "\n".join(cbuf[:])
    if prev != program:
        exec_script(program, globals(), locals())
    prev = program
