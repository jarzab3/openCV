# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.9

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.9.4_1/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.9.4_1/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/adam/Documents/programming/openCV/openInC/autoColor

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/adam/Documents/programming/openCV/openInC/autoColor

# Include any dependencies generated for this target.
include CMakeFiles/autoColor.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/autoColor.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/autoColor.dir/flags.make

CMakeFiles/autoColor.dir/autoColor.cpp.o: CMakeFiles/autoColor.dir/flags.make
CMakeFiles/autoColor.dir/autoColor.cpp.o: autoColor.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/adam/Documents/programming/openCV/openInC/autoColor/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/autoColor.dir/autoColor.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/autoColor.dir/autoColor.cpp.o -c /Users/adam/Documents/programming/openCV/openInC/autoColor/autoColor.cpp

CMakeFiles/autoColor.dir/autoColor.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/autoColor.dir/autoColor.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/adam/Documents/programming/openCV/openInC/autoColor/autoColor.cpp > CMakeFiles/autoColor.dir/autoColor.cpp.i

CMakeFiles/autoColor.dir/autoColor.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/autoColor.dir/autoColor.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/adam/Documents/programming/openCV/openInC/autoColor/autoColor.cpp -o CMakeFiles/autoColor.dir/autoColor.cpp.s

CMakeFiles/autoColor.dir/autoColor.cpp.o.requires:

.PHONY : CMakeFiles/autoColor.dir/autoColor.cpp.o.requires

CMakeFiles/autoColor.dir/autoColor.cpp.o.provides: CMakeFiles/autoColor.dir/autoColor.cpp.o.requires
	$(MAKE) -f CMakeFiles/autoColor.dir/build.make CMakeFiles/autoColor.dir/autoColor.cpp.o.provides.build
.PHONY : CMakeFiles/autoColor.dir/autoColor.cpp.o.provides

CMakeFiles/autoColor.dir/autoColor.cpp.o.provides.build: CMakeFiles/autoColor.dir/autoColor.cpp.o


# Object files for target autoColor
autoColor_OBJECTS = \
"CMakeFiles/autoColor.dir/autoColor.cpp.o"

# External object files for target autoColor
autoColor_EXTERNAL_OBJECTS =

autoColor: CMakeFiles/autoColor.dir/autoColor.cpp.o
autoColor: CMakeFiles/autoColor.dir/build.make
autoColor: /usr/local/lib/libopencv_dnn.3.3.1.dylib
autoColor: /usr/local/lib/libopencv_ml.3.3.1.dylib
autoColor: /usr/local/lib/libopencv_objdetect.3.3.1.dylib
autoColor: /usr/local/lib/libopencv_shape.3.3.1.dylib
autoColor: /usr/local/lib/libopencv_stitching.3.3.1.dylib
autoColor: /usr/local/lib/libopencv_superres.3.3.1.dylib
autoColor: /usr/local/lib/libopencv_videostab.3.3.1.dylib
autoColor: /usr/local/lib/libopencv_calib3d.3.3.1.dylib
autoColor: /usr/local/lib/libopencv_features2d.3.3.1.dylib
autoColor: /usr/local/lib/libopencv_flann.3.3.1.dylib
autoColor: /usr/local/lib/libopencv_highgui.3.3.1.dylib
autoColor: /usr/local/lib/libopencv_photo.3.3.1.dylib
autoColor: /usr/local/lib/libopencv_video.3.3.1.dylib
autoColor: /usr/local/lib/libopencv_videoio.3.3.1.dylib
autoColor: /usr/local/lib/libopencv_imgcodecs.3.3.1.dylib
autoColor: /usr/local/lib/libopencv_imgproc.3.3.1.dylib
autoColor: /usr/local/lib/libopencv_core.3.3.1.dylib
autoColor: CMakeFiles/autoColor.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/adam/Documents/programming/openCV/openInC/autoColor/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable autoColor"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/autoColor.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/autoColor.dir/build: autoColor

.PHONY : CMakeFiles/autoColor.dir/build

CMakeFiles/autoColor.dir/requires: CMakeFiles/autoColor.dir/autoColor.cpp.o.requires

.PHONY : CMakeFiles/autoColor.dir/requires

CMakeFiles/autoColor.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/autoColor.dir/cmake_clean.cmake
.PHONY : CMakeFiles/autoColor.dir/clean

CMakeFiles/autoColor.dir/depend:
	cd /Users/adam/Documents/programming/openCV/openInC/autoColor && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/adam/Documents/programming/openCV/openInC/autoColor /Users/adam/Documents/programming/openCV/openInC/autoColor /Users/adam/Documents/programming/openCV/openInC/autoColor /Users/adam/Documents/programming/openCV/openInC/autoColor /Users/adam/Documents/programming/openCV/openInC/autoColor/CMakeFiles/autoColor.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/autoColor.dir/depend

