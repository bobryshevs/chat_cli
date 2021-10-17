from structure import app


if __name__ == "__main__":
    while True:
        try:
            app.run()
        except KeyboardInterrupt:
            print("\nGood Bye.")
            break
        except Exception as err:
            print(format(err))
