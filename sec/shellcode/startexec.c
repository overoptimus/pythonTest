/*
 * @Description: 
 * @Version: 2.0
 * @Author: 0pt1mus
 * @Date: 2020-05-01 20:23:09
 * @LastEditors: 0pt1mus
 * @LastEditTime: 2020-05-01 20:33:02
 */
#include<stdio.h>
#include<unistd.h>

int main(int argc, char const *argv[])
{
    execve("/bin/sh", NULL, NULL);
    return 0;
}
