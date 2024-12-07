

bits 64
section .text

global main
extern printf

;; struct list_node {
;;     val int;
;;     list_node *int;
;; }

next_node: 
    MOV rax, [rdi + 8]                ;; struct list_node* (struct list_node*)
    RET

main:
    PUSH rbp
    mov rbp, rsp      ;; save stack frame

    sub rsp, 16      ;; assign two pointer n_ptr1(rsp) and n_ptr2(rsp + 8)

    MOV [rsp], dword node1       ;; set both pointer to node1
    MOV [rsp + 8], dword node1

    jmp loop
    jmp abort


loop:
    MOV rsi, [rsp]
    CALL next_node
    cmp DWORD [next_node + 8], 0 ;; check if reach to end
    jmp success
    MOV [rsp], rax ;; move n_ptr1 to next_node


    MOV rsi, [rsp + 8]
    CALL next_node
    cmp DWORD [next_node + 8], 0 ;; check if reach to end
    jmp success
    MOV rsi, rax
    CALL next_node
    cmp DWORD [next_node + 8],  0 ;; check if reach to end
    jmp success
    MOV [rsp + 8], rax ;; move n_ptr1 to next, next_node
    MOV rax, [rsp]
    MOV rbx, [rsp + 8]
    cmp rax, rbx
    jmp cycle
    jmp loop

success:
    MOV rax, 60
    MOV rdi, 0
    SYSCALL

cycle:
    MOV rax, 60
    MOV rdi, 1
    SYSCALL

abort:
    MOV rax, 60
    MOV rdi, 2
    SYSCALL



section .data
    message db "node val: %d", 10, 0

node1:
    dd 42
    dd 0
    dq node2

node2:
    dd 10
    dd 0
    dq 0



