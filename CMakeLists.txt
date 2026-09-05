cmake_minimum_required(VERSION 3.8)
project(ros2_fundamentals_examples)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

set(dependencies
  rclcpp
  std_msgs
)

include_directories(
  include
)

# C++ publisher
add_executable(minimal_cpp_publisher src/cpp_minimal_publisher.cpp)
ament_target_dependencies(minimal_cpp_publisher ${dependencies})

# C++ subscriber
add_executable(minimal_cpp_subscriber src/cpp_minimal_subscriber.cpp)
ament_target_dependencies(minimal_cpp_subscriber ${dependencies})

# Install C++ executables
install(
  TARGETS
    minimal_cpp_publisher
    minimal_cpp_subscriber
  DESTINATION lib/${PROJECT_NAME}
)

# Install Python package
ament_python_install_package(${PROJECT_NAME})

# Install Python scripts
install(
  PROGRAMS
    ros2_fundamentals_examples/py_minimal_publisher.py
    ros2_fundamentals_examples/py_minimal_subscriber.py
  DESTINATION lib/${PROJECT_NAME}
)

# Install include directory
install(
  DIRECTORY include/
  DESTINATION include
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)

  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)

  ament_lint_auto_find_test_dependencies()
endif()

ament_export_include_directories(include)

ament_package()