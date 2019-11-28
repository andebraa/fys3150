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
    int mc_cycles = 1E3;
    string s0 = "-";
    string s1 = to_string(N);
    string s2 = to_string(m0);
    string s3 = to_string(mc_cycles);

    float lambd= 0.25;
    string s4 = to_string(lambd);

    file.open(s1+s0+s2+s0+s4+".txt");

    main_func(N, lambd, mc_cycles, m0, file);

    file.open(s1+s0+s2+".txt");
    main_func(N, 0.5, mc_cycles, m0, file);








//kjør koden for forskjellige lambda!




    //high performance computing
    //problemløsning med høynivå språk



}
