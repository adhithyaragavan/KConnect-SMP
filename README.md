
## Memory Regions Identified

From the active process memory map, the following four primary segments were located and verified:

* **Text Segment (`r-xp`)** *Pathname:* `/home/adhithyaragavan/Documents/KConnect/memlayout`  
    *Purpose:* Stores the compiled machine code instructions of the program. It is read-only to prevent runtime modification and executable so the CPU can run it.

* **Heap Segment (`rw-p`)** *Pathname:* `[heap]`  
    *Purpose:* Used for dynamic memory allocation at runtime (e.g., using `malloc`). It grows upwards toward higher memory addresses as memory is requested.

* **Stack Segment (`rw-p`)** *Pathname:* `[stack]`  
    *Purpose:* Automatically manages memory for function execution. It stores local variables, parameters, and function return addresses, growing downwards from high memory addresses.

* **Shared Libraries (`r-xp`, `r--p`, etc.)** *Pathname:* `/usr/lib64/libc.so.6`  
    *Purpose:* Maps standard C library functions (like `printf` and `sleep`) into the process's memory space, saving system resources by sharing a single copy across multiple running programs.
