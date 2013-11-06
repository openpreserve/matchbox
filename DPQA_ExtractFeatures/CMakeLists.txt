
set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}")

include_directories(${CMAKE_SOURCE_DIR}/DPQAlib)

# include sources
FILE (GLOB DPQA_Extract_FILES  *.cpp)
set(DPQA_Extract_SRC ${DPQA_Extract_FILES})

set(EFBIN "mb_extractfeatures")

add_executable(${EFBIN} ${DPQA_Extract_SRC})

target_link_libraries(${EFBIN} DPQAlib)
target_link_libraries(${EFBIN} ${Boost_LIBRARIES})
target_link_libraries(${EFBIN} ${OpenCV_LIBS})

install(TARGETS ${EFBIN} DESTINATION ${DEB_INSTALL_DIR}/bin)
