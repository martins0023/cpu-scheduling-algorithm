<h5>To understand the composition of a typical operating system, we first consider the complete spectrum of software found within a typical computer system. Then we will concentrate on the operating system itself.
</h5>
Let us begin by dividing a machine’s software into two broad categories: application software and system software (Figure 3.3). Application software
consists of the programs for performing tasks particular to the machine’s utilization. A machine used to maintain the inventory for a manufacturing company will contain different application software from that found on a machine used by an electrical engineer. Examples of application software include spreadsheets, database systems, desktop publishing systems, accounting systems, program
development software, and games. In contrast to application software, system software performs those tasks that are common to computer systems in general. In a sense, the system software provides the infrastructure that the application software requires, in much the
same manner as a nation’s infrastructure (government, roads, utilities, financial institutions, etc.) provides the foundation on which its citizens rely for their individual lifestyles.

Within the class of system software are two categories: One is the operating system itself and the other consists of software units collectively known as utility software. The majority of an installation’s utility software consists of programs for performing activities that are fundamental to computer installations but not included in the operating system. In a sense, utility software consists of software units that extend (or perhaps customize) the capabilities of the operating system. For example, the ability to format a magnetic disk or to copy a file from a magnetic disk to a CD is often not implemented within the operating system itself but instead is provided by means of a utility program.

Other instances of utility software include software to compress and decompress data, software for playing multimedia presentations, and software for handling network communication.

<h1>The Concept of a Process</h1>
One of the most fundamental concepts of modern operating systems is the distinction between a program and the activity of executing a program. The former is a static set of directions, whereas the latter is a dynamic activity whose properties change as time progresses. (This distinction is analogous to a piece of sheet music, sitting inert in a book on the shelf, versus a musician performing that piece by taking actions that the sheet music describes.) 
The activity of executing a program under the control of the operating system is known as a process. Associated with a process is the current status of the activity, called the process state. This state includes the current position in the program being executed (the value of the program counter) as well as the values in the other CPU registers and the associated memory cells. Roughly speaking, the process state is a snapshot of the machine at a particular time. At different times during the execution of a program (at different times in a process) different snapshots (different process
states) will be observed.
Typical time-sharing/multitasking computers are running many processes, all competing for the computer’s resources. It is the task of the operating system to manage these processes so that each process has the resources (peripheral devices, space in main memory, access to files, and access to a CPU) that it needs, that independent processes do not interfere with one another, and that processes that need to exchange information are able to do so. To perform these multiple processes and allocate each process the required amount of resources, process administration needs to be administered.

<h4>Process Administration</h4>
The tasks associated with coordinating the execution of processes are handled by the scheduler and dispatcher within the operating system’s kernel. The scheduler maintains a record of the processes present in the computer system, introduces new processes to this pool, and removes completed processes from the pool. Thus when a user requests the execution of an application, it is the scheduler that adds the execution of that application to the pool of current processes.
These process scheduling requires some algorithm to be applied for assigning and allocating resources, which we'll delve in below with a programming perspective.

<p>Types of Scheduling</p>
<li>Non-Preemptive :- In simple term, the <b>non-preemptive</b> does not require any inteference or disruption till successfull completion of the process currently being executed.</li>
<li>Preemptive :- the <b>preemptive</b> requires interference, the CPU can be taken away from the process that is currently being executed.</li>

<h5>There are six popular methods of scheduling processes to the CPU, which are: </h5>
<li>First Come, First Serve</li>
<li>Shortest Job First</li>
<li>Priority Scheduling</li>
<li>Shortest Remaining Time</li>
<li>Round Robin(RR)</li>
<li>Multiple-Level Queues</li>

<h1>The Abstract Nature of Algorithms</h1>
It is important to emphasize the distinction between an algorithm and its representation—a distinction that is analogous to that between a story and a book.
A story is abstract, or conceptual, in nature; a book is a physical representation of a story. If a book is translated into another language or republished in a different format, it is merely the representation of the story that changes—the story itself
remains the same.
    In the same manner, an algorithm is abstract and distinct from its representation. A single algorithm can be represented in many ways. As an example,
