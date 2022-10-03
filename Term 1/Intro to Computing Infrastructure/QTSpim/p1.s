# A demonstration of some simple MIPS instructions
# used to test QtSPIM

	# Declare main as a global function
	.globl main 

	# All program code is placed after the
	# .text assembler directive
	.text 		

# The label 'main' represents the starting point
main:
	li $t2, 0xFFFFFFFF		# Load immediate value (25) 
	
	sra $t3, $t2, 1		# Load the word stored in value (see bottom)
	
	srl $t4, $t2, 1		# Load the word stored in value (see bottom)


	li $v0, 10 # Sets $v0 to "10" to select exit syscall
	syscall # Exit

	# All memory structures are placed after the
	# .data assembler directive
	.data

	# The .word assembler directive reserves space
	# in memory for a single 4-byte word (or multiple 4-byte words)
	# and assigns that memory location an initial value
	# (or a comma separated list of initial values)
value:	.word 12
Z:	.word 0
