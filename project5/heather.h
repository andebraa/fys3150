#ifndef HEATHER_H
#define HEATHER_H


#include <iostream>
#include <armadillo>
//#include "mpi.h"
#include <fstream>


using namespace std;
using namespace arma;


void main_func(int N, float lambd, int mc_cycles, int m0, ofstream& file, double alpha, double gamma);
void vibe_check(int N,int m0, vector <double> m);

#endif // HEATHER_H
