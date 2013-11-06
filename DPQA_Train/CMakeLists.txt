
set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}")

# include dependencies
include_directories(${CMAKE_SOURCE_DIR}/DPQAlib)

# include sources
FILE (GLOB DPQA_Train_FILES  *.cpp)
set(DPQA_Train_SRC ${DPQA_Train_FILES})

set(TRAINBIN "mb_train")

add_executable(${TRAINBIN} ${DPQA_Train_SRC})

target_link_libraries(${TRAINBIN} DPQAlib)
target_link_libraries(${TRAINBIN} ${OpenCV_LIBS})
target_link_libraries(${TRAINBIN} ${Boost_LIBRARIES})

install(TARGETS ${TRAINBIN} DESTINATION ${DEB_INSTALL_DIR}/bin)
