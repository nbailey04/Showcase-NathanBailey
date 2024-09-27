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
;----------------------------------------

; Assemble:       nasm -f elf64 lab12_pt3.asm
; Link:           gcc lab12_pt3.o -o lab12_pt3

    extern  srandom     ; We will use this external function
    extern  random      ; We will use this external function
    extern  puts        ; We will use this external function
    extern  printf      ; We will use this external function
    section .bss
str: resb 101

    section .data       ; Data section, initialized variables
myseed:   dq 0          ; Variable to store the seed value
newline:  db 10         ; Newline character

    section .text
    global main
main:

   ; Seed the random number generator
   rdtsc                 ; Read the Time Stamp Counter
   mov   [myseed], eax   ; Store the TSC value in myseed
   mov   edi, eax        ; Set the seed value to EDI for srandom function
   xor   rax, rax        ; Clear the A register
   call  srandom         ; Seed the random number generator

   xor rbx, rbx          ; Initialize B register to 0

lp:
   xor rax, rax                 ; Clear the A register
   call random                  ; Generate a random number
   and al, 0xF                  ; Limit values (0 to 15)
   or al, 40h                   ; Check for '@'
   mov byte [str + rbx], al     ; Store the random value in the str buffer
   inc rbx                      ; Increment B register

   cmp rbx, 100                 ; Compare the current value stored in B with 100
   jl lp                        ; If less, repeat the loop

   mov byte [str + rbx], 0     ; Null-terminate the string

   ; Print the string
   mov rdi, str
   call puts

   ; Print a newline
   mov rdi, newline
   mov rax, 0
   call printf

   mov rax, 0
   ret
