import traceback
from colored import DEFAULT, RED
from exceptions import (
    Exit,
)
try:
    from structure import (
        router,
        help_handler,
        exit_handler,
        register_handler,
        login_handler,
        send_message_handler,
        get_message_page_handler
    )
except ConnectionRefusedError:
    print(f"{RED}Connection refused{DEFAULT}")

router.register_route(
    command="/register",
    handle_func_ptr=register_handler.handle,
)
router.register_route(
    command="/login",
    handle_func_ptr=login_handler.handle,
)
router.register_route(
    command="/help",
    handle_func_ptr=help_handler.handle,
)
router.register_route(
    command="/send_message",
    handle_func_ptr=send_message_handler.handle,
)
router.register_route(
    command="/message_page",
    handle_func_ptr=get_message_page_handler.handle,
)
router.register_route(
    command="/exit",
    handle_func_ptr=exit_handler.handle,
)
if __name__ == "__main__":
    while True:
        try:
            from structure import app
            app.run()

        except (KeyboardInterrupt, Exit):
            print("\nGood Bye.")
            break
        except ConnectionRefusedError as err:
            print("Connection Refused.")
            break
        except Exception as err:
            traceback.print_exc()
            print(format(err))
