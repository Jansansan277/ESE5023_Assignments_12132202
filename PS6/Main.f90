program Main

implicit none

!Define 2D array
real(8),dimension(5,3) :: M
real(8),dimension(3,5) :: N
real(8),dimension(5,5) :: Result
!Define other variables
integer                :: u, i

! Read M.dat
! File unit
u = 10
! Open the file
open(unit=u, file='./fortran_demo1/M.dat', status='old')
! Read data line by line
do i = 1, 5
  read(u,*) M(i,1),  M(i,2), M(i,3)
enddo
! Close the file
close(u)

! Read N.dat
! File unit
u = 20
! Open the file
open(unit=u, file='./fortran_demo1/N.dat', status='old')
! Read data line by line
do i = 1, 3
  read(u,*) N(i,1), N(i,2),  N(i,3),  N(i,4),  N(i,5)
enddo
! Close the file
close(u)


! Display the values of M
print*, 'M is following:'
do i = 1,5
  write(*,*) M(i,1),  M(i,2), M(i,3)
enddo

! Display the values of N
print*, 'N is following:'
do i = 1,3
  write(*,*) N(i,1), N(i,2),  N(i,3),  N(i,4),  N(i,5)
enddo

!Matrix multip of M and N by calling the Matrix_multip.f90
call Matrix_multip(M,N,Result)
u = 30
! Create a file called MN to load the result of multip of m and n
open(unit=u,file='./fortran_demo1/MN.dat',status = 'replace')
! The values of MN.dat are in formats of f9,2
! And also print the MN
print*, 'MN is following:'
do i = 1, 5
  write(u,'(f9.2, f9.2, f9.2, f9.2, f9.2)') Result(i,1), Result(i,2),Result(i,3), Result(i,4), Result(i,5)
  print*, Result(i,1), Result(i,2),Result(i,3), Result(i,4), Result(i,5)
enddo


end program Main
