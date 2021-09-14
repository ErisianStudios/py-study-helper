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
    q0= mcq(q="You need to install a TV tuner adapter in a computer. All of the following steps are necessary EXCEPT...",
            a1="Plugging the audio cable into the TV tuner adapter card and sound card.",
            a2="Plugging the TV tuner adapter into a PCI slot",
            a3="Plugging the antena into the TV tuner card.",
            a4="Plugging the TV tuner into a USB port",
            a5="",
            ca="d")

    q1 = mcq(q="What is the network prefix used to denote an unsubnetted Class C IP address?",
            a1="/8",
            a2="/24",
            a3="/16",
            a4="/32",
            a5="",
            ca="b")

    q2= mcq(q="Your laser printer repeatedly prints vertical lines through the page. What is the probable cause?",
            a1="A problem with the corona wires or the drum",
            a2="Too much moisture on the paper",
            a3="A warped roller in the paper path",
            a4="Too much paper in the tray",
            a5="",
            ca="a")

    q3= mcq(q="If you were explaining to your company's IT Personnel the difference between SSD and HDD, which statement would be FALSE",
            a1="SSD are silent in operation.",
            a2="SSD use a read/write assembly.",
            a3="SSD are not as fragile as HDD",
            a4="SSD do not require and external power source",
            a5="",
            ca="b")

    q4= mcq(q="You want to use  Enhanced Intel SpeedStep Technology in a laptop. What components must support this technology to use it?",
            a1="Motherboard, Software Drivers, BIOS, OS",
            a2="Motherboard, BIOS, OS",
            a3="BIOS, Motherboard",
            a4="BIOS, Motherboard, Software Drivers",
            a5="Motherboard, Software, OS",
            ca="b")

    q5= mcq(q="You have noticed dust, debris, and toner particles inside a laser printer. You need to vacuum the inside of the printer. What should you do first?",
            a1="Remove the photosensitive drum",
            a2="Remove excess toner with a damp cloth.",
            a3="Remove the toner cartridge",
            a4="Remove the roller blade",
            a5="",
            ca="b")

    q6= mcq(q="One of your laptops has no active Ethernet port. Which accessory should you buy?",
            a1="USB 3.0",
            a2="USB->Thunderbolt",
            a3="USB->RJ-45",
            a4="USB->Wi-Fi",
            a5="USB->Bluetooth",
            ca="d")

    q7= mcq(q="You have been asked to increase the security of your wireless network. Which of the following options should you impement?",
            a1="MAC filtering",
            a2="SSID broadcast",
            a3="War Driving",
            a4="Rogue access points",
            a5="",
            ca="a")

    q8= mcq(q="A user contacts you about a notebook battery that will no longer hold a charge. The battery has been removed, but the computer will not work when plugged into AC power. The new battery is on order, but won't arrive in time for her meeting tomorrow. What should they do?",
            a1="Change the battery setting in the bios",
            a2="Re-inser the depleted battery in the computer, and then boot the computer.",
            a3="Fully charge the old battery overnight, and then boot the computer.",
            a4="Wait until the new battery arrives next week",
            a5="",
            ca="b")
   
    q9= mcq(q="Which network medium is the least susceptible to EMI or signal capture?",
            a1="Coaxial",
            a2="STP",
            a3="Fiber Optic",
            a4="UTP",
            a5="",
            ca="c")
   
    q10=mcq(q="What is the transmission distance supported by Single-Mode fiber optic?",
            a1="Approximately 3,000 feet",
            a2="Approximately 20 miles",
            a3="Approximately 50 feet",
            a4="Approcimately 74 miles.",
            a5="Approximately 35 miles.",
            ca="b")

    q11=mcq(q="You turn on your computer to connect to a computer named COMP5 on your development subnet, but you are unable to do so. However you can connect to all of the other computers in the research subnet, and other research computers can connect to COMP5 on the development subnet. What would explain your computer's communications problem?",
            a1="An incompatible network protocol listed first in the binding order.",
            a2="A loose network interface card",
            a3="An incorrect IP address",
            a4="An incorrect default gateway",
            a5="Maybe it's just introverted.",
            ca="d")
    
    q12=mcq(q="Your laser printer's charge or primary corona is having problems. What is the main purpose of this laser printer component?",
        a1="To melt the toner into the paper.",
        a2="To coordinate the components to print a page.",
        a3="To write the image on the drum",
        a4="To charge the paper.",
        a5="To apply a uniform negative charge to the photosensitive drum.",
        ca="d")
    
    q13=mcq(q="Which of the following is NOT part of routine maintenance for thermal printers.",
        a1="Removing debris",
        a2="Calibrating the printer.",
        a3="Cleaning the heating element.",
        a4="Replacing the paper.",
        a5="Replacing the heating element.",
        ca="b")

    q14=mcq(q="On which of these components can you specifically enable overclocking?",
        a1="HDD, Motherboard, System Bus",
        a2="Processor, RAM, Motherboard.",
        a3="Processor, RAM, System Bus",
        a4="Processor, Ram",
        a5="System Bus, Motherboard.",
        ca="C")
    
    q15=mcq(q="To which device should a WAP be connected?",
        a1="Firewall",
        a2="DSL 'modem'",
        a3="Hub", 
        a4="Router",
        a5="Switch",
        ca="c")

    q16=mcq(q="Which components are usually included in the toner cartridge of a laser printer.",
        a1="Photosensitive Drum, Transfer Corona",
        a2="Electrostatically Charged Toner, Fuser",
        a3="Photosensitive Drum, Electrostatically Charged Toner.",
        a4="Transfer Corona, Photosensitive Drum",
        a5="Transfer corona, Electrostatically Charged Toner.",
        ca="e")

    q17=mcq(q="Which RAM module uses 168 pins?",
        a1="RDRAM",
        a2="SIMM",
        a3="DIPP",
        a4="DIMM",
        a5="SIPP",
        ca="d")

    q18=mcq(q="Your printer does not have a duplexer installed. However, when printing a document, you choose to print with the duplex settings. What will be the outcome when you print the document?",
        a1="The document will first print the odd numbered pages, and then the even numbered pages.",
        a2="The document will first print the even numbered pages, and then the odd numbered pages.",
        a3="The printer will print the pages in continuation as numbered.",
        a4="The printer will prompt for the duplexer to be installed.",
        a5="The document will fail to print.",
        ca="a")

    q19=mcq(q="When you reboot your system after a new graphics adapter was installe,d you get a blank screen on bootup. The system does not proceed beyond the blank screen. Which of the following can be a root cause for this?",
        a1="RAM",
        a2="Video Adapter",
        a3="CPU",
        a4="BIOS configuration",
        a5="",
        ca="d")

    q20=mcq(q="Which of the following are valid reasons to choose 802.11n/ac over 802.11g?\n1. Use of 5GHZ frequencies incur less interference\n2. Provides larger channel bandwidths per user\n3. Use of 2.4GHz frequencies provide more bandwidth and less interference\n4. 802.11g provides higher bandwidths",
        a1="1 and 2",
        a2="1 and 3",
        a3="2 and 3",
        a4="3 and 4",
        a5="1, 2 and 4",
        ca="")
    
    q21=mcq(q="How do you resolve faded printout issue from an injet printer?",
        a1="Check the ribbon.",
        a2="Set the printer to normal print mode.",
        a3="Clean the nozzle.",
        a4="Check the toner belt.",
        a5="All of the above.",
        ca="c")

    q22=mcq(q="You are building a small network on which you want to minimize network collision between the connected devices. You also want to ensure that the devices on the network can ommunicate with each other. To meet this goal, what shouyld you do?",
        a1="Use a hub",
        a2="Use a router",
        a3="Use a bridge",
        a4="Use an unmanaged switch",
        a5="Use an active hub",
        ca="c")

    q23=mcq(q="You have several computers connected to the same multiport network device. A user accidentally connects two ports of his device directly into each other using a single cable. All the computers connected to this device lose network connectivity. Which of the following devices is the multiport network device?",
        a1="Firewall",
        a2="Managed Switch with STP enabled",
        a3="Router",
        a4="Hub",
        a5="Repeater",
        ca="d")

    q24=mcq(q="You have a set of computers that are connected to a 1Gbps network via Ethernet cables using RJ-45 connectors. The cable connected to one of the computers has the damaged brown/white twisted pair, which is used in the pints 7 and 9 on the RJ-45 connector. What will be the result?",
        a1="The computer will lose connection.",
        a2="The computer will remain connected, but the connection speed will be 10Mbps.",
        a3="The computer will remain connected, but some data loss is expected.",
        a4="The computer will remain connected, but the connection speed will be 100Mbps",
        a5="The computer will remain connected and the network speed will not change.",
        ca="d")

    q25=mcq(q="You have installed a RAID controller on a system using the proper method. However, the system is not able to detect it. What should be your first step to resolve the issue?",
        a1="Ensure all drive cables are conencted properly.",
        a2="Reaseat the RAID controller.",
        a3="Enable the RAID controller in the BIOS.",
        a4="Install the RAID controller's drivers.",
        a5="None of these.",
        ca="c")

    q26=mcq(q="You are configuring a firewall and want to allow NetBIOS traffic. Which ports should you open?",
        a1="TCP 137/139 UDP 137/138",
        a2="TCP 138/139 UDP 137/139",
        a3="TCP 137/138 UDP 138/139",
        a4="TCP 137/139 UDP 137/139",
        a5="TCP 137/139 UDP 138/139",
        ca="a")

    q27=mcq(q="Identify the components that can cause ghost images on a printout in a laser printer.\n1. Toner cartridge\n2. Imaging drum wiper blade.\n3. Fusing unit.",
        a1="2 and 3",
        a2="1 and 3",
        a3="1, 2 and 3",
        a4="1 and 2",
        a5="",
        ca="c")
        
    questions=[q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26]