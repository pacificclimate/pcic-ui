# PCIC style reference

`pcic_style_ref.py` generates the PCIC colour, typography, and web UI style reference PDF.

Requires Python 3 and Matplotlib (`python3 -m pip install matplotlib`).

Run:

```bash

python3 pcic_style_ref.py
```

This overwrites `PCIC-Style-Quick-Reference.pdf` in the current directory.
Myriad Pro is used when installed; otherwise, the script uses a sans-serif fallback.
