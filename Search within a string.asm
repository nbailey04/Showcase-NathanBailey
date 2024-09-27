    SYS_READ equ 0               ; read text from stdin
    SYS_WRITE equ 1              ; write text to stdout
    STDIN equ 0                  ; standard input
    STDOUT equ 1                 ; standard output

    extern printf
    extern puts

section .data
    search_str: db "Please input the string you want to find:",0
    text_str: db "Please input the full text:",0
    format_str: db "The search string was found at position %d ", 10, 0
    newline db ""
    x: dd 0                      ; Will be used to determine position
    y: dd 0                      ; Will be used to determine position

section .bss
    start resb 1
    find resb 1000
    text resb 1000
    temp resb 10

section .text
    global main

main:
    mov rdi, search_str
    call  puts
    xor ebx, ebx

search_loop:
    mov rsi, temp                ; Where to store characters that are read
    mov rdi, STDIN               ; Fd of input
    mov rdx, 1                   ; Tells how many characters to read
    mov rax, SYS_READ            ; Function to call
    syscall
    mov al, [temp]               ; This moves current character into 'al'
    cmp al, 10                   ; This compare 'al' to 10 to see if we are at a newline
    je continue                  ; Jmp to next subroutine if equal
    mov [find+ebx], al           ; If not, move current char into the search string
    inc ebx                      ; Increments ebx
    jmp search_loop              ; This restarts the loop

continue:
    mov rdi, text_str
    call  puts

    ; This will read the text
    mov rsi, text                ; Where to store characters read
    mov rdi, STDIN               ; Fd of input
    mov rdx, 1000                ; How many characters to read
    mov rax, SYS_READ            ; The function to be called
    syscall


while_loop:
    ; This will check if we reached the end of the text file (looking for null term)
    mov ecx, [x]         ; Moves x into the C register
    mov al, [text + ecx] ; Moves value of counter x plus the text size into 'al'
    cmp al, 0            ; Checks to see if 'al' is equal to 0 (aka empty)
    je end_while         ; If so, it will jump to 'end_while' to end the while loop

    ; Check if search string and current string within text are equal
    cmp al, [find + 0]
    jne not_equal

    ; If not, then it will call test function
    mov eax, [x]
    jmp start_loop

not_equal:
    ; This will increment x
    mov ecx, [x]   ; Move value of x into the C register
    inc ecx        ; Increment C register containing x
    mov [x], ecx   ; Move the value of the C register back into x
    jmp while_loop ; Go to the 'while_loop area'

end_while:
    mov rdi, newline
    call puts
    ; Exit program
    mov eax, 1
    xor ebx, ebx
    ret

start_loop:
    ; This compares the search string and the input text and finds the position of the search string in the input text
    mov edx, [y]           ; Moves the current position of matching string into edx
    mov al, [find + edx]   ; Gets character from the search string
    cmp al, 0              ; This compares al to 0 to see if weve reached a null character
    je end_test            ; If so, then we go to the 'end test' subroutine
    add edx, [x]           ; Add x and y to get position of the string
    mov bl, [text + edx]   ; This gets the character from the text file
    cmp bl, al             ; This compares al and bl to see if they are equal
    jne end_func          ; If they are not, then jump to end
    mov ecx, [y]           ; If so, then move y to the C register to get incremented
    inc ecx                ; Increment C
    mov [y], ecx           ; Place y back into the y variable from the C register
    jmp start_loop         ; Start the loop over again



end_test:
    ; Now at the end, we just need to prin
    mov   rdi, format_str  ; Format of the string to print
    mov   rsi, [x]         ; Value to print
    mov   rax, 0
    call printf
    mov ebx, 0
    mov [y], ebx

end_func:
    jmp not_equal
