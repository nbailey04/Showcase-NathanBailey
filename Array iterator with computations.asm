extern printf

section .data
    mystr:   db "%d", 10, 0        ; String format to use (decimal), followed by NL
    maxstr:  db "The maximum number in the array is %d", 10, 0
    minstr:  db "The minumum number in the array is %d", 10, 0
    avgstr:  db "The average value of the numbers in the array is %d", 10, 0
    myarr:   dd 10, 20, 30, 40, 50, 60 ; Declare the array
    counter: dd 6               ; Keeps track of the amount of elements in the array
    temp:    dd 0
    min_val: dd 0               ; Storage for the minimum value
    max_val: dd 0               ; Storage for the maximum value
    avg_val: dd 0               ; Storage for the average value

section .text
    global main

main:
    xor eax, eax                ; A = 0
    mov ecx, myarr              ; C points to myarr

    ; Initialize min_val and max_val with the first element of myarr
    mov ebx, DWORD [ecx]
    mov [min_val], ebx
    mov [max_val], ebx

myloop:
    mov ebx, DWORD [ecx+4*eax]  ; Get the value B = myarr[A]
    add [avg_val], ebx

    ; This checks if B is less than the current min_val
    cmp ebx, DWORD [min_val]

    jl update_min               ; Jumps if less than

    ; This checks if B is greater than the current max_val
    cmp ebx, DWORD [max_val]
    jg update_max
    jmp continue_loop

update_min:

    ; This updates the min_val with the new minimum value if the new one is lower
    mov [min_val], ebx
    jmp continue_loop

update_max:
    ; This updates the max_val with the new maximum value if the new one is greater
    mov [max_val], ebx

continue_loop:
    ; Continues the original given loop
    mov [temp], ebx
    push rax
    push rcx

                                ; Now print the result out
    mov rdi, mystr              ; Format of the string to print
    mov rsi, [temp]             ; Value to print
    mov rax, 0
    call printf

    pop rcx
    pop rax
    add eax, 1                  ; A++
    cmp eax, [counter]                  ; Does A == 6?
    jl myloop                   ; if less, jump to myloop

    ; Print the minimum and maximum values
    mov rdi, minstr
    mov rsi, [min_val]
    mov rax, 0
    call printf

    mov rdi, maxstr
    mov rsi, [max_val]
    mov rax, 0
    call printf

    ; Do the math with the updated [avg_vale] variable
    mov eax, [avg_val]
    mov ebx, [counter]
    xor edx, edx,
    div ebx
    mov [avg_val], eax

    ; Print the average value
    mov rdi, avgstr
    mov rsi, [avg_val]
    mov rax, 0
    call printf

    mov rax, 0
    ret
