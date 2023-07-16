# EGL315-AY23-24

## Software Required:<br>
Christie Pandora Box 8.6.1<br> 
Christie Pandora Box Server Management 1.5.0<br>
Widget Designer Unlimited 6.5.6<br>
GrandMA on PC 1.9.2.2<br>

## Hardware Required:<br>
Pandora Box license dongle x 2<br>
Passive speaker (JBL css 1st) x 2<br>
grandMA3 console(Insert Model Number) x 1<br>
Laptop (HP ZBook 15 G5) x 1<br>
TV monitor (Samsung UE46A ) x 1<br>
RFID reader (Phidget 1023) x 2<br>
USB hub (ATZ UH3102) x 1<br>
DMX transmitter (micro f-1 lite G5) x 4<br>
Media Server(HP Workstation) x1<br>
Network switch (netgear FS108) x 1<br>
Acrylic sheet (80x70cm) x 1<br>
Lanscape board (84x58cm) x 1<br>
DMX splitter (MDRT DMX512) x 2<br>
USB type C to female LAN adapter x 2<br>

## Cables Required:<br>
HDMI cable x 2<br>
5-pin female to 5-pin male XLR cable x 6<br>
3.5mm to 4 bear end cable x 1<br>
LAN cable x 4<br>

## Controls Diagram
(Insert Control Diagram here)<br>
The system has 3 main part: input, process, output, being laptop, server, monitor respectively.The laptop as the processor and the TV monitor as the output. The RFID reader sends input data when it detects the RfiD card, sends it to the laptop to process the data and will output the result on the TV monitor.

## Video Diagram
(Insert Video Diagram here)<br>
The laptop is connected to the server through the network switch via LAN. It is able to send video to the server due to the softwares Christie Pandora Box and Christie Pandora Box Server Management being connected to each other. THe server then sends video signal to the audio de-embedder via HDMI, the audio de-embedder then seperates the audio and video signal in the HDMI connection and sends only video signal to the TV monitor via HDMI connection. 


## Lighting Diagram
(Insert Lighting Diagram Here)<br>
THe grandMA3 acts as the input and processing device to control the lights. It sends DMX signal (a type of signal that controls lights) to 2 DMX splitter, which then sends DMX signal to 4 DMX transmitter, 2 per splitter. The DMX transmitter then sends DMX signal to the DMX receiver on the hoist wirelessly, controlling the lights.

## Audio Diagram
(Insert Diagram Here)<br>
The Laptop sends video and audio signal to the audio de-embedder via HDMI connection. The audio de-embedder then extracts the audio signal and sends it to the amplifier, connected via the 3.5mm jack to terminal block. The amplifier then sends the audio signal to the 2 passive speakers, resulting in audio playing.

## Control Setup (Hardware)
<h3>Step 1: Connect the laptop to USB hub via USB type A - USB type B 3.0</h3>
<h3>Step 2: Connect the RFID readers to USB hub via USB type A - USB type B 2.0</h3>
<h3>Step 3: Connect the phidget to USB hub via USB type A - USB mini</h3>

## Control Setup (Software)
<h3>Step 1: Setting up Widget Designer</h3>
<h3>Step 2:</h3>
<h3>Step 3:</h3>
<h3>Step 4:</h3>


## Video Setup (Hardware)
<h3>Step 1:</h3>
<h3>Step 2:</h3>
<h3>Step 3:</h3>
<h3>Step 4:</h3>

## Video Setup (Software)
<h3>Step 1: Setting up Christie Pandora Box</h3>

<br>![Capture](Thumbnails/Media.PNG)<br>
Create a folder to store all the required assets

<br>![Capture](Thumbnails/Capture.PNG)<br>
Under ...... ensure your Domain is 1 and your preferred netowrk adaptor is Ethernet 11 

<br>![Capture](Thumbnails/IP.PNG)<br>
Configure the ip address your laptop's Ethernet 11 to 192.168.254.27

<br>![Capture](Thumbnails/layers.png)<br>
Add the required amount of video layers under the server(Desktop xxx) as shown in the image below by right-clicking the server -> add device -> add video layer

<h3>Step 2: Setting up Christie Pandora Box Server Management</h3>

<br>![Capture](Thumbnails/PBServer.png)<br>
Ensure that your server is on the same ip subnet, being 192.168.254.25 and select Ethernet 11 under Adaptor options 

<h3>Step 3: Connecting to Christie Pandora Box to Christie Pandora Box Server Management</h3>

