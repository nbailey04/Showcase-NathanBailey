extern printf
extern scanf
section .data
format_str:         db "%d", 0               ; The scanf format, '0'
prompt:             db "Enter a 3-digit number: ", 0
num:                dd 0
narcissistic_msg:   db "The number is a Narcissistic Number.", 10, 0
not_narcissistic_msg: db "The number is not a Narcissistic Number.", 10, 0
error_msg:          db "Error: Input must be a 3-digit number.", 10, 0

section .text           ; Code section.

global main             ; the standard gcc entry point
main:                           ; the program label for the entry point

    ; Print the prompt
    mov rdi, prompt     ; First argument for printf (address of msg)
    xor rax, rax        ; Clear rax because printf is a variadic function
    call printf         ; Use printf instead of puts: no newline

    ; Call scanf
    mov rsi, num        ; Address of num for scanf
    mov rdi, format_str ; Format string for scanf
    xor rax, rax        ; Clear rax because scanf is a variadic function
    call scanf

    ; Check if the input is a 3-digit number
    mov eax, [num]      ; Load the input number into eax
    cmp eax, 100        ; Check if less than 100
    jl input_error
    cmp eax, 1000       ; Check if greater than or equal to 1000
    jge input_error

    ; Initialize sum of cubes to zero
    mov ecx, 0          ; Sum of cubes

    ; Loop to calculate sum of cubes of digits
div_loop:
    xor edx, edx        ; Clear edx each time before division
    mov ebx, 10         ; Set divisor to 10
    div ebx             ; Divide eax by 10, quotient in eax, remainder in edx

    ; Cube the remainder and add to sum
    mov ebx, edx        ; Move remainder to ebx for cubing
    imul ebx, edx       ; Square ebx
    imul ebx, edx       ; Cube ebx (remainder)
    add ecx, ebx        ; Add cube of remainder to sum

    ; Check if there are more digits to process
    test eax, eax       ; Test quotient for zero
    jnz div_loop        ; If quotient not zero, loop

    ; Compare sum of cubes with original number
    cmp ecx, [num]
    je is_narcissistic
    jmp not_narcissistic

not_narcissistic:
    ; Print message: Not a Narcissistic Number
    mov rdi, not_narcissistic_msg  ; Format string
    xor rax, rax
    call printf
    jmp exit_program

is_narcissistic:
    ; Print message: Narcissistic Number
    mov rdi, narcissistic_msg  ; Format string
    xor rax, rax
    call printf
    jmp exit_program

input_error:
    ; Print message: Error - Input must be a 3-digit number
    mov rdi, error_msg  ; Format string
    xor rax, rax
    call printf

exit_program:
    ; Exit the program
    xor eax, eax
    ret
