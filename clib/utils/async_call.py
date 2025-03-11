import ctypes
import threading


class _NONE: ...


class AsyncCallManager:
    class AsyncCall:
        def __init__(self, func, args, kwargs, start=True):
            self.result = _NONE
            self.error = _NONE
            self.thread = threading.Thread(target=self._run, args=(func, args, kwargs), daemon=True)
            self.event = threading.Event()
            if start:
                self.thread.start()

        def _run(self, func, args, kwargs):
            try:
                self.result = func(*args, **kwargs)
            except Exception as e:
                self.error = e
            self.event.set()

        def is_done(self):
            return self.event.is_set()

        def wait(self, timeout=None):
            self.event.wait(timeout)
            if not self.event.is_set():
                raise TimeoutError
            if self.error is not _NONE:
                raise self.error
            return self.result

        def terminate(self):
            if ctypes.pythonapi.PyThreadState_SetAsyncExc(self.thread.ident, ctypes.py_object(SystemExit)) != 1:
                raise RuntimeError("PyThreadState_SetAsyncExc failed")

    def __init__(self):
        self.calls = {}

    def is_calling(self, call_id):
        return call_id in self.calls and not self.calls[call_id].is_done()

    def is_done(self, call_id):
        return call_id in self.calls and self.calls[call_id].is_done()

    def call(self, call_id, func, *args, _stop_old=False, **kwargs):
        if self.is_calling(call_id):
            if _stop_old:
                self.calls[call_id].terminate()
            else:
                raise RuntimeError(f"call {call_id} is already running")
        self.calls[call_id] = self.AsyncCall(func, args, kwargs)

    def get_result(self, call_id):
        if not self.is_done(call_id):
            raise RuntimeError(f"call {call_id} is not done")
        return self.calls.pop(call_id).wait(0)

    def terminate(self, call_id):
        if call_id in self.calls:
            self.calls[call_id].terminate()
            self.calls.pop(call_id)