```
var cardString1 = "" 
cardString1 = Phidgets_PhidgetRFID5.TagString 
If cardString1.IsMatch("010775a7cc") { 
 DeviceSetParam(3,1,"Opacity",0) DeviceSetParam(3,2,"X Pos",4) 
 DeviceSetParam(3,2,"Y Pos",-3) DeviceSetParam(3,2,"Z Pos",2) 
 DeviceSetParam(3,2,"Z Scale",0.660) DeviceSetParam(3,2,"Y Scale",0.660) 
 DeviceSetParam(3,2,"X Scale",0.660) DeviceSetParam(3,2,"RGB Key|Mix",255) 
 WDWait(0.5) DeviceSetParam(3,2,"Opacity",255) 
 DeviceSetParam(3,3,"Opacity",0) DeviceSetParam(3,4,"Opacity",0) 
 DeviceSetParam(3,5,"Opacity",0) DeviceSetMedia(3,2,1,15) 
 DeviceSetParam(3,2,"Playback Transport","Play")  WDWait(5.0) 
 DeviceSetParam(3,2,"Playback Transport","Pause")  DeviceSetParam(3,3,"Playback Transport","Stop") 
 DeviceSetParam(3,4,"Playback Transport","Stop")   DeviceSetParam(3,5,"Playback Transport","Stop") 
 PhidgetRFID5IsReady = True 
 playRollDiceVideo() 
} 

Elseif cardString1.IsMatch("010775a07a") { 
 DeviceSetParam(3,1,"Opacity",0) DeviceSetParam(3,3,"X Pos",2) 
 DeviceSetParam(3,3,"Z Scale",0.750) DeviceSetParam(3,3,"Y Scale",0.750) 
 DeviceSetParam(3,3,"X Scale",0.750) DeviceSetParam(3,3,"RGB Key|Mix",255) 
 WDWait(0.5) DeviceSetParam(3,2,"Opacity",0) 
 DeviceSetParam(3,3,"Opacity",255) DeviceSetParam(3,4,"Opacity",0) 
 DeviceSetParam(3,5,"Opacity",0) DeviceSetMedia(3,3,1,9) 
 DeviceSetParam(3,3,"Playback Transport","Play")  WDWait(5.0) 
 DeviceSetParam(3,3,"Playback Transport","Pause")  DeviceSetParam(3,2,"Playback Transport","Stop")  
 DeviceSetParam(3,4,"Playback Transport","Stop")  DeviceSetParam(3,5,"Playback Transport","Stop")  
} 
Elseif cardString1.IsMatch("01077575bb") { DeviceSetParam(3,1,"Opacity",0) 
 DeviceSetParam(3,4,"X Pos",2) DeviceSetParam(3,4,"Z Scale",0.750) 
 DeviceSetParam(3,4,"Y Scale",0.750) DeviceSetParam(3,4,"X Scale",0.750) 
 DeviceSetParam(3,4,"RGB Key|Mix",255) WDWait(0.5) 
 DeviceSetParam(3,2,"Opacity",0) DeviceSetParam(3,3,"Opacity",0) 
 DeviceSetParam(3,4,"Opacity",255) DeviceSetParam(3,5,"Opacity",0) 
 DeviceSetMedia(3,4,1,6) DeviceSetParam(3,4,"Playback Transport","Play")  
 WDWait(5.0) DeviceSetParam(3,4,"Playback Transport","Pause")  
 DeviceSetParam(3,2,"Playback Transport","Stop")  DeviceSetParam(3,3,"Playback Transport","Stop")  
 DeviceSetParam(3,5,"Playback Transport","Stop") } 
Elseif cardString1.IsMatch("01077584cd") { 
 DeviceSetParam(3,1,"Opacity",0) DeviceSetParam(3,5,"X Pos",2) 
 DeviceSetParam(3,5,"Z Scale",0.750) DeviceSetParam(3,5,"Y Scale",0.750) 
 DeviceSetParam(3,5,"X Scale",0.750) DeviceSetParam(3,5,"RGB Key|Mix",255) 
 WDWait(0.5) DeviceSetParam(3,2,"Opacity",0) 
 DeviceSetParam(3,3,"Opacity",0) DeviceSetParam(3,4,"Opacity",0) 
 DeviceSetParam(3,5,"Opacity",255) DeviceSetMedia(3,5,1,10) 
 DeviceSetParam(3,5,"Playback Transport","Play")  WDWait(5.0) 
 DeviceSetParam(3,5,"Playback Transport","Pause")  DeviceSetParam(3,2,"Playback Transport","Stop")  
 DeviceSetParam(3,3,"Playback Transport","Stop")  DeviceSetParam(3,4,"Playback Transport","Stop")  
}
```

## **Dagger Edits** 

[![Watch the video](Assets/thumbnails/AttackDagger.jpg)](https://www.youtube.com/watch?v=DiMfWIs8LUc) 

A short attacking animation video of daggerman 

[![Watch the video](Assets/thumbnails/DaggerCombV1.jpg)](https://youtu.be/xPTUq8ydhzo)

A full death animation video of daggerman 

[![Watch the video](Assets/thumbnails/DaggerCombVic.jpg)](https://youtu.be/zA-caRkYX9w)

A full victory animation video of daggerman 

[![Watch the video](Assets/thumbnails/DaggerDeathv1.jpg)](https://youtu.be/shDJ2hvP4XM)

A death animation video of daggerman 

[![Watch the video](Assets/thumbnails/DaggerIdleV1.jpg)](https://youtu.be/bo7_ZhQ19j4)

An idle animation video of daggerman  

[![Watch the video](Assets/thumbnails/DaggerVP.jpg)](https://youtu.be/eGG7mUD-HII)

A spawn animation video of daggerman

[![Watch the video](Assets/thumbnails/DaggerVP.jpg)](https://youtu.be/eLfmyesCC1E)

A walking animation video of daggerman
 








