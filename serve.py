#!/usr/bin/env python

from mpi4py import MPI
import numpy
import sys
import os

def serve(size):
  data = numpy.matrix('0 1.5; 2.1 3')
  data = comm.bcast(data,root=0) #broadcast to all machines


  for i in range(1,size): #for all ranks but the server's
    r=numpy.matrix(numpy.zeros((3,1)))
    comm.Recv(r, source=i, tag=1) #receive from one machine
    print r #should print out three different 3x1 matrices

  r2=numpy.matrix(numpy.zeros((2,1)))
  r2=comm.gather(r2,root=0)
  print 'r2',r2 #r2 is now a list of all machines' r2 values, including its
  #own. So when printed, r2[0] is the zeros created two lines ago.
  print 'sum of r2',sum(r2)

###########################################################

def client(rank):
  data = None
  data = comm.bcast(data,root=0) #client's part of broadcast; root=0 means get
  #the data from the process with rank 0 (which is the server)
  print data #should be "data" from serve()


  r=numpy.matrix(numpy.random.rand(3,1))
  comm.Send(r, dest=0, tag=1) #send from one machine to another

  
  r2=numpy.matrix(numpy.random.rand(2,1))
  r2=comm.gather(r2, root=0)


comm = MPI.COMM_WORLD
rank = comm.Get_rank() #different identification rank for each process
size = comm.Get_size() #number of processes in communication

if rank == 0: #if server,
  serve(size)
else:
  client(rank)