the algorithm for converting temperature readings from Celsius to Fahrenheit is
traditionally represented as the algebraic formula
<br>                                    F = (9⁄5)C + 32
<br>But it could be represented by the instruction
<br>                                    Multiply the temperature reading in Celsius by 9⁄5
<br>                                    and then add 32 to the product
or even in the form of an electronic circuit. In each case the underlying algorithm is the same; only the representations differ.
    
    The distinction between an algorithm and its representation presents a problem when we try to communicate algorithms. A common example involves the level of detail at which an algorithm must be described. Among meteorologists, the instruction “Convert the Celsius reading to its Fahrenheit equivalent” suffices, but a layperson, requiring a more detailed description, might argue that the instruction is ambiguous. The problem, however, is not with the underlying algorithm but that the algorithm is not represented in enough detail for the layperson.

<br>Finally, while on the subject of algorithms and their representations, we should clarify the distinction between two other related concepts—programs and processes. A program is a representation of an algorithm. (Here we are using the term algorithm in its less formal sense in that many programs are representations of nonterminating “algorithms.”) In fact, within the computing community the term program usually refers to a formal representation of an algorithm designed for computer application. 

<br><i>Excerpts from <b><p>"Computer Science - An Overview, 12th edition. "</b></p></i>

<b><h4>install neccessary dependencies, the only program used in these Algorithm Intepretations is  Python3 and can be installed on linux with the below command. While on windows can be downloaded from the official <a href = "https://www.python.org">site</a></h4></b>

!sudo apt-get install python3


**Testing for first come first serve Algorithm**
<br><hr>
What is <b>First Come First Serve Algorithm</b>: First Come First Serve Algorithm in simple terms means attending to and executing tasks just as they arrive or on their arrival. The task that comes first, gets executed first. It is also a non-preemptive algorithm. While this method ensures that each process has a fair amount of time to be executed, it usually has poor performance due to high average waiting time.

**Output**
Available object on queue 0 is: cat
object on queue 0 will be attended to next... then, object 1
Available object on queue 1 is: dog
object on queue 1 will be attended to next... then, object 2
Available object on queue 2 is: snake
object on queue 2 will be attended to next... then, object 3
Available object on queue 3 is: lizard
object on queue 3 will be attended to next... then, object 4
Available object on queue 4 is: lion
object on queue 4 will be attended to next... then, object 5
Available object on queue 5 is: hen
object on queue 5 will be attended to next... then, object 6

 objects remaining on queue still remains :  6
There are no more suggestions for objects on queue to be executed in this program.
Available object on queue 0 is: nee
object on queue 0 will be attended to next... then, object 1
Available object on queue 1 is: dee
object on queue 1 will be attended to next... then, object 2
Available object on queue 2 is: gee
object on queue 2 will be attended to next... then, object 3
Available object on queue 3 is: ree
object on queue 3 will be attended to next... then, object 4

 objects remaining on queue still remains :  4
object on queue 0 has been successfully executed... object 1  will be executed next..
object on queue 1 has been successfully executed... object 2  will be executed next..
object on queue 2 has been successfully executed... object 3  will be executed next..
object on queue 3 has been successfully executed... object 4  will be executed next..
All actions for objects on queue have been successfully executed


**Testing for Last In First Out (LIFO) with python..** 
<hr>
<b>LAST IN FIRST OUT</b> is a scheduling <i>Algorithm</i> that involves attending to and giving priority to processes that arrives last i.e processes that arrives last in the stack are executed first. It is a reverse process of how <b>FIRST IN FIRST SERVE</b> processes are executed.

**output:**

List of items in stack are; 
HP
DELL
ACER
LENOVO
APPLE
SAMSUNG
HISENSE

List of order of execution for the LAST IN FIRST OUT ALGORITHM will be; 
HISENSE
SAMSUNG
APPLE
LENOVO
ACER
DELL
HP

Item  HISENSE  will be out of the stack first.
Items ramining are: 

 SAMSUNG
 APPLE
 LENOVO
 ACER
 DELL
 HP

Item  SAMSUNG  will be out of the stack next.
Items ramining are: 
 APPLE
 LENOVO
 ACER
 DELL
 HP

Item  APPLE  will be out of the stack next.
Items ramining are: 
 LENOVO
 ACER
 DELL
 HP

Item  LENOVO  will be out of the stack next.
Items ramining are: 
 ACER
 DELL
 HP

Item  ACER  will be out of the stack next.
Items ramining are: 
 DELL
 HP

Item  DELL  will be out of the stack next.
Items ramining are: 
 HP

