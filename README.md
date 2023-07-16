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
 
<br>!Capture<br> 
Create a folder to store all the required assets 
 
<br>!Capture<br> 
Under ...... ensure your Domain is 1 and your preferred netowrk adaptor is Ethernet 11  
 
<br>!Capture<br> 
Configure the ip address your laptop's Ethernet 11 to 192.168.254.27 
 
<br>Insert image of PB video layers<br> 
Add the required amount of video layers under the server(Desktop xxx) as shown in the image below by right-clicking the server -> add device -> add video laye 
 
 
 
<h3>Step 2: Setting up Christie Pandora Box Server Management</h3> 
<h3>Step 3: Connecting to Christie Pandora Box to Christie Pandora Box Server Management</h3> 
 
``` 
``` 
var cardString1 = ""  
cardString1 = Phidgets_PhidgetRFID5.TagString  
If cardString1.IsMatch("010775a7cc") {  
 DeviceSetParam(3,1,"Opacity",0) DeviceSetParam(3,2,"X Pos",4)  
 DeviceSetParam(3,2,"Y Pos",-3) DeviceSetParam(3,2,"Z Pos",2)  
 DeviceSetParam(3,2,"Z







