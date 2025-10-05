try:
    import Jyr  
except ImportError as e:
    print("[ERROR] Compiled module nahi mila:", e)
    raise SystemExit

# Ye function ka naam wahi hona chahiye jo tu ne .pyx/.py me entry point banaya tha
try:
    aprov()  # start() ko apne main code me define kiya hona chahiye
except AttributeError:
    print("[ERROR] main.start() function nahi mila. Apna main module check karo.")

