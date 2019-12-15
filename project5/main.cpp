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
    /*
    float lambd= 0.25;
    string s4 = to_string(lambd);

    file.open(s1+s0+s2+s0+s4+".txt");

    main_func(N, lambd, mc_cycles, m0, file);

    lambd= 0.5;
    s4 = to_string(lambd);

    file.open(s1+s0+s2+s0+s4+".txt");
    main_func(N, 0.5, mc_cycles, m0, file);
    */




    string s4;
    string s5;

    double gamma = 2;

    double lambda_values [5] = {0, 0.25, 0.4, 0.5, 0.9};

    double alpha = 0;
    s5 = to_string(alpha);
    s4 = to_string(0.5);

    file.open(s1+s0+s2+s0+s4+s0+s5+"histogram_values_to_fit_parametrization"+s0+".txt");
    main_func(N, 0.5, mc_cycles, m0, file, alpha, gamma);


    /*
    for(int i  = 2; i < 3; i++){
        s5 = to_string(alpha);
        s4 = to_string(lambda_values[i]);

        cout<<i<<endl;

        file.open(s1+s0+s2+s0+s4+s0+s5+"histogram_values_to_fit_parametrization"+s0+".txt");
        main_func(N, lambda_values[i], mc_cycles, m0, file, alpha, gamma);
    }//end for alpha=0.5
    */








}
