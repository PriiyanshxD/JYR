try:
    import menu  # ye main.cpython-312.so ko load karega
except ImportError as e:
    print("[ERROR] Compiled module nahi mila:", e)
    raise SystemExit

# Ye function ka naam wahi hona chahiye jo tu ne .pyx/.py me entry point banaya tha
try:
    menu.main.menu()  # start() ko apne main code me define kiya hona chahiye
except AttributeError:
    print("[ERROR] main.start() function nahi mila. Apna main module check karo.")
