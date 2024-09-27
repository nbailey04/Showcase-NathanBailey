; Assemble:       nasm -f elf64 lab12_pt2.asm
; Link:           gcc lab12_pt2.o -o lab12_pt2

; Generate a random number.

    extern  printf      ; We will use this external function
    extern  srandom     ; We will use this external function
    extern  random      ; We will use this external function

    section .data       ; Data section, initialized variables
myseed:   dq 0
myval1:   dq 0
myval2:   dq 0
myval3:   dq 0
mystr:   db "%ld", 10, 0   ; String format to use (decimal), followed by NL
seedMsg: db "Seed is: %ld", 10, 0 ; Message for printing seed value

    section .text
    global main
main:

      rdtsc
   mov     [myseed], rax   ; Store TSC value as the seed

   ; "Seed" the random number generator with the TSC value.
   mov   rdi, [myseed]
   call  srandom

   ; Print the seed value
   mov   rsi, [myseed]
   mov   rax, 0
   mov   rdi, seedMsg
   call  printf

   ; Generate first random number
   xor   rax, rax          ; A = 0
   call  random
   mov   [myval1], rax     ; Store the value

   ; Generate second random number
   xor   rax, rax          ; A = 0
   call  random
   mov   [myval2], rax     ; Store the value

   ; Generate third random number
   xor   rax, rax          ; A = 0
   call  random
   mov   [myval3], rax     ; Store the value

   ; Print the first random number
   mov   rsi, [myval1]
   mov   rax, 0
   mov   rdi, mystr
   call  printf

   ; Print the second random number
   mov   rsi, [myval2]
   mov   rax, 0
   mov   rdi, mystr
   call  printf

   ; Print the third random number
   mov   rsi, [myval3]
   mov   rax, 0
   mov   rdi, mystr
   call  printf

   mov  rax, 0
   ret
