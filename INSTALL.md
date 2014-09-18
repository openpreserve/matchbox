Matchbox Toolset Installation Guide 
=================================== 

This file describes how to build Matchbox from the source distribution. 

*Alexander Schindler <alexander.schindler@ait.ac.at>*
*Roman Graf <roman.graf@ait.ac.at>*

### Requirements 


#### CMake 

To build OpenCV and the Matchbox commandline tools Visual Studio solutions or 
Makefiles for MinGW or gcc have to be generated using CMake. 

##### Installing CMake

For Windows, download cMake from the cMake 
website http://www.cmake.org and install it. 

For Linux, cMake usually can be installed via the distribution package manager. 
E.g. for Ubuntu 
	
	sudo aptitude install cmake

#### Open Computer Vision Library (OpenCV)

The Open Source Computer Vision (OpenCV) libarary opencv_library is a 
library of programming functions for real time computer vision. It is released 
under a Berkeley Software Distribution (BSD) 
http://opensource.org/licenses/bsd-license.php license and thus is free for 
commercial or research use. The library provides a wide range of implemented 
algorithms on image analyses, image data and matrix manipulation, basic and 
advanced image processing, object recognition and image feature extraction. 

Most of Matchbox'es implementation is based on routines provided by OpenCV. 

##### Installing OpenCV

The OpenCV source code can be downloaded from the OpenCV 
website http://opencv.willowgarage.com/wiki/ for all platforms. 
It is necessary to generate either Visual Studio solutions or Makefiles with 
cMake to build it. 

To do this, start CMake, browse to the directory where the downloaded OpenCV 
source code resides, choose a directory where OpenCV will be built, click 
'Configure' to choose which compiler you want to use, click 'Finish' and 
then click 'Generate'. 

The Visual Studio solution or the Makefile can then be found in the build 
directory. 

#### Python

Python is a popular dynamic programming language. Python is used to model 
diverse use cases and workflows of document image quality assurance. 

Modules required by Matchbox: 

* Numpy - Numerical Python 
* Argparse - Parser for command-line options, arguments and sub-commands

##### Installing Python

Python comes with most linux distributions out of the box. For Windows, install 
Python from the Python website http://www.python.org. The 
additional libraries can also be found on the website or in the package 
repositories of the Linux distribution of your choice. 

#### C++ Compiler

##### Linux

Matchbox can be built with gcc, a compiler that is shipped with most Linux 
distributions. 

##### Windows

On Windows, either Visual Studio or MinGW (MinGW is open source software and can 
be downloaded from their website http://www.mingw.org/ for 
free) can be used to build the code. 

#### Optional Packages

* Intel Threading Building Blocks Library (TBB)


### Installing Matchbox 

#### Installation on Linux

Manual compilation:
Manual compilation should be straightforward: 
After you made sure that the requirements are fulfilled, navigate to the source 
code directory and enter 

	mkdir build 
	cd build 
	cmake .. 
	make sudo 
	make install 

If the compilation succeeded, the commandline tools extractfeatures, 
train, compare, FindDuplicates.py and CompareCollections.py are available. 


#### Installation on Windows

#### Compiling Matchbox using MinGW

An environment variable called OPENCV\_DIR, pointing to the directory where 
OpenCV was built, has to be defined. This can be done by right-clicking ``My 
Computer'', choosing ``Properties'' and changing to the ``Advanced'' tab. After 
clicking the button ``Environment variables'', an environment variable can be 
added. 

As a next step, a MinGW Makefile has to be generated using CMake. 
Start CMake, click 'Browse Source' and find the directory containing the 
Matchbox source. Click 'Browse Build' and choose a directory where the code 
will be built. Click 'Configure' and choose 'MinGW Makefiles' from the 
dropdown menu. Below the dropdown menu, 'Use default native compilers' has to 
be selected. Click 'Finish'. 
After cMake finished configuring, click 'Generate'. After cMake is done, the 
Makefile can be found in the build directory. 

Start the MinGW shell and navigate to the directory you specified as build 
directory. Enter the command mingw32-make and press enter. The sourcecode 
should now compile successfully. Issuing the command mingw32-make install 
copies the executables and libraries to the right places in the filesystem. 

