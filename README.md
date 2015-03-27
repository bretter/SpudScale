#Project Objective
The goal of this project is to collect and organize input from several scales and a human user.
The data needs to be in a format that can be easily imported into Excel.

##Assumptions
- There will always be exactly 10 scales
- All data will be present at time of collection (scales loaded, user input completed)
- Values will be displayed as they are collected
- Scale configuration/identity will not change after initial setup *(ID comes from scale or USB-to-RS232 Adapter???)*

#Physical Components

##Inventory
- (1) Laptop
- (10) Scales
- (10) USB-to-RS232 Adapters
- (10) CAT5 Cables
- (20) CAT5-to-USB Adapters
- (1) USB Hub

##Connection Scheme
The following describes the physical connection of each scale to the laptop (note: the USB hub is shared by all scales):
> Scale RS232 Port<->USB-to-RS232<->CAT5-to-USB<->CAT5 Cable<->CAT5-to-USB<->USB Hub<->Laptop USB Port

#Program Objects:
- scale
  - *(str)identity*
  - *(double)currentValue*
- row
  - *(str)rowNum*
  - [((str)field, scale)]
  - getScaleValues()
  - formattedRow()
- interface
  - getRowNum()
  - showLastValues()
  - showPreviousValues()
  - writeRow()
  - readConfig()
  - makeConfig()
- file writer
  - recordNewRow()
