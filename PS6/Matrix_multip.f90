!This subroutine is to do matrix multiplication of M and N
subroutine Matrix_multip(M, N, result) 
implicit none

! Define variables
real(8),dimension(5, 3) :: M
real(8),dimension(3, 5) :: N
real(8),dimension(5, 5) :: Result
real(8)                 :: tmp
integer                 :: i, j, k

! i is the row of M and j is the column of N
! k is the column of M and row of N
do i = 1, 5 
  do j = 1, 5
    tmp = 0
      do k  = 1, 3
        tmp = tmp + (m(i, k) * n(k, j))
      enddo
    Result(i,j) = tmp
  enddo
enddo

end subroutine Matrix_multip
