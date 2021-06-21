# FINAL

## How to set up adn run mu program
1.  Compile the program
```
$ sudo mbed compile --source . --source ~/ee2405/mbed-os/ -m B_L4S5I_IOT01A -t GCC_ARM --profile tflite.json -f
```

## How it work



### Line following BBcar
The line which the BBcar following can be detected two lines(left side and right sied), so I use find_lines to find the two lines and caculate the mid point of two lines' end. According to the coordinate of the mid point, the camera will send the moving dirction to BBcar throught UART. 
![](https://i.imgur.com/ObLbLcX.jpg)

### BBcar position calibration
Use camera to measure the angle and position of Apriltag surface, then determine car should go right or left.  
**ex:** If the apriltax is at "L" part then the car will turn right until the position of apriltag in the range from 75 to 85.
![](https://i.imgur.com/0DRsYFY.jpg)

