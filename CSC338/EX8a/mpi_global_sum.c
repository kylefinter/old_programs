#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mpi.h>

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
int main(void) {
  const int global_n = 40;  //Number of numbers in input file
  const int local_n = 10;  //Number of numbers for each process
  int globalArray[global_n];  //Declare an int array of size global_n to hold all the numbers
  int localArray[local_n];  //Declare an array of size local_n to hold the local numbers
  int localSum;  //Declare an int to hold the local sum
  int globalSum;  //Declare an int to hold the global sum

  //Add MPI boiler plate here
  int comm_sz;  //Number of processes
  int my_rank;  //My process rank

  MPI_Init(NULL, NULL); //Prepare for mpi calls
  MPI_Comm_size(MPI_COMM_WORLD, &comm_sz);  //Get no. of processes
  MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);  //Get rank of process

  if (my_rank != 0) {
    /* Get numbers from process 0 using MPI_Scatter
       Calculate local sum
       Participate in global sum calculation: call MPI_Reduce
    */
    int i;
    localSum = 0;
    MPI_Scatter(globalArray, local_n, MPI_INT, localArray, local_n, MPI_INT, 0, MPI_COMM_WORLD);
    for(i=0; i<local_n; i++) {
      localSum = localSum + localArray[i];
    }
    MPI_Reduce(&localSum, NULL, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
  } else {
    /* Read numbers from file into array[global_n] using readfile()
       Distribute numbers using MPI_Scatter()
       Calculate local sum
       Get global sum by calling MPI_Reduce()
       Print global sum:
         printf("Global sum: %d\n", variable_name);
    */
    int i;
    char fileName[] = "randnums.txt";
    localSum = 0;
    globalSum = 0;
    readfile(fileName,globalArray);
    MPI_Scatter(globalArray, local_n, MPI_INT, localArray, local_n, MPI_INT, 0, MPI_COMM_WORLD);
    for(i=0; i<local_n; i++) {
      localSum = localSum + localArray[i];
    }
    MPI_Reduce(&localSum, &globalSum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    printf("Global sum: %d\n", globalSum);

  } //end else
  MPI_Finalize();  //Clean up
}