Item  HP  will be out of the stack next.
Stack emptied. Execution terminated



<h3><b>PRIORITY SCHEDULING </b></h3>
<div class="">
<a href="https://www.google.com/search?priority%scheduling">Priority Scheduling</a> is a non-preemptive algorithm that assigns each task a
priority number to be executed by. If two task arrive at the same time, they
would be dealt in a first come first serve manner. Priority can be decided on a
number of factors such as memory requirements, time requirements or any
other resource requirement.
</div>

**OUTPUT**

PROCESS NAME 	 EXECUTION TIME 	 PRIORITY 	 BURST TIME
HOTDOG 		                5 			 2 		 4
CORN 		                6 			 9 		 3
BACON 		                2 			 4 		 8
CHEESE 		                8 			 8 		 6

The maximum priority for the process is 9
 
So therefore process CORN will be out of the stack first and will be executed for 0 - 6 time length.
______________________________________________________________________________
processes left with their corresponding busrt, execution time and priority; 

PROCESS NAME 	 EXECUTION TIME 	 PRIORITY 	 BURST TIME

HOTDOG 		                5 			 2 		 4

BACON 		                2 			 4 		 8

CHEESE 		                8 			 8 		 6

The next maximum priority for the process is 8
 
So therefore process CHEESE will be out of the stack next and will be executed for 6 - 14 time length.
______________________________________________________________________________
processes left with their corresponding busrt, execution time and priority; 

PROCESS NAME 	 EXECUTION TIME 	 PRIORITY 	 BURST TIME

HOTDOG 		                5 			 2 		 4

BACON 		                2 			 4 		 8

The next maximum priority for the process is 4
 
So therefore process BACON will be out of the stack next and will be executed for 14 - 16 time length.
______________________________________________________________________________
processes left with their corresponding busrt, execution time and priority; 

PROCESS NAME 	 EXECUTION TIME 	 PRIORITY 	 BURST TIME

HOTDOG 		                5 			 2 		 4

The next maximum priority for the process is 2
 
So therefore process HOTDOG will be out of the stack next and will be executed for 16 - 21 time length.

All execution has been completed successfully! 
Total number of executions = 21



<h3><b>Shortest Job First</b></h3>
Shortest Job First is a preemptive algorithm that executes the shortest job first.
This algorithm uses one of the best tactic to minimize or reduce the waiting time, when the processor knows in advance how much time it will take to complete each process. In an interactive Operating System this algorithms fails, since small process will get to cut the line each time they arrive which could lead to starvation of the longer tasks.



PROCESS NAME 	 ARRIVAL TIME 		 EXECUTION TIME 	 SERVICE TIME

 CASHEW 		 0 			            10 			 8

 PINEAPPLE 		 1 			            7 			 13

 LOLLIPOP 		 2 			            2 			 11

 JERGENS 		 3 			            9 			 20

The shortest job first for the process is 8
 
So therefore process CASHEW will be out of the processes first and will be executed for 0 - 10 time length.
______________________________________________________________________________
processes left with their corresponding arrival, execution time and service time; 

PROCESS NAME 	 ARRIVAL TIME 		 EXECUTION TIME 	 SERVICE TIME

 PINEAPPLE 		 1 			                7 			 13

 LOLLIPOP 		 2 			                2 			 11

 JERGENS 		 3 			                9 			 20

The next shortest job for the process is 11
 
So therefore process LOLLIPOP will be out of the processes next and will be executed for 10 - 12 time length.
______________________________________________________________________________
processes left with their corresponding arrival, execution time and service time; 

PROCESS NAME 	 ARRIVAL TIME 		 EXECUTION TIME 	 SERVICE TIME

 PINEAPPLE 		 1 			                7 			 13

 JERGENS 		 3 			                9 			 20

The next shortest job for the process is 13
 
So therefore process PINEAPPLE will be out of the processes next and will be executed for 12 - 19 time length.
______________________________________________________________________________
processes left with their corresponding arrival, execution time and service time; 

PROCESS NAME 	 ARRIVAL TIME 		 EXECUTION TIME 	 SERVICE TIME

 JERGENS 		 3 			                9 			 20

The next shortest job for the process is 20
 
So therefore process JERGENS will be out of the processes next and will be executed for 19 - 28 time length.

All execution has been completed successfully! 
Total number of executions = 28