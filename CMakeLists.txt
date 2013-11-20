
cmake_minimum_required(VERSION 2.8)

# === Project specific parameters

project(scape-matchbox)

SET(MAJOR_VERSION 1)
SET(MINOR_VERSION 0)
SET(PATCH_VERSION 0)

# === global build parameters

SET(BUILD_SHARED_LIBS ON)

SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fpermissive ")

SET(CMAKE_CXX_LINK_EXECUTABLE "${CMAKE_CXX_LINK_EXECUTABLE} -static-libgcc -static-libstdc++")
SET(CMAKE_C_LINK_EXECUTABLE "${CMAKE_C_LINK_EXECUTABLE} -static-libgcc -static-libstdc++")

# WP - force this option on (only relevant when building .deb)
option(withLibs "withLibs" ON)

# === find and add required ressources

find_path(OPENCV_DIR OpenCVConfig.cmake HINTS $ENV{PATH} $ENV{OPENCV_DIR} $ENV{OPENCVDIR} $ENV{OpenCVDIR} $ENV{OPENCV_DIR} $ENV{OpenCV_DIR})
FIND_PACKAGE(OpenCV REQUIRED)

if(OpenCV_FOUND)
message(STATUS "COMPARE: Opencv found.")
ENDIF(OpenCV_FOUND)

set(Boost_USE_STATIC_LIBS OFF)
set(Boost_USE_MULTITHREADED ON) 
set(Boost_USE_STATIC_RUNTIME OFF)
FIND_PACKAGE(Boost COMPONENTS serialization)

INCLUDE_DIRECTORIES("./libs/tclap/include")
INCLUDE_DIRECTORIES(${OpenCV_INCLUDE_DIR})
INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIRS})

# === CPack packaging parameters

IF(EXISTS "${CMAKE_ROOT}/Modules/CPack.cmake")
INCLUDE(InstallRequiredSystemLibraries)

# WP - this is the default installation path for the .deb
# NOTE: this should not currently be /usr/ as the binary names
# conflict with ImageMagick
set(DEB_INSTALL_DIR                "/usr/")

SET(CPACK_PACKAGE_VERSION_MAJOR    "${MAJOR_VERSION}")
SET(CPACK_PACKAGE_VERSION_MINOR    "${MINOR_VERSION}")
SET(CPACK_PACKAGE_VERSION_PATCH    "${PATCH_VERSION}")
set(CPACK_PACKAGE_VERSION          "${MAJOR_VERSION}.${MINOR_VERSION}.${CPACK_PACKAGE_VERSION_PATCH}")

# WP - this list is based on the libraries detected by cmake in Travis CI and other additional known dependencies
set(DEB_DEPENDS "zlib1g, python (>=2.7), python-numpy, libjpeg8, libtiff4, libpng12-0, libjasper1, libopenexr6, libboost-all-dev")

IF (withLibs)
	SET(CPACK_PACKAGE_NAME             "${CMAKE_PROJECT_NAME}_${MAJOR_VERSION}.${MINOR_VERSION}.${CPACK_PACKAGE_VERSION_PATCH}_incl_libs")
	SET(CPACK_PACKAGE_FILE_NAME        "${CMAKE_PROJECT_NAME}_${MAJOR_VERSION}.${MINOR_VERSION}.${CPACK_PACKAGE_VERSION_PATCH}_incl_libs")
	SET(CPACK_SOURCE_PACKAGE_FILE_NAME "${CMAKE_PROJECT_NAME}_${MAJOR_VERSION}.${MINOR_VERSION}.${CPACK_PACKAGE_VERSION_PATCH}_incl_libs")
	SET(CPACK_DEBIAN_PACKAGE_DEPENDS    ${DEB_DEPENDS})
ELSE (withLibs)
# WP - this won't work as Matchbox currently relies on features in OpenCV that are not packaged by Debian/Ubuntu
	SET(CPACK_PACKAGE_NAME             "${CMAKE_PROJECT_NAME}_${MAJOR_VERSION}.${MINOR_VERSION}.${CPACK_PACKAGE_VERSION_PATCH}")
	SET(CPACK_PACKAGE_FILE_NAME        "${CMAKE_PROJECT_NAME}_${MAJOR_VERSION}.${MINOR_VERSION}.${CPACK_PACKAGE_VERSION_PATCH}")
	SET(CPACK_SOURCE_PACKAGE_FILE_NAME "${CMAKE_PROJECT_NAME}_${MAJOR_VERSION}.${MINOR_VERSION}.${CPACK_PACKAGE_VERSION_PATCH}")
# WP - list additional OpenCV package dependencies here
	SET(CPACK_DEBIAN_PACKAGE_DEPENDS   "libcv2.4.4,python-opencv," ${DEB_DEPENDS})
ENDIF (withLibs)

SET(CPACK_PACKAGE_DESCRIPTION         "Matchbox Tools")
SET(CPACK_PACKAGE_DESCRIPTION_SUMMARY "The SCAPE Matchbox Toolbox is a toolset for detecting duplicate entires in document image collections.")
SET(CPACK_PACKAGE_VENDOR              "Austrian Institute of Technology AIT")
SET(CPACK_PACKAGE_CONTACT             "alexander.schindler@ait.ac.at")

SET(CPACK_RESOURCE_FILE_README        ${CMAKE_CURRENT_SOURCE_DIR}/README.txt)

SET(CPACK_DEBIAN_PACKAGE_PRIORITY     "optional")
SET(CPACK_DEBIAN_PACKAGE_SECTION      "tools")
SET(CPACK_DEBIAN_ARCHITECTURE         "i386")

SET(CPACK_COMPONENTS_ALL Libraries ApplicationData)
SET(CPACK_SET_DESTDIR "on")
SET(CPACK_PACKAGING_INSTALL_PREFIX "/tmp")

SET(CPACK_GENERATOR "DEB")

ENDIF(EXISTS "${CMAKE_ROOT}/Modules/CPack.cmake")

# === add additional files to package

INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/Python/FindDuplicates.py DESTINATION ${DEB_INSTALL_DIR}/bin/)
INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/Python/MatchboxLib.py DESTINATION ${DEB_INSTALL_DIR}/bin/)

IF (withLibs)
	SET(DEB_OPENCV "")
	foreach(_ml ${OpenCV_LIB_DIR})
		FILE(GLOB MYOPENCV ${_ml}/libopencv_*.so*)
		set(DEB_OPENCV ${DEB_OPENCV} ${MYOPENCV})
	endforeach()
	IF(DEB_OPENCV)
		foreach(_ml ${DEB_OPENCV})
			INSTALL(FILES ${_ml} DESTINATION ${DEB_INSTALL_DIR}/lib/)
		endforeach(_ml)
	ENDIF()

ENDIF (withLibs)

# === add sub-projects for compilation
add_subdirectory(DPQAlib)
add_subdirectory(DPQA_Compare)
add_subdirectory(DPQA_ExtractFeatures)
add_subdirectory(DPQA_Train)

# === declare make install parameters

INCLUDE(CPack)
