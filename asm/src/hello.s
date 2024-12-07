

bits 64
section .text

global main
extern printf

main:
    MOV rdi, message
    XOR rax, rax
    CALL printf

    MOV rax, 60
    MOV rdi, 0
    SYSCALL

section .data
    message db "Hello World",10, 0
