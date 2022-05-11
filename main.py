def binary(decimal):
    L = ""
    while True:
        L = L + str(divmod(decimal, 2)[1])
        decimal = divmod(decimal, 2)[0]
        if (decimal == 0):
            break
    L = int(str(L)[::-1])
    if(len(str(L)) < 8):
        z = '0'*(8-len(str(L)))
        L = z + str(L)
    return L

def getClass(IP):
    IP = int(IP[0])
    if(IP > 239):
        return 'E'
    elif(IP > 223 ):
        return 'D'
    elif (IP > 191):
        return 'C'
    elif (IP > 127):
        return 'B'
    else:
        return 'A'

def ipToBinary(ipList):
    binary_ip = []
    for i in range(0,4):
        octect = binary(int(ipList[i]))
        binary_ip.append(octect)
    return binary_ip

def ipToDecimal(binaryIp):
    decimalIp=''
    for a in range(0,4):
        number = binaryIp[a]
        dec_number = int(number, 2)
        decimalIp = decimalIp + str(dec_number)
        if(not(a==3)):
            decimalIp = decimalIp+'.'
    return decimalIp

while True:
    b=0
    ip = str(input("Enter ip address => "))
    ip = ip.split('.')
    if(not(len(ip) == 4)):
        print("Invalid IP Address { ip must contain only 4 octects }")
        continue
    for octect in ip:
        if(int(octect) >255 or int(octect)<0):
            print("Invalid IP Address { Invalid octect value }")
            b = 1
    if(b==1):
        b=0
        continue
    ipClass = getClass(ip)
    ipBinary = ipToBinary(ip)

    cidr = int(input("Enter CIDR number => "))
    subnet_mask = '1'*cidr + '0'*(32 - cidr)
    subnet_mask_decimal = ipToDecimal(subnet_mask)
    network_bits_major = divmod(cidr,8)[0]
    network_bits_minor = divmod(cidr,8)[1]
    e = str(ipBinary[network_bits_major])
    new_sector=[]
    e1 = str(e[0:network_bits_minor])
    e2 = str(e[network_bits_minor:len(e)])
    new_sector.append(e1)
    new_sector.append(e2)
    ipBinary[network_bits_major] = new_sector

    host_bits = 32-cidr
    connectable_devices = (2**host_bits)-2

    network_ip_part = ipBinary[network_bits_major][0]
    network_address_host_part = '0'*(8-network_bits_minor)
    netowrk_address_section = network_ip_part+network_address_host_part
    netowrk_ip_address_binary = []
    for a in range(0,network_bits_major):
        netowrk_ip_address_binary.append(str(ipBinary[a]))
    netowrk_ip_address_binary.append(netowrk_address_section)
    if(not(len(netowrk_ip_address_binary)==4)):
        for b in range(network_bits_major+1,4):
            netowrk_ip_address_binary.append('00000000')
    netowrk_ip_address_decimal = ipToDecimal(netowrk_ip_address_binary)

    broadcast_ip_part = network_ip_part
    broadcast_address_host_part = '1'*(8-network_bits_minor)
    broadcast_address_section = broadcast_ip_part + broadcast_address_host_part
    broadcast_ip_address_binary = []
    for a in range(0,network_bits_major):
        broadcast_ip_address_binary.append(str(ipBinary[a]))
    broadcast_ip_address_binary.append(broadcast_address_section)
    if(not(len(broadcast_ip_address_binary)==4)):
        for b in range(network_bits_major+1,4):
            broadcast_ip_address_binary.append('11111111')
    broadcast_ip_address_decimal = ipToDecimal(broadcast_ip_address_binary)

    print("---------------------------------------------------------------------")
    print("This IP Belongs to Class -",ipClass)
    print("No of Connectable devices -",connectable_devices)

    print('')
    print("This IP's Network IP Address is -",netowrk_ip_address_decimal)
    print("This IP's Broadcast IP Address is -",broadcast_ip_address_decimal)
    print("---------------------------------------------------------------------")
    print("########## Coded By Vimukthi Kothalawala @2022 ##########")
    print('')