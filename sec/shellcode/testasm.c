/*
 * @Description: 
 * @Version: 2.0
 * @Author: 0pt1mus
 * @Date: 2020-05-01 21:07:51
 * @LastEditors: 0pt1mus
 * @LastEditTime: 2020-05-01 23:48:58
 */
#include<stdio.h>

int main(int argc, char const *argv[])
{
    asm volatile(
        "mov eax,ebx"
    );
    return 0;
}
