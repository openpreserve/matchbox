#matchbox

*Matchbox* detects duplicate pages in digitised document collection.

### What does matchbox do?
*Matchbox* is an [open source tool](https://github.com/openplanets/matchbox) providing decision-making support for quality assurance tasks concerning document image collections. The tool aims at comparing digitized text documents.
 A main advantage is its general approach that works where OCR will not, for example images of handwriting or music scores. 
 
### Use cases for *Matchbox* image based tool
* detect duplicates in or across document image collections
* compare two image documents for similarity (1 - similar, 0 - not similar)
* support collections assembling from multiple sources
* identify missing files in a document collection

### *Matchbox* advantages
* reduces involvement of a human expert
* automated analysis with *Matchbox* is faster then human expert
* reduces costs for quality assurance processes
* works also with handwritten text
* works also for music scores
* works for mathematical expressions
* works independent from file format
* works independent from file size
* works independent from text rotation
* works independent from text cropping
* works independent from text colour

*Matchbox* development was partially supported by the [SCAPE](http://www.scape-project.eu/) Project. The SCAPE project is co-funded by the European Union under FP7 ICT-2009.4.1 (Grant Agreement number 270137).

### What are the benefits for end user?

* User can make quality assurance for digital collections
* User can automatically detect duplicates in or across document image collections and save expert time, storage space and money
* Tool works without OCR and independent from format, size, rotation, cropping and colour of the document
* User can identify missing files comparing new and old version of digital book.
* Tool works also for handwritten text like chinese scripts.

### Who is intended audience?

Matchbox is designed for:

* Content holders
* Preservation experts
* Institutions that would like to do quality assurance on digital document collections

## Features and roadmap

### Version 1.0

* Duplicate detection in a digital document collection
* SSIM image comparison

## How to install and use

### Requirements

To install you need:

* Latest version of OpenCV
* Python 2.7
* Git

### Download

| Version | Size   | SHA1                                                    |                      |
|---------|--------|---------------------------------------------------------|----------------------|
| v1.0    | 23.6 MB| <small>1b34d11f66fe4b847f271a5aaaabb02c7917690c</small> |[download](https://github.com/openplanets/matchbox/archive/master.zip)            |

### Install instructions

Please refere to the INSTALL file in the source directory [1].

### Use

#### Matchbox Tools

* extractfeatures

This tool extracts features from images. The set of features implemented  contains  the basic image metadata extraction, the basic image processing features Color Histograms and Image Profiles, as well as more complex features based on interest point detection.
	
Features can be either extracted all at once or by distinctively specifiyng the required feature. Extracted features are either stored to the same directory of the corresponding image, or to a specified directory.  Features  can  be  stored in gzipped xml format or in binary  format. Binary storage  enables  faster processing while xml provides more flexibility for data processing with third party tools.
	
The stored feature filenames have the format:
	
<original_image_filename>.<featurename>.<dat|xml.gz>
e.g. img00001.tif.ImageHistogram.xml.gz
	
* compare

The compare tool compares two extracted features and  calculates a similarity estimation.
	
Input files have to be of the same feature set. Comparison between different feature sets is not possible. Also only two files can be compared with each other, not a set of files.
	
The resulting similarity estimation is written in xml format to standard output (e.g. the command line interface).
	
* train

The train tool is a specialized tool to create visual vocabularies based on visual bag-of-words. A visual bag-of-words is a pendant to the bag-of-words in classical information retrieval, where each text document is represented as a histogram of its distinctive word occurnces. This approach  has  been  adopted  in image processing based on features from interest point detectors - especially SIFT features.
	
The train tool takes a list of SIFT descriptors and applies a clustering algorithm onto it. The calculated centroids represent the visual vocabulary that will be used in further processing of certain workflows.
	

#### Basic Workflows
---------------------

* Duplicate Detection

Duplicate detection is the task of detecting duplicates within an image collection.
	
1. extract SIFTComaparison features of all images
2. train a visual vocabulary on the extracted features
3. extract BoWHistograms using the vocabulary and all extracted SIFTCompairison features
4. create a similarity matrix for the collection using compare on all BoWHistogram features
5. take the top-most similar images for each image and compare their SIFTComparison features.
6. Set a threshold based on the retrieved data.
7. images with an SSIM exceeding the threshold are considered to be duplicates.

## More information

### Publications

* R. Huber-Mörk and A. Schindler. Quality assurance for document image collections in digital preservation. In Proc. of the 14th Intl. Conf. on ACIVS (ACIVS 2012), volume 7517 of LNCS, pages 108-119, Brno, Czech Republic, September 4-7 2012. Springer.
* R. Huber-Mörk, A. Schindler, and S. Schlarb. Duplicate deterction for quality assurcance of document image collections. In In iPRES 2012 - Proceedings of the 9th International Conference on Preservation of Digital Objects, pages 136-143, Toronto, Canada, October 1-5 2012.
* R. Graf, R. Huber-Mörk, A. Schindler, S. Schlarb. An expert system for quality assurance of document image collections. EuroMed 2012, Limassol, Cyprus; 29.10.2012 - 03.11.2012; in: Progress in Cultural Heritage Preservation, Springer, Berlin, Heidelberg (2012), pages 251-260.

### Acknowledgements

Part of this work was supported by the European Union in the 7th Framework Program, IST, through the SCAPE project, Contract 270137.

### Support

This tool is supported by the [Open Planets Foundation](http://www.openplanetsfoundation.org). 

## Command line use

### Sample usage
python2.7 ./FindDuplicates.py /home/matchbox/matchbox-data/ all

### Output of duplicates detection script is a list of possible duplicates (e.g. document 10 is a duplicate candidat for page 2)
[1 of 20] 1
[2 of 20] 2 => [10]
[3 of 20] 3

### SSIM comparison sample
extractfeatures.exe <img1>
extractfeatures.exe <img2>
compare <img1>.feat.xml <img2>.feat.xml

### Output of SSIM comparison with value between 0 and 1, where 1 means high similarity
<SIFTCompairison>
   <SSIM>0.889990</SSIM>
   ...
</SIFTCompairision>

