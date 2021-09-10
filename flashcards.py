import random
from multiple_choice_question import mcq
class Ports:
    q = ["Port 21","Port 22","Port 23","Port 25","Port 53","Port 80","Port 110","Port 161/162","Port 143","Port 443","port 3389", "Port 137-139","Port  139/445", "Port 427","Port 548","Port 67/68","Port 389","Port 1812/1813","FTP","SSH","Telnet","SMTP","DNS","HTTP","POP3","SNMP","IMAP","HTTPS","RDP","NetBIOS/NetBT","SMB/CIFS","SLP","AFP","DHCP","LDAP","RADIUS"]
    a =["FTP","SSH","Telnet","SMTP","DNS","HTTP","POP3","SNMP","IMAP","HTTPS","RDP","NetBIOS/NetBT","SMB/CIFS","SLP","AFP","DHCP","LDAP","RADIUS","Port 21","Port 22","Port 23","Port 25","Port 53","Port 80","Port 110", "Port 161/162","Port 143","Port 443","port 3389", "Port 137-139","Port 139/445", "Port 427","Port 548","Port 67/68","Port 389","Port 1812/1813"]
    def question_or_answer():
        i = random.randrange(0,2)
        return i
class MultipleChoice:
    #Not totally sure, but some sort of JSON might be more efficient.
    q0= mcq(q="You need to install a TV tuner adapter in a computer. All of the following steps are necessary EXCEPT...",a1="Plugging the audio cable into the TV tuner adapter card and sound card.",a2="Plugging the TV tuner adapter into a PCI slot",a3="Plugging the antena into the TV tuner card.",a4="Plugging the TV tuner into a USB port",a5="",ca="d")

    q1 = mcq(q="What is the network prefix used to denote an unsubnetted Class C IP address?",a1="/8",a2="/24",a3="/16",a4="/32",a5="",ca="b")

    q2= mcq(q="Your laser printer repeatedly prints vertical lines through the page. What is the probable cause?",a1="A problem with the corona wires or the drum",a2="Too much moisture on the paper",a3="A warped roller in the paper path",a4="Too much paper in the tray",a5="",ca="a")

    q3= mcq(q="If you were explaining to your company's IT Personnel the difference between SSD and HDD, which statement would be FALSE",a1="SSD are silent in operation.",a2="SSD use a read/write assembly.",a3="SSD are not as fragile as HDD",a4="SSD do not require and external power source",a5="",ca="b")

    q4= mcq(q="You want to use  Enhanced Intel SpeedStep Technology in a laptop. What components must support this technology to use it?",a1="Motherboard, Software Drivers, BIOS, OS",a2="Motherboard, BIOS, OS",a3="BIOS, Motherboard",a4="BIOS, Motherboard, Software Drivers",a5="Motherboard, Software, OS",ca="b")

    q5= mcq(q="You have noticed dust, debris, and toner particles inside a laser printer. You need to vacuum the inside of the printer. What should you do first?",a1="Remove the photosensitive drum",a2="Remove excess toner with a damp cloth.",a3="Remove the toner cartridge",a4="Remove the roller blade",a5="",ca="b")

    q6= mcq(q="One of your laptops has no active Ethernet port. Which accessory should you buy?",a1="USB 3.0",a2="USB->Thunderbolt",a3="USB->RJ-45",a4="USB->Wi-Fi",a5="USB->Bluetooth",ca="d")

    q7= mcq(q="You have been asked to increase the security of your wireless network. Which of the following options should you impement?",a1="MAC filtering",a2="SSID broadcast",a3="War Driving",a4="Rogue access points",a5="",ca="a")

    q8= mcq(q="A user contacts you about a notebook battery that will no longer hold a charge. The battery has been removed, but the computer will not work when plugged into AC power. The new battery is on order, but won't arrive in time for her meeting tomorrow. What should they do?",a1="Change the battery setting in the bios",a2="Re-inser the depleted battery in the computer, and then boot the computer.",a3="Fully charge the old battery overnight, and then boot the computer.",a4="Wait until the new battery arrives next week",a5="",ca="b")
   
    q9= mcq(q="Which network medium is the least susceptible to EMI or signal capture?",a1="Coaxial",a2="STP",a3="Fiber Optic",a4="UTP",a5="",ca="c")
   
    q10=mcq(q="What is the transmission distance supported by Single-Mode fiber optic?",a1="Approximately 3,000 feet",a2="Approximately 20 miles",a3="Approximately 50 feet",a4="Approcimately 74 miles.",a5="Approximately 35 miles.",ca="b")

    q11=mcq(q="You turn on your computer to connect to a computer named COMP5 on your development subnet, but you are unable to do so. However you can connect to all of the other computers in the research subnet, and other research computers can connect to COMP5 on the development subnet. What would explain your computer's communications problem?",a1="An incompatible network protocol listed first in the binding order.",a2="A loose network interface card",a3="An incorrect IP address",a4="An incorrect default gateway",a5="Maybe it's just introverted.",ca="d")
    
    q12=mcq(q="Your laser printer's charge or primary corona is having problems. What is the main purpose of this laser printer component?",a1="To melt the toner into the paper.",a2="To coordinate the components to print a page.",a3="To write the image on the drum",a4="To charge the paper.",a5="To apply a uniform negative charge to the photosensitive drum.",ca="d")
    
    q13=mcq(q="Which of the following is NOT part of routine maintenance for thermal printers.",a1="Removing debris",a2="Calibrating the printer.",a3="Cleaning the heating element.",a4="Replacing the paper.",a5="Replacing the heating element.",ca="b")

    q14=mcq(q="On which of these components can you specifically enable overclocking?",a1="HDD, Motherboard, System Bus",a2="Processor, RAM, Motherboard.",a3="Processor, RAM, System Bus",a4="Processor, Ram",a5="System Bus, Motherboard.",ca="C")
    
    q15=mcq(q="To which device should a WAP be connected?",a1="Firewall",a2="DSL 'modem'",a3="Hub", a4="Router",a5="Switch",ca="c")

    q16=mcq(q="Which components are usually included in the toner cartridge of a laser printer.",a1="Photosensitive Drum, Transfer Corona",a2="Electrostatically Charged Toner, Fuser",a3="Photosensitive Drum, Electrostatically Charged Toner.",a4="Transfer Corona, Photosensitive Drum",a5="Transfer corona, Electrostatically Charged Toner.",ca="e")

    q17=mcq(q="Which RAM module uses 168 pins?",a1="RDRAM",a2="SIMM",a3="DIPP",a4="DIMM",a5="SIPP",ca="d")


    
    questions=[q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17]
