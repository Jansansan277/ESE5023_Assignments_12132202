module Declination_angle
implicit none
!For calculating the declination angle, d (the number of days since the beginning of Jan 1st in UTC) in XXX year is the key parameter.
!Define variables
  real, parameter:: pi = 3.1415926536

contains

subroutine Declination_angle(yy,mm,dd,dec_angle)
  implicit none
! Define variables
  integer:: yy,mm,dd,days=0
  real(8):: dec_angle,i,j
  integer::dayofmonth(12)=[31,28,31,30,31,30,31,31,30,31,30,31]

! It is a Leap Year or not
  if(((MOD(yy,4)==0).and.(MOD(yy,100)/=0)).or.(mod(yy,400)==0)) then
    dayofmonth(2)=29
  end if

!Get the days
  days=sum(dayofmonth(1:mm-1))+dd
  print*,days
  

  i = 360.0 / 365.24
  j = sin(-23.44*2*pi/360.0)*cos((i*(days+10)+(360.0/pi)*0.0167*sin(i*(days-2)))*2*pi/360.0)   
  dec_angle = asin(j*180.0/pi)

end subroutine Declination_angle

end module  Declination_angle
