//Kyle Finter
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mpi.h>

int findlen(char* fname) {
  //Returns the number of integers in the file fname
  FILE* f;
  int x;  //Variable to receive numbers read from the file
  int n = 0;  //Variable to count numbers in the file

  f = fopen(fname, "r");
  while (fscanf(f, "%d", &x) > 0) n++;
  fclose(f);
  //printf("Findlen returns %d\n", n);
  return n;
}

int readfile(char fname[], int nums[]) {
  FILE* f;
  int i;  //Loop index
  f = fopen(fname, "r");
  i = 0;
  while (fscanf(f, "%d", &nums[i]) > 0) {
    i++;
  }
  fclose(f);
  return i;
}

int main(int argc, char **argv) {
  char fname[] = "randnums40.txt";
  int global_n = findlen(fname);  //Number of numbers in input file
  int processes = strtoll(argv[1], NULL, 10);
  int local_n = global_n/processes;  //Number of numbers for each process
  int globalArray[global_n];  //Declare an int array of size global_n to hold all the numbers
  int localArray[local_n];  //Declare an array of size local_n to hold the local numbers
  int localSum;  //Declare an int to hold the local sum
  int globalSum;  //Declare an int to hold the global sum
  double start_time, end_time;
  //Add MPI boiler plate here
  int comm_sz = strtoll(argv[1], NULL, 10);  //Number of processes
  int my_rank;  //My process rank
  MPI_Init(NULL, NULL); //Prepare for mpi calls
  MPI_Comm_size(MPI_COMM_WORLD, &comm_sz);  //Get no. of processes
  MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);  //Get rank of process
  start_time=MPI_Wtime();
  if (my_rank != 0) {

    int i;
    localSum = 0;
    MPI_Scatter(globalArray, local_n, MPI_INT, localArray, local_n, MPI_INT, 0, MPI_COMM_WORLD);
    for(i=0; i<local_n; i++) {
      localSum = localSum + localArray[i];
    }
    MPI_Reduce(&localSum, NULL, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
  } else {

    int i;
    localSum = 0;
    globalSum = 0;
    readfile(fname,globalArray);
    MPI_Scatter(globalArray, local_n, MPI_INT, localArray, local_n, MPI_INT, 0, MPI_COMM_WORLD);
    for(i=0; i<local_n; i++) {
      localSum = localSum + localArray[i];
    }
    MPI_Reduce(&localSum, &globalSum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
    end_time=MPI_Wtime();
    printf("Global sum: %d\n", globalSum);
    printf("Time to process: %e\n", end_time-start_time);
  } //end else
  MPI_Finalize();  //Clean up

  return 0;
}
