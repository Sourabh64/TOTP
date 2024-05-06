#!/usr/bin/env python3

import base64
import hmac
import struct
import sys
import time
import pyotp


class TOTP:

    def hotp(self, key, counter, digits=6, digest='sha256'):
        print(key.upper() + '=' * ((8 - len(key)) % 8))
        key = base64.b64decode(key + '=' * ((8 - len(key)) % 8))
        counter = struct.pack('>Q', counter)
        print(hmac.new(key, counter, digest))
        mac = hmac.new(key, counter, digest).hexdigest()
        print(mac[-1])
        offset = int(mac[-1], 16)
        print((mac[(offset*2):((offset*2)+8)]))
        binary_new = int(mac[(offset*2):((offset*2)+8)], 16) & 0x7fffffff
        return str(binary_new)[-digits:].zfill(digits)

    def totp(self, key, time_step=30, digits=6, digest='sha256'):
        print(time.time())
        return self.hotp(key, int(time.time() / time_step), digits, digest)

    def main(self):
        args = [int(x) if x.isdigit() else x for x in sys.argv[1:]]
        for key in sys.stdin:
            print(self.totp(key.strip(), *args))

    def random_base32(self, secret):
        # value = pyotp.random_base32()
        bSecret = secret.encode("UTF-8")
        bSecret = base64.b64encode(bSecret)
        bSecret = bSecret.decode()
        # print(pyotp.totp.TOTP('A5OWUMQMJDLRFZSTAR7JQUWNAT6RCFFP').provisioning_uri(name='sourabh@gmail.com',
        # issuer_name='Secure App'))
        print(bSecret)
        return bSecret


if __name__ == '__main__':
    # secret = input("Enter your phone number:")
    secret = "testpassword"
    bSecret = secret.encode("UTF-8")
    bSecret = base64.b64encode(bSecret)
    bSecret = bSecret.decode()
    print(bSecret)
    totps = pyotp.TOTP(bSecret)
    print(totps.now())
    totp = TOTP()
    totp.main()
    # val = random_base32()
    # main()
    # print(totp(bSecret))
