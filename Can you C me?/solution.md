# Can you C me?
Category: Binary Exploitation, 250 points

## Description
> Everything is right in front of your eyes. You just have to C it.

## Solution

Let's run the attached file:
```
┌──(wahajk㉿WahajK)-[~/Downloads/NEDCTF/Can you C me?]
└─$ ./can_you_c_me  
Enter correct password: abc
wrong!
```

Nothing much to see here

Let's open the biary in ghidra and check the decompiled output:
```c
undefined8 main(void)

{
  int iVar1;
  undefined8 local_a1;
  undefined local_99;
  undefined8 local_98;
  undefined8 local_90;
  undefined8 local_88;
  undefined4 local_80;
  undefined2 local_7c;
  undefined local_7a;
  char local_78 [112];
  
  local_98 = 0x337633727b43434e;
  local_90 = 0x35695f676e693572;
  local_88 = 0x35325f793561335f;
  local_80 = 0x32343233;
  local_7c = 0x7d33;
  local_7a = 0;
  local_a1 = 0x7937215275633373;
  local_99 = 0;
  printf("Enter correct password: ");
  __isoc99_scanf(&DAT_0010201d,local_78);
  iVar1 = strcmp((char *)&local_a1,local_78);
  if (iVar1 == 0) {
    printf("Correct!\nHere\'s the Flag: ");
    printf("%s",&local_98);
  }
  else {
    printf("wrong!");
  }
  return 0;
}
```

At first glance we see that the program is printing the variable `local_98` while saying `Here's the Flag`

You can use any tool for conversion or simply hover over the value in ghidra and it will show us it's character value
(Make sure to remove the 0x when using an online tool otherwise it might give wrong value)

Converting the value of the variable `local_98`, we get: `7c7'´44` which is not what we are looking for
There are many other variables with some value, let's try converting them to see if they give us the flag.

After converting and joing all the variables, we get: `3v3r{CCN`

