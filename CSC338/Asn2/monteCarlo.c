/* Monte Carlo
  Assignment 2
  Kyle Finter
  Finter179
*/

#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mpi.h>

int main(int argc, char **argv) {
  //randomize seed using time
  srand(time(NULL));
  
  //passed in as argument
  long long int number_of_tosses = strtoll(argv[1], NULL, 10);
  long long int number_in_circle;
  
  int local_n; //number of throws per process

  //Add MPI boiler plate here
  int comm_sz; //Number of processes
  int my_rank; //Rank of local process
  MPI_Init(NULL, NULL);
  MPI_Comm_size(MPI_COMM_WORLD, &comm_sz);
  MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

  if (my_rank != 0) {
    int i; //Loop index
    long long int local_number_in_circle = 0;  //Initialize to 0
    
	//Get number_of_tosses through broadcast from process 0
    MPI_Bcast(&local_n, 1, MPI_LONG_LONG_INT, 0, MPI_COMM_WORLD);

	double x;
	double y;
	double distance_squared;
    for (i = 0; i < local_n; i++) {
	  //random number between 0 and 1
	  x = (double)rand()/((double)RAND_MAX+(double)(1));
	  //increase range to be between 0 and 2
	  x = x*2;
	  //decrement that number to be between -1 and 1
	  x--;
	  y = (double)rand()/((double)RAND_MAX+(double)(1));
	  y=y*2;
	  y--;
	  distance_squared = x * x + y * y;

	  if(distance_squared <= 1){
		  local_number_in_circle++;
	  }
    }
	//send local value to be summed up into global value
    MPI_Reduce(&local_number_in_circle, &i, 1, MPI_LONG_LONG_INT, MPI_SUM, 0, MPI_COMM_WORLD);

  } else {
    //Send number of tosses to all threads
	local_n = number_of_tosses/comm_sz;
    MPI_Bcast(&local_n, 1, MPI_LONG_LONG_INT, 0, MPI_COMM_WORLD);
    
	int i;
	long long int local_number_in_circle = 0;  //Initialize to 0

    double x;
	double y;
	double distance_squared;
    for (i = 0; i < local_n; i++) {
	  x = (double)rand()/((double)RAND_MAX+(double)(1));
	  x = x*2;
	  x--;
	  y = (double)rand()/((double)RAND_MAX+(double)(1));
	  y = y*2;
	  y--;
	  distance_squared = x * x + y * y;

	  if(distance_squared <= 1){
		  local_number_in_circle++;
	  }
    }

    //Get global sum by combining all local sums
    MPI_Reduce(&local_number_in_circle, &number_in_circle, 1, MPI_LONG_LONG_INT, MPI_SUM, 0, MPI_COMM_WORLD);
    //calculate pi estimate
	double pi_estimate = 4 * number_in_circle / ((double) number_of_tosses);
    printf("PI Estimate: %f\n", pi_estimate);
  } //end else
  MPI_Finalize();
}
