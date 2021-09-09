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
    q1 = mcq(q=,a1=,a2=,a3=,ca=)
    q2= mcq(q=,a1=,a2=,a3=,ca=)
    q3= mcq(q=,a1=,a2=,a3=,ca=)
    q4= mcq(q=,a1=,a2=,a3=,ca=)
    q5= mcq(q=,a1=,a2=,a3=,ca=)
    q6= mcq(q=,a1=,a2=,a3=,ca=)
    q7= mcq(q=,a1=,a2=,a3=,ca=)
    q8= mcq(q=,a1=,a2=,a3=,ca=)
    q9= mcq(q=,a1=,a2=,a3=,ca=)
    questions=[q1,q2,q3,q4,q5,q6,q7,q8,q9]

