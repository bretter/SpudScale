
#SpudScale

SpudScale is a tool used to collect data from several CPW-Plus scales simultaneously.
It combines identification data entered by the user with data streamed in on a COM port and writes it all to a .csv file.

##Running

To run the program, navigate to the base directory and execute:
```python src/GUI.py```

##Dependencies

- python3
- pySerial
- pyyaml

##Notes

Although it was designed to interface with a specific model of scale it could easily be modified to collect data from any source that writes to a COM port.
