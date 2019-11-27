#include <iostream>
#include <armadillo>
//#include <mpi.h>
#include <mpi/mpi.h>
#define ZERO  1.0E-10
#include "heather.h"
#include <fstream>
#include <time.h>

using namespace std;

int main()
{
    ofstream file;
    int N = 500;
    int m0 = 500;
    string s0 = "-";
    string s1 = to_string(N);
    string s2 = to_string(m0);
    float lambd = 0;

    file.open(s1+s0+s2+".txt");

    main_func(N, lambd, m0, file);













    //high performance computing
    //problemløsning med høynivå språk



}
