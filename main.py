import traceback
from structure import app
from exceptions import (
    Exit,
    BadInput
)

if __name__ == "__main__":
    while True:
        try:
            app.run()

        except (KeyboardInterrupt, Exit):
            print("\nGood Bye.")
            break
        except Exception as err:
            traceback.print_exc()
            print(format(err))
