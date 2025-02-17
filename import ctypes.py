import ctypes

MessageBoxA = ctypes.windll.user32.MessageBoxA
NULL = 0 
MB_OK = 0

MessageBoxA(NULL, ctypes.c_char_p(b"Hello from python."), ctypes.c_char_p("bAlert"), MB_OK)