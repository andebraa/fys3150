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

void vibe_check(int N, int m0, arma::vec &m);
void main_func(int N, float lambd, int m0, ofstream& file){
    vec m = arma::vec(N, arma::fill::zeros); //vector of 500 different agents
    m.fill(m0);



//    int world_rank;
//    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank)
    int seed = time(0);//+world_rank * 10)
    mt19937_64 engine(seed);

    uniform_int_distribution<int> uniform(0, N-1); //for finding the random angents (i)
    uniform_int_distribution<int> uniform2_electric_boogaloo(0, N-2); //random agents (j)!
    uniform_real_distribution<double> double_uniform(0,1); //for finding the amount of mone

    for(int k =0; k< 500; k++){
        for(int l = 0; l<1E7; l++){
            int i = uniform(engine);
            int j = uniform2_electric_boogaloo(engine);

            if (j >= i){
                j++;
            }

            double eps = double_uniform(engine);
            double delt_e = (1 - lambd)*(eps*m[j] - (1 - eps)*m[i]);
            m[i] += delt_e;
            m[j] -= delt_e;
//            cout<<m(i)<<endl;
//            cout << m(j) << endl;


        }//end for i<1E7
    }//end for k < 500
    for(int k = 0; k<N-1; k++){
        file<<m(k) << "  ";

    }
    file<<"\n";
    vibe_check(N, m0, m);

} //end main func

void vibe_check(int N, int m0, arma::vec &m){
    double m_init = N*m0;
    double m_actual = 0;

    m_actual = arma::sum(m);
    /*
    for(int i=0; i < N; i++){
        m_actual += m[i];
    }
    */
    double tol = 1E-15;
    if ((m_init - m_actual )> tol){
        cout<<"aint no good" << endl;
        cout<<m_init-m_actual<<endl;
    }


}
