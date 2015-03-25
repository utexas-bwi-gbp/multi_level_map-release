Name:           ros-hydro-multi-level-map-utils
Version:        0.1.1
Release:        0%{?dist}
Summary:        ROS multi_level_map_utils package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/multi_level_map_utils
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-bwi-tools
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-multi-level-map-msgs
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-python-qt-binding
Requires:       ros-hydro-qt-gui
Requires:       ros-hydro-rospy
Requires:       ros-hydro-rqt-gui
Requires:       ros-hydro-rqt-gui-py
BuildRequires:  boost-devel
BuildRequires:  ros-hydro-catkin

%description
Contains utilities like a level multiplexer, a level selector and other utility
functions.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Mar 24 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.1.1-0
- Autogenerated by Bloom

* Sat Mar 14 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.1.0-0
- Autogenerated by Bloom

