-----------------------------------String Iterator that Copies---------------------------------------------
section .data
    string db "Low Level Assembly Programming",0
    len equ $-string
section .bss
    copy resb len
section .text
    global main
    extern puts
main:
    mov rcx,len              ; This uses the 64-bit registers
    xor rdx,rdx        	     ; This clears the 'rdx' register
lp:
    xor rax,rax              ; This clears the 'rax' register
    mov al,byte[string+rdx]  ; This accesses the byte from 'string'
    mov byte[copy+rdx],al    ; This copies byte to 'copy'
    inc rdx                  ; This increments 'rdx'
    cmp rdx,rcx              ; This compares 'rdx' with 'rcx' 
    jl lp                    ; If rdx is less than rcx, then jump to lp 
endof:
    lea rdi, [copy]          ; This loads the address of copy into rdi 
    call puts                ; Call puts function
    ret                      ; Returns
--------------------------------------String iterator that displays length---------------------------------------------
section .data
    string db "Low Level Assembly Programming",0

section .text
    global main

main:
    xor rax, rax               ; This clears 'rax'
    xor rcx, rcx      
    mov rdi, string  	       ; Address of the string into rdi
lp:
    cmp byte [rdi + rcx], 0    ; Compare the current character to null terminator
    je endof                   ; If null, jump to endof
    inc rcx                    ; Increment counter
    jmp lp                     ; Repeat loop
endof:
    mov rsi, rcx               ; Move string length to rsi for print
    mov rdi, rsp               ; Use rsp as temporary buffer
    add rdi, 20h               ; Move to the end of the buffer
    mov byte [rdi], 0          ; Null-terminate the buffer
    dec rdi                    ; Move to the last character of the buffer
print_loop:
    mov rbx, 10                ; Divide by 10 to convert to ASCII
    xor rdx, rdx               ; Clear rdx
    div rbx                    ; Divide rcx by 10
    add dl, '0'                ; Convert remainder to ASCII
    dec rdi                    ; Previous position in the buffer
    mov byte [rdi], dl         ; Store the character
    test rax, rax              ; Check if quotient is zero
    jnz print_loop             ; If not zero, continue loop

    mov rax, 1                 ; Syscall number for sys_write
    mov rdi, 1
    mov rdx, rsp               ; Length of the string to print
    sub rdx, rdi               ; Calculate the length
    add rdx, 20h               ; Add offset to point to the start of the buffer
    mov rax, 60                ; Syscall number for sys_exit
    xor rdi, rdi
    syscall
-----------------------------------------String iterator that displays number of occurences------------------------------------------
section .data
    string db "This is string",0
    format db "Number of occurrences of 'a': %d", 10, 0  ; Format string for printf
section .text
    global main
    extern printf

main:
    mov rdi, string     	; Address of string into rdi
    mov rsi, 'i'        	; letter to search
    call count_occurrences      ; count occurrences

    mov rsi, rax                ; Count to rsi
    lea rdi, [format]           ; format string into rdi
    xor eax, eax                ; Clear eax
    call printf                 ; Call printf
    ret

count_occurrences:
    xor rax, rax                ; Clear rax register
    xor rcx, rcx                ; Clear rcx register
    .loop:
        cmp byte [rdi + rcx], 0
        je .end_loop
        cmp byte [rdi + rcx], sil ; Compare character with the letter to search for
        jne .continue_loop
        inc rax                   ; Increment count if the character matches
    .continue_loop:
        inc rcx                 ; Move to the next character
        jmp .loop               ; Repeat loop
    .end_loop:
    ret                         ; Return with the count stored in rax
-----------------------------------------String iterator that cound the number of spaces------------------------------------------
section .data
    string db "Spaces are going to count from here so we are giving more and more and more",0
    format db "Number of spaces: %d", 10, 0  ; Format string for printf
section .text
    global main
    extern printf

main:
    mov rdi, string     	  ; This moves the address of string into rdi
    mov rsi, ' '        	  ; Load the character to search
    call count_occurrences        ; Call function to count occurrences

    mov rsi, rax         	  ; Move the count to rsi
    lea rdi, [format]   	  ; Address of format string into rdi
    xor eax, eax        	  ; Clear eax
    call printf         	  ; Call printf
    ret                 	  ; Return

count_occurrences:
    xor rax, rax       	  	  ; Clears rax register 
    xor rcx, rcx        	  ; Clears rcx register 
    .loop:
        cmp byte [rdi + rcx], 0   ; Check if end of string
        je .end_loop
        cmp byte [rdi + rcx], sil ; Compares character with the letter to search for
        jne .continue_loop
        inc rax                   ; Increment count if the character matches
    .continue_loop:
        inc rcx            	  ; Moves to the next character
        jmp .loop          	  ; Repeats the loop
    .end_loop:
    ret                 	  ; Return with the count stored in rax


------------------------------------------String iterator that flips the given string-----------------------------------------

extern printf
section .data
        fmt:    db "%s",10,0
        str:    db "Hello World"
        strlen: equ $-str
section .text
        global main
main:
        push rbp
        mov rbp, rsp			
        mov rax, str			; These are pointers to start & end of string
        mov rbx, str			; This too
        add rbx, strlen
        dec rbx  ; ignoring null byte
        ; Copy either character into CL & CH regs
        ; T
loop:
        cmp rax,rbx			; This compares 'rbx' to 'rax'
        jg endloop			; If the comparison says that its greater than, then it will jump to 'endloop'
        mov cl, [rax]
        mov ch, [rbx]
        mov [rax], ch
        mov [rbx], cl
        dec rbx
        inc rax
        jmp loop
endloop:
        mov rsi, str			; The following 2 lines displays reversed string
        mov rdi, fmt
        call printf

        mov rsp, rbp
        pop rbp
        ret				; Return
------------------------------------------String iterator that checks if string is palindrome-----------------------------------------
extern printf
section .data
    fmt:    db "%s is a palindrome", 10, 0
    fmt_not: db "%s is not a palindrome", 10, 0
    str:    db "NITIN"   ;
    strlen: equ $-str
section .text
    global main
main:
    push rbp
    mov rbp, rsp
    mov rax, str		; These are pointers to start & end of string
    mov rbx, str		; This too
    add rbx, strlen
    dec rbx  ; ignoring null byte
    				; Check if the string is a palindrome
    mov rcx, rbx  		; Set rcx to the end of the string
    sub rcx, rax  		; Calculate the length of the string
    shr rcx, 1     		; Divide the length by 2 to find the midpoint

check_palindrome:
    cmp rax, rbx
    jge end_check   		; If we reached the midpoint, string is palindrome

    mov al, [rax]   		; Load character from the beginning
    mov bl, [rbx]   		; Load character from the end
    cmp al, bl      		; Compare characters
    jne not_palindrome  	; If characters are not equal, it's not a palindrome

    inc rax         		; Move to the next character from the beginning
    dec rbx         		; Move to the next character from the end
    jmp check_palindrome

not_palindrome:
    mov rsi, str
    mov rdi, fmt_not
    call printf
    jmp end_program

end_check:
    mov rsi, str
    mov rdi, fmt
    call printf

end_program:
    mov rsp, rbp
    pop rbp
    ret
