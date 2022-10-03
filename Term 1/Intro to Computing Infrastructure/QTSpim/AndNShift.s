	# Declare main as a global function
	.globl main 

	# All program code is placed after the
	# .text assembler directive
	.text 		

# The label 'main' represents the starting point
main:
    # Print message and take input
	li	$v0,4		# print_string syscall code = 4
	la	$a0, inp_str	# load the address of msg2
	syscall
	li	$v0,5		# read_int syscall code = 5
	syscall	
	move	$t2,$v0		# syscall results returned in $v0
	li	$v0,4		# print_string syscall code = 4
	la	$a0, newline	# load the address of msg2
	syscall
	
	

	li $t3, 1		# Load the word stored in value (see bottom)
	li $t6, 0
	
loop:	
    and $t4, $t2, $t3
	beq $t4, 1, c1
h2:
	sra $t5, $t2, 1
	move $t2, $t5
	beq $t2, 0, exit
	j loop

c1:
    add $t6, 1
	j h2

	
exit:
	move $a0, $t6
	li $v0, 1
	syscall
	
	li $v0, 10
	syscall


.data
inp_str:	.asciiz	"Enter Number: "
newline:    .asciiz	"\n"