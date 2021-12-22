program  Solar_elevation_angle

    use Solar_hour_angle
    use Declination_angle

    implicit none

    integer:: mm, dd, hour, minute, del_TZ
    real(8):: dec_angle, sol_hur_angle, Lon, Lat, i, SEA
    real, parameter:: pi = 3.1415926536

    mm = 12
    dd = 31
    hour = 10
    minute = 32
    Lon = 114.062996
    Lat = 22.542883
    del_TZ = 8

    call Declination_angle(yy,mm,dd,dec_angle)
    call Solar_hour_angle(yy,mm,dd,hour,minute,del_TZ,Lon,sol_hur_angle)

    i = sin(Lat * pi / 180.0) * sin(dec_angle * pi / 180.0) + cos(Lat * pi / 180.0) * cos(dec_angle * pi / 180.0) * cos(sol_hur_angle * pi / 180.0)
    SEA = ASIN(i) * 180.0  / pi
    print*, 'SEA for Shenzhen (22.542883N, 114.062996E) at 10:32 (Beijing time; UTC+8) on 2021-12-31 is', SEA
end program  Solar_elevation_angle
