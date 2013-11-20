
set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}")

set(OpenCV_DIR "/usr/local/share/OpenCV/")

FILE (GLOB DPQAlib_FILES  *.cpp)

set(DPQAlibSrcs ${DPQAlib_FILES})

# using a shared library has problems in windows
add_library(DPQAlib STATIC ${DPQAlibSrcs})
target_link_libraries(DPQAlib ${OpenCV_LIBRARIES})
target_link_libraries(DPQAlib ${Boost_LIBRARIES})

install(TARGETS DPQAlib DESTINATION ${DEB_INSTALL_DIR}/lib)
