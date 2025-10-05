#!/usr/bin/env python3
# run.py

import sys
import importlib
import traceback

MODULE_NAMES = ["jyr", "jyr"]

def try_import_module(names):
    for modname in names:
        try:
            mod = importlib.import_module(modname)
            print(f"[INFO] Imported module '{modname}'")
            return mod
        except Exception as e:
            print(f"[INFO] Could not import '{modname}': {e}")
    return None

def main():
    
    mod = try_import_module(MODULE_NAMES)
    if not mod:
        print("[ERROR] No module found (Jyr/jyr). Exiting...")
        sys.exit(1)

    
    if hasattr(mod, "aprov"):
        try:
            mod.aprov()
        except SystemExit:
            sys.exit(1)
        except Exception as e:
            print(f"[ERROR] Exception in 'aprov()': {e}")
            traceback.print_exc()
            sys.exit(2)
    else:
        print("[ERROR] 'aprov()' not found in module. Exiting...")
        sys.exit(3)

if __name__ == "__main__":
    main()



