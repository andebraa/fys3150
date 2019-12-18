#include <iostream>
#include <armadillo>
//#include <mpi.h>
//#include <mpi/mpi.h>
#define ZERO  1.0E-10
#include "heather.h"
#include <fstream>
#include <time.h>

using namespace std;

int main()
{
    ofstream file;
    int N = 1000;
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




    string s4;string s5;string s6;

    double lambda_values [5] = {0, 0.25, 0.4, 0.5, 0.9};
    double gamma_values[5] = {0.0, 1.0, 2.0, 3.0, 4.0};

    double alpha_values[2] = {1.0, 2.0};

    for(int i  = 1; i < 2; i++){//gamma values
        for(int j = 1; j<2; j++){//alpha values
            for(double lambda = 0.9; lambda < 1.0; lambda += 0.9){
                s6 = to_string(lambda);
                s5 = to_string(alpha_values[j]);
                s4 = to_string(gamma_values[i]);

                cout<<gamma_values[i]<< " " << alpha_values[j] << " " << lambda <<endl;

                file.open(s1+s0+s2+s0+"gamma"+s4+s0+"alpha"+s5+s0+"lambda"+s6+".txt");
                main_func(N, lambda, mc_cycles, m0, file, alpha_values[j], gamma_values[i]);

            }
        }//end j =0 j < 1
    }//end for alpha=0.5









}
