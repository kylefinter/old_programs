#Kyle Finter 
.data
str1:	.asciiz "The number was: "

.text
addi $s0, $zero, 7 #insert chosen number
sll $s0, $s0, 1 #multiply by 2
addi $s0, $s0, 5 #add 5

add $s1, $zero, $s0 #copy value to other registers
add $s2, $zero, $s0

sll $s0, $s0, 1 #multiply by 2
sll $s1, $s1, 4 #multiply by 16
sll $s2, $s2, 5 #multiply by 32

add $s0, $s0, $s1 #add s1 register
add $s0, $s0, $s2 #add s2 register

addi $s0, $s0, 2017 #add current year
subi $s0, $s0, 251 #subtract if birthday has yet to happen yet
subi $s0, $s0, 1996 #subtract birthyear

li $v0, 4 #printing the number is
la $a0, str1
syscall

li $v0, 1 #printing number
add $a0, $zero, $s0
syscall