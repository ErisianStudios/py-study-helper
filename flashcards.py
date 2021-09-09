import random
from multiple_choice_question import mcq
class Ports:
    q = ["Port 21","Port 22","Port 23","Port 25","Port 53","Port 80","Port 110","Port 161/162","Port 143","Port 443","port 3389", "Port 137-139","Port  139/445", "Port 427","Port 548","Port 67/68","Port 389","Port 1812/1813","FTP","SSH","Telnet","SMTP","DNS","HTTP","POP3","SNMP","IMAP","HTTPS","RDP","NetBIOS/NetBT","SMB/CIFS","SLP","AFP","DHCP","LDAP","RADIUS"]
    a =["FTP","SSH","Telnet","SMTP","DNS","HTTP","POP3","SNMP","IMAP","HTTPS","RDP","NetBIOS/NetBT","SMB/CIFS","SLP","AFP","DHCP","LDAP","RADIUS","Port 21","Port 22","Port 23","Port 25","Port 53","Port 80","Port 110", "Port 161/162","Port 143","Port 443","port 3389", "Port 137-139","Port 139/445", "Port 427","Port 548","Port 67/68","Port 389","Port 1812/1813"]
    def question_or_answer():
        i = random.randrange(0,2)
        return i
class MultipleChoice:
    q1 = mcq(q="What is 1+1",a1="3",a2="2",a3="I dunno man....",ca="2")
    questions=[q1]

