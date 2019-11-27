#include <iostream>
#include <armadillo>
//#include <mpi.h>
#include <mpi/mpi.h>
#define ZERO  1.0E-10
#include "heather.h"
#include <fstream>
#include <time.h>

using namespace std;
using namespace arma;

void vibe_check(int N, int m0, vector <double> &m);
void main_func(int N, float lambd, int m0, ofstream& file){
    vec m = zeros<vec>(N); //vector of 500 different agents
    m.fill(m0);



//    int world_rank;
//    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank)
    int seed = time(0);//+world_rank * 10)
    mt19937 engine(seed);

    uniform_int_distribution<int> uniform(0, N-1); //for finding the random angents (i)
    uniform_int_distribution<int> uniform2_electric_boogaloo(0, N-2); //random agents (j)!
    uniform_real_distribution<double> eps(0,1); //for finding the amount of mone

    for(int l = 0; l<1E7; l++){
        int i = uniform(engine);
        int j = uniform2_electric_boogaloo(engine);

        if (j >= i){
            j++;                         //ELIN har dette, skjønner ikke hvorfor??!
        }

        double eps_ = eps(engine);
        double delt_e = (1 - eps_)*(m(i) + m(j));
        m[i] = eps_*(m[i] + m[j]);
        m[j] = (1-eps_)*(m[i] + m[j]);
        cout<<m(i)<<endl;


    vibe_check(N, m0, m);

    }//end for i<1E7
    for(int k = 0; k<N-1; k++){
        file<<m(k) << "  ";
    }
    file<<"\n";


}

void vibe_check(int N, int m0, vector <double> &m){
    double m_init = N*m0;
    double m_actual = 0;

    for(int i=0; i < N; i++){
        m_actual += m[i];
    }
    double tol = 1E-14;
    if ((m_init - m_actual )> tol){
        cout<<"aint no good" << endl;
    }


}
