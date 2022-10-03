	# Declare main as a global function nad A as global variable
	.globl main 
	.globl A 


	.text 		     # This segment contains the logic


main:
    
	lw $t2, A        # Load the word stored in A (see bottom)
	li $t3, 1		
	li $t6, 0        # Counter variable
	
loop:	             # Repeatedly "AND" with 1 to get the Least Significant Bit
                     # and then shift right(unsigned) followed by conditionally
					 #  incrementing the counter if the bit is 1. Exit when word
					 # becomes 0.
    and $t4, $t2, $t3
	beq $t4, 1, c1   # Branch to c1 if Least Significant Bit is 1
h2:
	srl $t5, $t2, 1  # Shift right by 1(logical)
	move $t2, $t5
	beq $t2, 0, exit # Exit if word becomes 0
	j loop

c1:                  # This label is executed when bitwise AND gives 1
    add $t6, 1       # Increment counter
	j h2

	
exit:
	li $v0, 4
	la $a0, otp_str
	syscall          # Print otp_str
	li $v0, 1
	move $a0, $t6
	syscall          # Print the counter
	li $v0, 4
	la $a0, otp_str2
	syscall          # Print otp_str2
	
	li $v0, 10
	syscall          # Exit


.data                # This segment contains the number and strings to be used
otp_str:	.asciiz	"There are "
otp_str2:	.asciiz	" 1's in the inputted number"
newline:    .asciiz	"\n"
A:          .word 31 # A is 31