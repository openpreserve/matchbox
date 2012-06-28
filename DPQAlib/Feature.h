#pragma once

#include "stdafx.h"

#include <list>
#include <string>

#include <fstream>

#include <cv.h>

#include <tclap/CmdLine.h>
#include <tclap/Arg.h>

#include "OutputParameter.h"
#include "OutputAttribute.h"
#include "VerboseOutput.h"

#include "StringUtils.h"

using namespace std;
using namespace cv;

class Feature
{

private:

	list<OutputParameter> outputParams;
	list<TCLAP::Arg*>     characterizationArguments;
	list<TCLAP::Arg*>     comparisonArguments;
	list<FileNode>        fileNodes;

	string                getFilepath(string featureFileOutputDirectory);

protected:

	string    name;
	string    filename;
	int       level;

	virtual void           writeOutput(FileStorage& fs)            = 0;
	virtual void           readData(FileNode& fs)                  = 0;

	// protected methods
	void                   verbosePrintln(string msg);

public:

	static const string TAG_NAME;
	static const string ATTR_LEVEL;
	static const string ATTR_NAME;

	// constructors / destructors
	Feature(void);
	~Feature(void);

	// virtual methods
	virtual void           execute(Mat& image)                     = 0;
	virtual void           compare(Feature* task)                  = 0;
	virtual void           parseCommandlineArguments()             = 0;
	virtual list<string>*  getCmdlineArguments(void)               = 0;
	virtual void           setCmdlineArguments(list<string>* args) = 0;
	
	// persistence I/O
	void                   persist(string featureFileOutputDirectory);

	

	void                   loadData(void);
	void                   addFilenode(FileNode node);

	// result output methods
	void                   addOutputParameter(OutputParameter param);
	list<OutputParameter>* getOutputParameters();
	void                   printXML(void);	

	// commandline arguments
	void                   addCharacterizationCommandlineArgument(TCLAP::Arg* arg);
	void                   addComparisonCommandlineArgument(TCLAP::Arg* arg);
	list<TCLAP::Arg*>*     getCharacterizationCommandlineArguments();
	list<TCLAP::Arg*>*     getComparisonCommandlineArguments();

	// getter/setter
	string                 getName(void);
	int                    getLevel(void);
	void                   setFilename( string* filename );
	string                 getFilename(void);

	
};