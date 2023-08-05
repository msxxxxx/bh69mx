from threading import(
    current_thread,
    main_thread,
    Thread,
    Barrier,
    Timer,
    Event,
    Lock,
    RLock,
    Semaphore,
    activeCount,
    get_ident
)
from threading import enumerate as threading_enumerate


def foo():
    for _ in range(10):
        print(current_thread().name)

if __name__ ==