# A demonstration of some simple MIPS instructions
# used to test QtSPIM

	# Declare main as a global function
	.globl main 

	# All program code is placed after the
	# .text assembler directive
	.text 		

# The label 'main' represents the starting point
main:
	li $t2, 0
	beqz $t2, new_br_18
	li	$v0,10		# Code for syscall: exit
	syscall
	
new_br_18:
	#j long_disp

new_br_28:
	li	$v0,1		    # Code for syscall: print_string
	li	$a0, 0xfffffff	# Pointer to string (load the address of msg)
	syscall

	li	$v0,10		# Code for syscall: exit
	syscall
	

	# All memory structures are placed after the
	# .data assembler directive
	.data

	# The .word assembler directive reserves space
	# in memory for a single 4-byte word (or multiple 4-byte words)
	# and assigns that memory location an initial value
	# (or a comma separated list of initial values)
long_disp:	.word 0x400040
Z:	.word 0
