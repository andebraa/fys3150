#include <iostream>
#include <armadillo>
//#include <mpi.h>
#include <mpi/mpi.h>
#define ZERO  1.0E-10
#include "heather.h"
#include <fstream>
#include <time.h>



void main_func(int N, int m0, ofstream file){
    vec m = zeros<vec>(N); //vector of 500 different agents
    m.fill(m0);



//    int world_rank;
//    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank)
    int seed = time(0);//+world_rank * 10)
    mt19937 engine(seed);

    uniform_int_distribution<int> uniform(0, N-1);
    uniform_real_distribution<double> eps(0,1);

    for(int l = 0; l<1E7; l++){
        int i = uniform(engine);
        int j = uniform(engine);

        double eps_ = eps(engine);
        m(i) = eps_*(m(i) + m(j));
        m(j) = (1-eps_)*(m(i) + m(j));




    }//end for i<1E7
    for(int k = 0; k<501; k++){
        file<<m(k) << "  ";
    }
    file<<"\n";


}
