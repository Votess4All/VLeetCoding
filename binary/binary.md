1. 进制转换

1.1 十进制转二进制

思路：将某个十进制数除2得到的整数部分保留，作为第二次除2时的被除数，得到的余数依次记下，
重复上述步骤，直到整数部分为0就结束，将所有得到的余数最终**逆序**输出，则为该十进制对应的二进制数。

```
EXAMPLE：
1、 9(10)->1001(2)
9 / 2 = 4 ...... 1;
4 / 2 = 2 ...... 0;
2 / 2 = 1 ...... 0;
1 / 2 = 0 ...... 1; 倒过来就是 1001 (2)进制
```