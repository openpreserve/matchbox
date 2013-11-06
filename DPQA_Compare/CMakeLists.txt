
set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}")

# include dependencies
include_directories(${CMAKE_SOURCE_DIR}/DPQAlib)

# include sources
FILE (GLOB DPQA_Compare_FILES  *.cpp)
set(DPQA_Compare_SRC ${DPQA_Compare_FILES})

set(COMPBIN "mb_compare")

add_executable(${COMPBIN} ${DPQA_Compare_SRC})

target_link_libraries(${COMPBIN} ${OpenCV_LIBS} DPQAlib)
target_link_libraries(${COMPBIN} ${OpenCV_LIBS})
target_link_libraries(${COMPBIN} ${Boost_LIBRARIES})

install(TARGETS ${COMPBIN} DESTINATION ${DEB_INSTALL_DIR}/bin)
