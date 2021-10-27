#### 1.Significant earthquakes since 2150 B.C

##### 1.1 Compute the total number of deaths caused by earthquakes since 2150 B.C. in each country, and then print the top ten countries along with the total number of deaths.

```python
# The result of top ten countries along with the total number of deaths is following:
Country
CHINA         2041784.0
TURKEY         867454.0
IRAN           758638.0
SYRIA          437700.0
ITALY          359064.0
JAPAN          355137.0
HAITI          323770.0
AZERBAIJAN     310119.0
INDONESIA      280351.0
ARMENIA        189000.0
Name: Total Deaths, dtype: float64
```

##### 1.2 Compute the total number of earthquakes with magnitude larger than 6.0 (use column Mag as the magnitude) worldwide each year, and then plot the time series. Do you observe any trend? Explain why or why not?

```python
# The result of the total number of earthquakes with magnitude larger than 6.0 worldwide each year is following:
Year
-2150.0     1
-2000.0     1
-1250.0     1
-1050.0     1
-479.0      1
           ..
 2017.0    32
 2018.0    28
 2019.0    27
 2020.0    15
 2021.0    18
Name: Year, Length: 530, dtype: int64
```

The figure of time series only use the year as the x. 

**通过下图可以看出全球地震震级大于6级以上的地震总次数呈现一个先总体不变，然后在1500年左右开始出现上升的趋势，同时，近百年来的次数显著大于过去。猜测这种现象出现的一个主要原因是随着时间的推进，监测地震的技术手段在提升，因此观测到的6级以上的地震次数增加，而古代的数据可能只有造成重大影响的地震才有可能被记录下来，因此存在数据缺失等问题，至于在千年中的地壳活跃程度是否变得更加剧烈还有待别的证据来证明。**

![image-20211027132429218](C:/Users/Administrator/blog/image/PS2/image-20211027132429218.png)

##### 1.3 Write a function CountEq_LargestEq that returns both (1) the total number of earthquakes since 2150 B.C. in a given country AND (2) the date of the largest earthquake ever happened in this country. Apply CountEq_LargestEq to every country in the file, report your results in a descending order.

```python
#(1)对CountEq_LargestEe(Sig_Eqs, Country)的测试结果：
#以Country = 'CHINA'为例，输出的结果为：
Date
1668-07-25 in CHINA    610
Name: CountEq, dtype: int64
        
#(2)Apply CountEq_LargestEq to every country in the file and result in a descending order
#输出结果为：(期中Total_number代表的是对应国家发生地震的总次数，而Date-I~III代表的是对应国家历史上发生最大的地震的日期，格式为Year-Month-Day,数据类型为str)
     Total_number                                  Date-I Date-II Date-III
0             610                     1668-07-25 in CHINA    None     None
1             409                     2011-03-11 in JAPAN    None     None
2             401                 2004-12-26 in INDONESIA    None     None
3             380                       856-12-22 in IRAN    None     None
4             330                    1916-01-24 in TURKEY    None     None
..            ...                                     ...     ...      ...
152             1                    1819-08-31 in NORWAY    None     None
153             1  1921-09-16 in CENTRAL AFRICAN REPUBLIC    None     None
154             1                     1914-10-23 in PALAU    None     None
155             1                  1905-06-30 in KIRIBATI    None     None
156             1                       2021-10-12 in NAN    None     None

[157 rows x 4 columns]
```

