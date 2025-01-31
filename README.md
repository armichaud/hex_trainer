# Hex Trainer
While learning about low-level programming and assembly, I found myself slowing down every time I encountered hex codes as representations of stack addresses and offsets. I wanted to build a small tool with which to improve my ability to translate hexidecimal to decimal values and do mental math with hexidecimal values.

As of 1/31/25, this is a work in progress.

## CLI
The most basic way to interact with the trainer is through the cli tool I built. See usage below:

```
# Given a hexidecimal value, you will be prompted for its decimal equivalent.
python hex_trainer.py hex-to-int

# After selecting which operators you'd like to train with,
# you'll be prompted for the solution to an equation using hexidecimal values.
python hex_trainer.py solve-equation
```

## API
I've developed a FastAPI based API as the backend for a browser-based SPA I hope to create. Next step is to serve the API from a docker container.

## Features I'd Like to Implement
- Int-to-hex: given a decimal value, give the hexidecimal equivalent
- CLI Unit Testing
- Browser-based UI
- Containerization of API and UI
- Better error handling, e.g. failed conversion to/from hex
