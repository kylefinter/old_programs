/* Parallel hello from Pacheco, Ch3 */
#include <stdio.h>
#include <string.h> //For Strlen
#include <mpi.h> //For mpi functions

const int MAX_STRING=100; //Max length of string

int main(void){
  char greeting[MAX_STRING];
  char report[MAX_STRING+100];
  int comm_sz;  //Number of processes
  int my_rank;  //My process rank
  int q;        //Used for loop index

  MPI_Init(NULL, NULL); //Prepare for mpi calls
  MPI_Comm_size(MPI_COMM_WORLD, &comm_sz);  //Get no. of processes
  MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);  //Get rank of process

  if (my_rank != 0){
    if (my_rank == comm_sz){
      sprintf(greeting, "Greetings to process %d from process %d!", 0, my_rank);
      MPI_Send(greeting, strlen(greeting)+1, MPI_CHAR, my_rank+1, 0, MPI_COMM_WORLD);
      sprintf(report, "Process %d received this message: %s", my_rank, greeting);
      MPI_Send(report, strlen(report)+1, MPI_CHAR, 0, 0, MPI_COMM_WORLD);
    }
    sprintf(greeting, "Greetings to process %d from process %d!", my_rank+1, my_rank);
    MPI_Send(greeting, strlen(greeting)+1, MPI_CHAR, my_rank+1, 0, MPI_COMM_WORLD);
    sprintf(report, "Process %d received this message: %s", my_rank, greeting);
    MPI_Send(report, strlen(report)+1, MPI_CHAR, 0, 0, MPI_COMM_WORLD);
  } else{
    printf("Greetings from process %d of %d!\n", my_rank, comm_sz);
    for(q=1; q<comm_sz;q++){
      MPI_Recv(greeting, MAX_STRING, MPI_CHAR, q, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE); //Receive msg from process q
      printf("%s\n", greeting);
      MPI_Recv(report, MAX_STRING+100, MPI_CHAR, q, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
      printf("%s\n", report);
    }
  }
  MPI_Finalize(); //Clean up - no mpi calls after this
  return 0;
}
