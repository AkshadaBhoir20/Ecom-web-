import pynvml 
pynvml.nvmlInit()
print("pynvml initialized successfully!")
pynvml.nvmlShutdown()
