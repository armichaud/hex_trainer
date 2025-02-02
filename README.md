# Hex Trainer
While learning about low-level programming and assembly, I found myself slowing down every time I encountered hex codes as representations of stack addresses and offsets. I wanted to build a small tool with which to improve my ability to translate hexidecimal to decimal values and do mental math with hexidecimal values.

As of 2/1/25, this is a work in progress.

## API
The primary means of using the trainer is a FastAPI-based app, ready to be served from a docker container with `docker-compose up`.
The API is served at `localhost:8000`. To view the list of routes and their schemata, load the `/docs` route in a browser.

## CLI
The easiest way to interact with the trainer is through the cli tool I built. 
The simplest way to access it is to just start the API container, `exec` into it, 
and run the commands below.

```
# Given a hexidecimal value, you will be prompted for its decimal equivalent.
python hex_trainer.py hex-to-int

# Given a decimal value, you will be prompted for its hexidecimal equivalent.
python hex_trainer.py int-to-hex

# After selecting which operators you'd like to train with,
# you'll be prompted for the solution to an equation using hexidecimal values.
python hex_trainer.py solve-equation
```

## Features I'd Like to Implement
- Deploy production API
- Option to answer equation in hexidecimal
- Better error handling, e.g. failed conversion to/from hex
